##################### Ejercicio Final ##############################
# Desarrollar un chatbot en python que nos pida que le digamos algo
# y tome eso que le decimos, analice el sentimiento y nos responda
# cual es el sentimiento


# import pip
# pip.main(['install','textblob'])

# Esto es muy soso, simple, imprefecto, impreciso:

# from textblob import TextBlob

# class AnalizadorDeSentimientos:
#     def analizar_sentimiento(self,texto):
#         analisis = TextBlob(texto)
#         if analisis.sentiment.polarity > 0:
#             return "positivo"
#         elif analisis.sentiment.polarity == 0:
#             return 'neutral'
#         else:
#             return 'negativo'

# analizador = AnalizadorDeSentimientos()
# resultado = analizador.analizar_sentimiento('Today i feel bad')
# print(resultado)

# Mejor usar esta version:
# import pip
# pip.main(['install','openai'])
import openai 

client = openai.OpenAI(api_key="sk-proj-vbOHDulkPOHeZ4qGPDG9T3BlbkFJN06afL7XIMrDfTBxsFWH")

system_rol = '''Haz de cuenta que eres un analizador de sentimientos.
Yo te paso sentimientos y tú analizas el sentimiento de los mensajes
y me das una respuesta con al menos 1 caracter y como maximo 4 caracteres
SOLO RESPUESTAS NUMERICAS. Donde -1 = es negatividad máxima, 0 es neutral y
1 es positividad maxima. Puedes ir entre esos rangos, es decir 0.3, -0.5, etc 
tambien son validos (Solo puedes responder con ints o floats) '''

mensajes = [{'role': 'system', 'content': system_rol }]

class AnalizadorDeSentimientos:
    def analizar_sentimiento(self, polaridad):
        if polaridad > -0.8 and polaridad <= -0.3:
            return '\x1b[1;31m' + 'Negativo'  + '\x1b[0;37m' # Esto es para darle un color al texto
        elif polaridad > -0.3 and polaridad < -0.1:
            return '\x1b[1;31m' + 'Algo negativo' + '\x1b[0;37m'
        elif polaridad >= -0.1 and polaridad <= 0.1:
            return '\x1b[1;33m' + 'Neutral' + '\x1b[0;37m'
        elif polaridad > 0.1 and polaridad <= 0.4:
            return '\x1b[1;32m' + 'Algo positivo' + '\x1b[0;37m'
        elif polaridad > 0.4 and polaridad <= 0.9:
            return '\x1b[1;32m' + 'Positivo' + '\x1b[0;37m'
        elif polaridad > 0.9:
            return '\x1b[1;32m' + 'Muy positivo' + '\x1b[0;37m'
        else:
            return '\x1b[1;31m' + 'Muy Negativo' + '\x1b[0;37m'
        
analizador = AnalizadorDeSentimientos()

while True:
    user_prompt = input('\x1b[1;33m' + '\nDime algo... \n'  + '\x1b[0;37m')
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