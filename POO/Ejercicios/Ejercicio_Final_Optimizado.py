import openai 
import os
from dotenv import load_dotenv

load_dotenv()

apiKey = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=apiKey)

system_rol = '''Haz de cuenta que eres un analizador de sentimientos.
Yo te paso sentimientos y tú analizas el sentimiento de los mensajes
y me das una respuesta con al menos 1 caracter y como maximo 4 caracteres
SOLO RESPUESTAS NUMERICAS. Donde -1 = es negatividad máxima, 0 es neutral y
1 es positividad maxima. Puedes ir entre esos rangos, es decir 0.3, -0.5, etc 
tambien son validos (Solo puedes responder con ints o floats) '''

mensajes = [{'role': 'system', 'content': system_rol }]

class Sentimiento:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
        
    def __str__(self) -> str:
        return '\x1b[1;{}m{}\x1b[0;37m'.format(self.color, self.nombre)

class AnalizadorDeSentimientos:
    def __init__(self, rangos):
        self.rangos = rangos
    
    def analizar_sentimiento(self, polaridad):
        for rango, sentimiento in self.rangos:
           if rango[0] < polaridad <= rango[1]:
               return sentimiento
        
        return Sentimiento('Muy negativo', '31')
  
       
rangos = [
    ((-0.6, -0.3), Sentimiento('Negativo', '31')),
    ((-0.3, -0.1), Sentimiento('Algo negativo', '31')),
    ((-0.1, 0.1), Sentimiento('Neutral', '33')),
    ((0.1, 0.4), Sentimiento('Algo positivo', '32')),
    ((0.4, 0.9), Sentimiento('Positivo', '32')),
    ((0.9, 1), Sentimiento('Muy positivo', '32'))
]
            
analizador = AnalizadorDeSentimientos(rangos)

while True:
    user_prompt = input('\x1b[1;33m' + '\nDime algo: '  + '\x1b[0;37m')
    mensajes.append({'role': 'user', 'content': user_prompt})

    completion = client.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = mensajes,
        max_tokens = 8
    )
    respuesta = completion.choices[0].message.content.strip()
    mensajes.append({'role': 'assistant', 'content': respuesta})
    
    sentimiento = analizador.analizar_sentimiento(float(respuesta))
    print(sentimiento)