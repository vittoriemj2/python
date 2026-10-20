print("==CHATBOT V1==")
nombre = input("¿Cual es tu nombre? ")
print(f" Hola {nombre}, escribime algo (por ejemplo: hola, contame un chiste, adios)")
mensaje=input("Vos: ")
mensaje=mensaje.lower()
if "hola" in mensaje:
	print("Bot: ¡Hola! ¿En que puedo ayudarte?")
else:
	print("Bot: No entendí muy bien, pero estoy aprendiendo!")