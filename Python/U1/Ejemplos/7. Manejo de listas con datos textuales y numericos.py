# **Manejo de listas con valores numéricos y valores textuales**
letras = ["a","b","c","d","e","f","g"]
print(letras)
numeros =[1,2,8,5,6]
print(numeros)

#  **Reemplazando algunos valores en las listas**
letras[2:5]=[ ] #se eliminan las letras de la posición 2 a la 4 la c,d y e
print(letras)

# **Sustituyendo letras**
letras[ 1:2 ] = ['B','F']
print(letras)
# **Instrucción len para calcular el tamaño de la lista**
print(len(letras))
print(len (numeros))
