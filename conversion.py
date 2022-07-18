menu = """
Bienvenido al conversor de monedas 💰

1. Pesos colombianos
2. Pesos argentinos
3. Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("¿Cuántos pesos colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 4490
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares" )
elif opcion == 2:
    pesos = input("¿Cuántos pesos argentinos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 128
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares" )
elif opcion == 3:
    pesos = input("¿Cuántos pesos mexicanos tienes tienes?: ")
    pesos = float(pesos)
    valor_dolar = 21
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares" )
else:
    print("Ingresa una opción correcta por favor.")


