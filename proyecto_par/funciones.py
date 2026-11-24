def es_par(num):
    """Indica si un número es par o impar.

    Args:
        num (int): Número a evaluar.

    Returns:
        str: "par" si el número es divisible por 2,
        "impar" en caso contrario.
    """
    if (num==0):
      return "Es Cero"
    if (num%2==0):
        return "par"
    return "impar"

print(es_par(0))


def separar_pares_impares(nums):
    """Recibe una lista de números y devuelve dos listas: pares e impares."""
    pares = []
    impares = []
    for num in nums:
        if es_par(num) == "par":
            pares.append(num)
        else:
            impares.append(num)
    return pares, impares


nums = [8,9,0,4,5]
pares, impares = separar_pares_impares(nums)
print("Números:", nums)
print("Pares:", pares)
print("Impares:", impares)