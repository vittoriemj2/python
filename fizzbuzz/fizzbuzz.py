# Como usuario de la aplicación quiero que se clasifique cualquier número entero según 
# sea múltiplo de 3, de 5, de ambos o de ninguno para que el juego muestre 
# la respuesta correcta.

# multiplo 3 -> fizz
# multiplo 5 -> buzz
# multiplo 3 y multiplo 5 -> fizzbuzz

# ninguno -> valor del número entero

def es_multiplo(num):

    if (num%3==0) and (num%5==0):
        return "fizzbuzz"

    if (num%3==0):
        return "fizz"

    if (num%5==0):
        return "buzz"

    return num

print(es_multiplo(15))

