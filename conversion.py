menu = """
Bienvenido al conversor de monedas 馃挵

1. Pesos colombianos
2. Pesos argentinos
3. Pesos mexicanos

Elige una opci贸n: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("驴Cu谩ntos pesos colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 4490
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " d贸lares" )
elif opcion == 2:
    pesos = input("驴Cu谩ntos pesos argentinos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 128
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " d贸lares" )
elif opcion == 3:
    pesos = input("驴Cu谩ntos pesos mexicanos tienes tienes?: ")
    pesos = float(pesos)
    valor_dolar = 21
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " d贸lares" )
else:
    print("Ingresa una opci贸n correcta por favor.")


