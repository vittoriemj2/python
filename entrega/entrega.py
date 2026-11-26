def fizzbuzz(num):
    # 1) Primero lo MÁS ESPECÍFICO: múltiplo de 3 Y de 5 a la vez (15, 30, 45...).
    #    Va primero porque si no, el "if" de 3 o el de 5 lo atrapan antes.
    #    El 0 también entra acá, porque 0 % 3 == 0 y 0 % 5 == 0.
    
    if num % 3 == 0 and num % 5 == 0:  # % es el resto de la división; resto 0 = es múltiplo
        return "FizzBuzz"              # return corta la función: no se evalúa nada más

    # 2) Después, solo múltiplo de 3 (los de 3 y 5 ya salieron arriba)
    if num % 3 == 0:
        return "Fizz"

    # 3) Después, solo múltiplo de 5
    if num % 5 == 0:
        return "Buzz"

    # 4) Si no cumplió ninguna regla, devuelve el mismo número
    return num