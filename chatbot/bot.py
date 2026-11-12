ARCHIVO="conversacion.txt"


def mostrar_bienvenida(nombre):
	print("=== Chatbot con decisiones ===")
	print(f"¡Hola {nombre}! Escribime algo (por ejemplo: hola, contame un chiste, chau)")
print("Escribí salir o adios o adiós o bye o chau para terminar")

def main():
  with open(ARCHIVO,"w",encoding="utf-8") as archivo:
    archivo.write("Historial de la conversación")
    nombre = input("¿Cómo te llamás? ")
    mostrar_bienvenida(nombre)
    cantidad_mensajes = 0
    # Diccionario: clave = palabra que buscamos, valor = respuesta del bot
    respuestas = {
        "hola": "¡Hola! ¿Cómo estás?",
        "chiste": "¿Qué le dice un jardinero a otro? Nos vemos cuando podamos.",
        "no hablar": "Intentalo de nuevo...",
        "nose": "No te aflijas, ¿Puedo contarte algo mío? Por ejemplo hoy tengo mucho sueño.",
    }
    # Palabras que finalizan la conversación
    palabras_salida = ["salir", "adios", "adiós", "bye", "chau"]
    # Bucle principal del chatbot
    while True:
        mensaje = input("Vos: ").lower()
        archivo.write(f"Mensaje transmitido : {mensaje}\n")
        cantidad_mensajes += 1
        # Comprobamos si el usuario quiere salir
        if mensaje in palabras_salida:
            print("Bot: ¡Listo! Fue un gusto charlar, nos vemos.")
            print(f"Cantidad de mensajes recibidos: {cantidad_mensajes}")
            break
        # Buscamos si alguna clave del diccionario está contenida en el mensaje
        encontrada = False
        for clave in respuestas:
            if clave in mensaje:
                print(f"Bot: {respuestas[clave]}")
                encontrada = True
                break
        # Si no encontramos ninguna palabra conocida
    if not encontrada:
        print("Bot: No te entendí muy bien, ¡pero estoy aprendiendo!")
    
if __name__=="__main__":
    main()