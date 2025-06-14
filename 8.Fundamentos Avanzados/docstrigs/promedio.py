def calculate_average(numbers):
  """
  Calcula el promedio de una lista de numeros.
  
  parametros:
  numbers (list): Una lista de numeros enteros o flotantes.
  
  Retorna:
  Float El promedio de los numeros en la lista.
  """
  return sum(numbers) / len(numbers)

# Imprimiendo el resultado de la función
print(calculate_average([1, 2, 3, 4, 5]))  # Salida: 3.0
