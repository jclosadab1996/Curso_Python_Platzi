x = 5 # Variable global

def modify_global():
    global x  # Declara que se usará la variable global x
    x += 3    # Modifica la variable global
    print(f'Valor Moificado: {x}')  # Imprime el valor modificado
    
modify_global() # Llamada recursiva a la funcion
print(f'Valor Final: {x}')  # Imprime el valor final