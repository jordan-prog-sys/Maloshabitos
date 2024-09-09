def calcular(variable1, variable2, variable3):
    resultado = variable1 * variable2 + variable3
    return resultado

def principal():
    numero1 = float(input("Ingresar numero 1: "))
    numero2 = float(input("Ingresar numero 2: "))
    numero3 = float(input("Ingresar numero 3: "))
    resultado = calcular(numero1, numero2, numero3)
    print("El resultado es:", resultado)

principal()
