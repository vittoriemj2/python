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



def par_o_impar(nums):
    par_impar_list=[] 
    for num in nums:
        par_impar_list.append(es_par(num))
    return par_impar_list

nums=[8,9,0,4,5]
par_impar_list=par_o_impar(nums)
print(par_impar_list)