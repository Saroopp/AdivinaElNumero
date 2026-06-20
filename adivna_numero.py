# Proyecto: Adivina el Número
# Autor: Sarahi Paredes
# Lógica de Programación

print("================================")
print(" A D I V I N A   E L   N Ú M E R O ")
print("================================")

# Variable para controlar si el usuario desea volver a jugar
jugar = "si"

while jugar == "si":

    # Inicialización de variables
    minimo = 1
    maximo = 100
    intentos = 0

    print("\nPiensa un número entre 1 y 100")

    while True:

        # Contador de intentos
        intentos += 1

        # Cálculo del número propuesto
        intento = (minimo + maximo) // 2

        print(f"\n¿Tu número es {intento}?")

        respuesta = input(
            "Escriba mayor, menor o correcto: "
        ).lower()

        # Evaluación de la respuesta
        if respuesta == "correcto":

            print(
                f"\n¡Número encontrado en {intentos} intentos!"
            )

            break

        elif respuesta == "mayor":

            minimo = intento + 1

        elif respuesta == "menor":

            maximo = intento - 1

        else:

            print(
                "\nRespuesta inválida. Use mayor, menor o correcto."
            )

    # Preguntar si desea jugar nuevamente
    jugar = input(
        "\n¿Desea jugar nuevamente? (si/no): "
    ).lower()

print("\nGracias por utilizar el programa.")

