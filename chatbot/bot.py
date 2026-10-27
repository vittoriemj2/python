print("==CHATBOT V3==")
chiste="Mozo, ese filete tiene muchos nervios. Pues normal, es la primera vez que se lo comen."
Nombre=input("¿Cual es tu nombre?")
print(f" Hola {Nombre}, escribime algo (por ejemplo: hola, contame un chiste, adios)")
cantidad_mensajes=0
respuestas = {
    "hola": "¡Hola! ¿Cómo estás?",
    "chiste": "¿Qué le dice un jardinero a otro? Nos vemos cuando podamos.",
    "no hablar": "Intentalo de nuevo...",
    "nose": "No te aflijas, ¿Puedo contarte algo mío? Por ejemplo hoy tengo mucho sueño
}
while True:
  cantidad_mensajes=cantidad_mensajes+1
  mensaje=input("Vos: ")
  mensaje=mensaje.lower()
  if "hola" in mensaje:
    print("Bot: ¡Hola! ¿En que puedo ayudarte?")
  elif "chiste" in mensaje or "broma" in mensaje or "bromita" in mensaje or "joda" in mensaje:
    print(chiste)
  elif "adios" in mensaje or "chau" in mensaje or "adiós" in mensaje or "nos vemos" in mensaje or "hasta luego" in mensaje or "bye" in mensaje:
    print(f"Bot: Adios! {Nombre}")
    print(f"Cantidad de mensajes enviados = : {cantidad_mensajes}")
    break
  elif mensaje=="":
    print("Bot: Intentalo de nuevo...")
  elif len(mensaje)>40:
    print("Bot: Me encanta que te guste conversar")
  else:
    print("No te entendí muy bien, ¡pero estoy aprendiendo!")