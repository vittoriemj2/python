print("==CHATBOT V3==")
chiste="Mozo, ese filete tiene muchos nervios. Pues normal, es la primera vez que se lo comen."
Nombre=input("¿Cual es tu nombre?")
print(f" Hola {Nombre}, escribime algo (por ejemplo: hola, contame un chiste, adios)")
cantidad_mensajes=0
respuestas = {
    "hola": "¡Hola! ¿Cómo estás?",
    "chiste": "¿Qué le dice un jardinero a otro? Nos vemos cuando podamos.",
    "no hablar": "Intentalo de nuevo...",
    "nose": "No te aflijas, ¿Puedo contarte algo mío? Por ejemplo hoy tengo mucho sueño"
}
palabras_salida=["bye","adios","hasta luego","chau","nos vemos","adiós","salir"]

while True:
  cantidad_mensajes +=1
  mensaje=input("Vos: ")
  mensaje=mensaje.lower()
  if mensaje in palabras_salida:
  	print("Bot: ¡Listo! Fue un gusto charlar, nos vemos.")
    print(f"Cantidad de mensajes : {cantidad_mensajes}")
    break
  for clave in respuestas:
  	if clave in mensaje:
    		print(respuestas[clave])
        break