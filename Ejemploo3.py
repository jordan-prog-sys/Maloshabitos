# Función para calcular el área de un rectángulo
def calcularAREArectangulo(largo, ancho):
    arearectangular = largo * ancho
    return arearectangular

# Función para calcular el área de un triángulo
def calcularAREAtrinagulo(base, altura):
    areatriangular = 0.5 * base * altura
    return areatriangular

# Función principal
def main():
    datolargo = float (input("Ingresa el numero del lado largo del rectangulo:"))
    datoancho = float (input("Ingresa el numero del lado ancho del rectangulo:"))
    rect_area = calcularAREArectangulo(datolargo, datoancho)
    print("Área del rectángulo:", rect_area)

    datobase = float (input("Ingresa el numero de la base del triangulo:"))
    datoaltura = float (input("Ingresa el numero de la altura del triangul:"))
    tri_area = calcularAREAtrinagulo(datobase, datoaltura)
    print("Área del triángulo:", tri_area)

main()
