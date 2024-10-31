#Codigo 1
print (" ")
print("Piedra Gonzalez Rodrigo Examen segundo parcial 3W 1204!")
print (" ")


Materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]   #creamos una lista con lsa materias
aprobados = []  #Creamos una lista vacia para las materias
for Materia in Materias:       #Para  la materia en las materias
    Calif = float(input("¿Qué nota has sacado en " + Materia + "?"))  #cramos una variable calificacion donde pedimos ingresar la nota y la guardamos en calif
    if Calif >= 5:   #Si calificacion es mayor o igual a 5
        aprobados.append(Materia)    #Añadimos elemntos a aprobados
for Materia in aprobados:  #Para materia en aprbados 
    Materias.remove(Materia)   #Removemos las materias aprobadas
print("Tienes que recursar " + str(Materias))  #imprimimos el resultado con las materias repetidas o recursadas