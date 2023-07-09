class Codebreaker:
    def __init__(self, true_number):
        """
        Inicializa el objeto Codebreaker con el número verdadero.
        Args:
            true_number (str): El número verdadero a adivinar.
        """
        self.true_number = true_number

    def adivinar(self, numero=None):
        """
        Adivina el número ingresado y devuelve el resultado.
        Args:
            numero (str): El número a adivinar.
        Returns:
            str: El resultado de la adivinanza ('X' para dígitos correctos en la posición correcta, '_' para dígitos correctos en la posición incorrecta).
        """
        if self.true_number == '':
            return 'Number is not defined'

        if numero is None or len(numero) != 4 or 'e' not in numero:
            return 'error'

        if numero == self.true_number:
            return True

        resultadoX = ''
        resultado_ = ''
        arrayNumber = [False] * 10

        for x in range(len(numero)):
            if arrayNumber[int(numero[x])]:
                return 'error'
            arrayNumber[int(numero[x])] = True

        for index, x in enumerate(numero):
            if self.true_number[index] == x:
                resultadoX += 'X'
            elif x in self.true_number:
                resultado_ += '_'

        return resultadoX + resultado_


def jugar_codebreaker():
    true_number = "1010"
    codebreaker = Codebreaker(true_number)

    intentos_totales = 10

