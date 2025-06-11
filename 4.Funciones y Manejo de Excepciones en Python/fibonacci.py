def sum_numbers(n):
    # Caso base: si n es 0, la suma es 0
    if n == 0:
        return 0
    # Caso recursivo: n + suma de (n-1)
    else:
        return n + sum_numbers(n - 1)

# Llamada a la función
result = sum_numbers(5)
print(f"Suma de los primeros 5 números es: {result}")

def sum_numbers(n):
    """
    Calculate the sum of the first n natural numbers using recursion.

    Parameters:
    n (int): The number up to which the sum is to be calculated.

    Returns:
    int: The sum of the first n natural numbers.
    """
    # Base case: if n is 0, the sum is 0
    if n == 0:
        return 0
    # Recursive case: n plus the sum of numbers up to n-1
    else:
        return n + sum_numbers(n - 1)