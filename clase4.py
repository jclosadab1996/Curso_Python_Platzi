name = "Juan Camilo"  # String
last_name = "Losada Bultaif"  # Last name
caracter = "C" # Character

print(type(name))  # <class 'str'>
print(type(caracter))  # <class 'str'>

print(name[0])  # J
print(name[0:4])  # Juan

print(last_name + ' ' + name)  # Juan Camilo Losada Bultaif

print(len(name))  # 8
print(len(last_name))  # 14
print(name.lower())  # juan camilo
print(name.upper()) # JUAN CAMILO
print(last_name.strip()) # Losada Bultaif (removes leading and trailing whitespace)