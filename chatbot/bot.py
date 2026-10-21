print("==CHATBOT V1==")
nombre = input("¿Cual es tu nombre? ")
print(f" Hola {nombre}, escribime algo (por ejemplo: hola, contame un chiste, adios)")
mensaje=input("Vos: ")
mensaje=mensaje.lower()
if "hola" in mensaje:
	print("Bot: ¡Hola! ¿En que puedo ayudarte?")
elif "chiste" in mensaje:
  print("¿Qué le dice un jardinero a otro? Nos vemos cuando podamos.")
elif "adios" in mensaje:
	print(f"Bot: Adios! {nombre}")
else:
	print("Bot: No te entendí muy bien, ¡pero estoy aprendiendo!")