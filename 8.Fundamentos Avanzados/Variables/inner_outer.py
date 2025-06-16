x = 'global' #Variable global
# Funcion externa
def outer_function():
  x = 'enclosing' #Variable de cierre
  
  #Funcion interna
  def inner_function():
    x = 'local' # Variable Local
    print('Inner:', x) # Imprime la variable local
    
  inner_function() # Llamada a la funcion interna
  print('Outer:', x) # Imprime la variable de cierre

outer_function() # Llamada a la funcion externa
print('Global:', x) # Imprime la variable global