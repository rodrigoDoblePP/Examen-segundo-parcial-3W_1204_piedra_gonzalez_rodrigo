#Codigo 4
print (" ")
print("Piedra Gonzalez Rodrigo Examen segundo parcial 3W 1204!")
print (" ")

nombre = input('¿Cómo te llamas? ')   #pedimos el nombre y lo guardams en la varibale nombre
edad = input('¿Cuántos años tienes? ') #pedimos edad y la guardamos en la variable edad
direccion = input('¿Cuál es tu dirección? ')  #pedimos direccion y la guardamos en la variable direccion
telefono = input('¿Cuál es tu número de teléfono? ') #pedimos telefono y lo guardamos en la variable telefono
persona = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}  #creamos un diccionario y ponemos las variables
print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['direccion'], 'y su número de teléfono es', persona['telefono'])
#imprimimos el mensaje y lo mostramos en pantalla