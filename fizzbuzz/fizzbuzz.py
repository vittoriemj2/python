# Como usuario de la aplicación quiero que se clasifique cualquier número entero según 
# sea múltiplo de 3, de 5, de ambos o de ninguno para que el juego muestre 
# la respuesta correcta.

# multiplo 3 -> fizz
# multiplo 5 -> buzz
# multiplo 3 y multiplo 5 -> fizzbuzz

# ninguno -> valor del número entero

def es_multiplo(num):
    """
    Clasifica un número según las reglas de FizzBuzz.

    Args:
        num (int): Número a evaluar.

    Returns:
        str | int: "fizzbuzz" si es múltiplo de 3 y de 5,
        "fizz" si es múltiplo de 3,
        "buzz" si es múltiplo de 5,
        o el mismo número si no es múltiplo de ninguno.
    """
    if (num%3==0) and (num%5==0):
        return"fizzbuzz"
    if (num%3==0):
        return "fizz"
    if (num%5==0):
        return"buzz"
    return(num)

def es_multiplo_lista(nums):
    """
    Aplica es_multiplo a cada elemento de una lista.

    Args:
        nums (list[int]): Lista de números a evaluar.

    Returns:
        list: Lista nueva, en el mismo orden que la original, con el
        resultado de es_multiplo para cada número.
        Ejemplo: [3, 5, 15, 10, 8] -> ["fizz", "buzz", "fizzbuzz", "buzz", 8]
    """
    fizzbuzz_list=[]
    for num in nums:
        fizzbuzz_list.append(es_multiplo(num))
    return fizzbuzz_list
