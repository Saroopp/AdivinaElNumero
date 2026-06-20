print("================================")
print("A D I V I N A   E L   N Ú M E R O")
print("================================")

print("Piensa un número entre 1 y 100")

minimo = 1
maximo = 100

while True:

    intento = (minimo + maximo) // 2

    print(f"\n¿Tu número es {intento}?")

    respuesta = input("Escriba mayor, menor o correcto: ").lower()

    if respuesta == "correcto":
        print("¡Número encontrado!")
        break

    elif respuesta == "mayor":
        minimo = intento + 1

    elif respuesta == "menor":
        maximo = intento - 1

    else:
        print("Respuesta no válida")
