from codebreaker import Codebreaker

INTENTOS_TOTALES = 10

def jugar_codebreaker():
    """
    Función principal que ejecuta el juego Codebreaker.
    """
    true_number = "1010"  # Define el número verdadero aquí
    codebreaker = Codebreaker(true_number)
    intento = 0

    print('Jugar Codebreaker!')

    while intento < INTENTOS_TOTALES:
        number = input('Número: ')
        resolve = codebreaker.adivinar(number)
        print(resolve)
        if resolve:
            print('¡Ganaste!')
            break
        intento += 1
    else:
        print('Agotaste tus intentos. Perdiste.')

if __name__ == '__main__':
    jugar_codebreaker()
