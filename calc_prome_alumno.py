print("Sistema para calcular el promedio de un alumno.")
nombre = input("Para comenzar, ¿Cuál es tu nombre?: ")
nota_uno = int(input(nombre +" ¿Cuál es tu calificación en matemática?: "))
nota_dos = int(input(nombre +" ¿Cuál es tu calificación en química?: "))
nota_tres = int(input(nombre +" ¿Cuál es tu calificación en biología?: "))
promedio = (nota_uno + nota_dos + nota_tres) / 3
if promedio >= 6:
    print("Felicidades " + nombre + " aprobaste con un promedio de " + str(promedio) + " de calificación.")
else:
    print("No has aprobado " + nombre + " tu promedio es: " + str(promedio) +" de calificación.")



