#Codigo 3
print (" ")
print("Piedra Gonzalez Rodrigo Examen segundo parcial 3W 1204!")
print (" ")

materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]  #Creamos la lista con las materias ingresadas
puntuaciones = []   #Cramos una lista vacia
for materia in materias:               #para materia en las materias
    puntuacion = input("¿Qué nota has sacado en " + materia + "?")  #Preguntar que nota sacamos y la guardamos en materia
    puntuaciones.append(puntuacion)    #En la variable puntuaciones usamos el append para agregar nuevos objetos
for i in range(len(materias)):         #para i en rango imprimimos en lista
    print("En " + materias[i] + " has sacado " + puntuaciones[i])   #imprimimos el resultado