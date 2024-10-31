#Codigo 2
print (" ")
print("Piedra Gonzalez Rodrigo Examen segundo parcial 3W 1204!")
print (" ")

curso = {'Matemáticas': 6, 'Física': 4, 'Química': 5}   #Creamos un diccionario con la variable curso
total_creditos = 0   #Asiganamos a la variable total credios 0
for asignatura, creditos in curso.items():     # para signatura creditos en curso devolvemos objeto
    print(asignatura, 'tiene', creditos, 'créditos')  #imprimimos los creditos de la asignatura
    total_creditos += creditos                             #sumamos el total de los creditos 
print('Número total de créditos del curso: ', total_creditos)     #imprimimos el resultado