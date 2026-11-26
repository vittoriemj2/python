def fizzbuzz(num):

    if num == 0:                          # el 0 va PRIMERO: si no, caería en "3 y 5" (0 % 3 y 0 % 5 dan 0)
        return 0                          # criterio 4: el 0 devuelve el valor 0
    
    if num % 3 == 0 and num % 5 == 0:     # múltiplo de 3 Y de 5; % da el resto, resto 0 = es múltiplo
        return "FizzBuzz"                 # criterio 3; va antes que 3 y 5 solos para que no lo atrapen
   
    if num % 3 == 0:                      # solo múltiplo de 3 (los de 3 y 5 ya salieron arriba)
        return "Fizz"                     # criterio 1
   
    if num % 5 == 0:                      # solo múltiplo de 5
        return "Buzz"                     # criterio 2
   
    return num                            # criterio 5: no cumple nada, devuelve el mismo número