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