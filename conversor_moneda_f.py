def conversor(pais, valor):
    pesos = float(input("¿Cuántos pesos " + pais + " tienes? "))
    dolares = pesos/valor
    dolares = round(dolares, 2)
    print("Tienes $" + str(dolares) + " dolares.")

menu = """
Bienvenido al conversor de monedas
Opción 1: Pesos mexicanos
Opcion 2: Pesos argentinos
Opcion 3: Pesos colombianos

Elige una opción: """
opcion = int(input(menu))

if opcion == 1:
    conversor("mexicanos", 20.47)
elif opcion == 2:
    conversor("argentinos", 128.90)
elif opcion == 3:
    conversor("colombianos", 4315.31)
else:
    print("Opcion no disponible.")