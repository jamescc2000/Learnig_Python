import openai # lo importamos para poder usar la API
from textblob import TextBlob # lo importamos para analizar el texto en ingles
import os # lo importamos para obtener la api key de openAI
from dotenv import load_dotenv # lo importamos para cargar la api key
from abc import ABC, abstractmethod # lo importamos para crear los metodos abastractos

# Funcion para cargar la api_key almacena en la variable de entorno
load_dotenv() 

# Obtener la varaible de entorno
apiKey = os.getenv("OPENAI_API_KEY") 

# utilizando la api key
client = openai.OpenAI(api_key=apiKey) 

# A continuacion se crea el prompt que convierte a chatgpt en un analizador de sensibildiad
system_rol = '''Haz de cuenta que eres un analizador de sentimientos.
Yo te paso sentimientos y tú analizas el sentimiento de los mensajes
y me das una respuesta con al menos 1 caracter y como maximo 4 caracteres
SOLO RESPUESTAS NUMERICAS. Donde -1 = es negatividad máxima, 0 es neutral y
1 es positividad maxima. Puedes ir entre esos rangos, es decir 0.3, -0.5, etc 
tambien son validos (Solo puedes responder con ints o floats) '''

# Se crea una lista que contendra los mensajes y el tipo de rol, en este caso se comienza con el rol de system que tendra chatgpt
mensajes_openai = [{'role': 'system', 'content': system_rol }]

# Se crea la clase Sentimiento
class Sentimiento:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
      
    # Se redefine la funcion str para cambiar la forma de mostra el objeto, dandole un nuevo formato  
    def __str__(self) -> str:
        return '\x1b[1;{}m{}\x1b[0;37m'.format(self.color, self.nombre)


# Se crea la clase padre para los diferentes tipo de analizador de sensibilidad
class AnalizadorDeSentimientos(ABC):
    def __init__(self, rangos):
        self.rangos = rangos
    
    # Se crea el metodo abstracto que deben tener todos los analizadores
    @abstractmethod
    def analizar_sentimiento(self, polaridad):
        pass


# Se crea la clase OpenAI que utilizara ChatGPT como analizador de texto
class OpenAI(AnalizadorDeSentimientos):
    # Se define la logica para mostrar los resultados del analisis
    def analizar_sentimiento(self, polaridad):
        for rango, sentimiento in self.rangos:
           if rango[0] < polaridad <= rango[1]:
               return sentimiento
        return Sentimiento('Muy negativo', '31')
    
    # Se crea otro metodo para enviar los mensajes a traves de la API
    def cargar_mensajes(self, mensajes, prompt):
        # Agregamos el texto del usuario al historial de mensajes
        mensajes.append({'role': 'user', 'content': prompt})
        
        # Creamos la consulta que se enviara a la API
        completion = client.chat.completions.create(
            model = 'gpt-3.5-turbo',
            messages = mensajes,
            max_tokens = 8
        )
        # Almacenamos la respuesta de ChatGPT en la variable respuesta
        respuesta = completion.choices[0].message.content.strip()
        
        # Agergamos la respuesta de ChatGPT al historial de mensajes
        mensajes.append({'role': 'assistant', 'content': respuesta})
        
        return respuesta
    
    
# Se crea la clase Textblob que utiliza la libreria de textblob para analizar el texto
class Textblob(AnalizadorDeSentimientos):
    # Se define la logica para mostrar los resultados del analisis, en este caso como 
    # textblob solo proceso textos en ingles, las respuestas tambien seran en ingles
    def analizar_sentimiento(self, polarity):
        for range, sensitivity in self.rangos:
           if range[0] < polarity <= range[1]:
               return sensitivity
        return Sentimiento('Very negative', '31')
    
    # Se crea otro metodo que consulta la polaridad del texto a textblob
    def cargar_mensajes(self, prompt):
        analisis = TextBlob(prompt)
        return analisis.sentiment.polarity
  
    
# Se definen los rangos de sensibilidad       
rangos_openai = [
    ((-0.6, -0.3), Sentimiento('Negativo', '31')),
    ((-0.3, -0.1), Sentimiento('Algo negativo', '31')),
    ((-0.1, 0.1), Sentimiento('Neutral', '33')),
    ((0.1, 0.4), Sentimiento('Algo positivo', '32')),
    ((0.4, 0.9), Sentimiento('Positivo', '32')),
    ((0.9, 1), Sentimiento('Muy positivo', '32'))
]

rangos_textblob = [
    ((-0.6, -0.3), Sentimiento('Negative', '31')),
    ((-0.3, -0.1), Sentimiento('A little negative', '31')),
    ((-0.1, 0.1), Sentimiento('Neutral', '33')),
    ((0.1, 0.4), Sentimiento('A little positive', '32')),
    ((0.4, 0.9), Sentimiento('Positive', '32')),
    ((0.9, 1), Sentimiento('Very positive', '32'))
]
  
# Se inicializan los analizadores de sensibilidad          
analizador_openai = OpenAI(rangos_openai)
analizador_textblob = Textblob(rangos_textblob)

# Mensaje de bienvenida y explicaciones del programa
print('######################### Bienvenido al analizador de sensibilidad de texto ###################################')
print('\n1. Ingrese el idioma en el que desea hablar\n2. Comienze a enviar texto en el idioma seleccionado\n3. Para finalizar la conversacion escriba salir o exit')

# Se crea una variable que almacenara el idioma preferido por el usuario
idioma = ''
idioma = input('\nDesea hablar en español o en ingles?: ')
idioma = idioma.lower()

# Se crea la variable de salida
salida = True

# Comienza el chat con el usuario
while salida:
    
    # Si eligio español, se utiliza openAI como analizador
    if idioma == 'español' :
        # Solicitamos al usuario que ingrese el texto a analizar
        user_prompt = input('\x1b[1;33m' + '\nDime algo: '  + '\x1b[0;37m')
        
        # Si escribio salir, cerramos el programa
        if user_prompt.lower() == 'salir':
            salida = False
        
        # Caso contrario procedemos a ejecutar los metodos del analizador    
        else:
            # Cargamos los mensajes a la API para obtener una respuesta
            respuesta = analizador_openai.cargar_mensajes(mensajes_openai, user_prompt)
            
            # Y mostramos esa respuesta
            # Nota: como la respuesta que envia ChatGPT es un string, lo convertirmos a float primero
            sentimiento = analizador_openai.analizar_sentimiento(float(respuesta))
            print(sentimiento)
        
    # Si eligio ingles, se utiliza textblob como analizador
    elif idioma == 'ingles':
        # Solicitamos al usuario que ingrese el texto a analizar
        user_prompt = input('\x1b[1;33m' + '\nTell me something: '  + '\x1b[0;37m')
        
        # Si escribio exit, cerramos el programa
        if user_prompt.lower() == 'exit':
            salida = False
          
        # Caso contrario procedemos a ejecutar los metodos del analizador   
        else:
            # Enviamos el texto para que lo analice textblob
            respuesta = analizador_textblob.cargar_mensajes(user_prompt)
            
            # Y mostramos la respuesta obtenida
            sentimiento = analizador_textblob.analizar_sentimiento(respuesta)
            print(sentimiento)
            
    # Si coloco un valor no valido        
    else:
        idioma = input('Por favor ingrese un idioma valido: ')
        
