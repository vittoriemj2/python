def fizzbuzz(num):
    if num == 0:
        return 0
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    return num


def juego(n):
    resultados = []
    for i in range(1, n + 1):
        resultados.append(fizzbuzz(i))
    return resultados