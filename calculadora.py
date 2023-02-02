import os

def menu():
    os.system("cls")
    print("     Calculadora Geométrica")
    print("------------------------------")
    print("1 - Calcular área do triângulo")
    print("2 - Calcular área do retângulo")
    print("3 - Calcular área do quadrado")
    print("4 - Calcular área do trapézio")
    print("5 - Calcular área do círculo")
    print("           6 -sair")
    x = input("   Escolha a opção desejada:")
    if x.isdigit() and len(x) == 1:
        return x
    else:
        return "erro"

def areaTriangulo():
    os.system("cls")
    base = input("Medida da base: ")
    altura = input("Medida da altura: ")
    return int(base) * int(altura) / 2

def areaRetangulo():
    os.system("cls")
    base = input("Medida da base: ")
    altura = input("Medida da altura: ")
    return int(base) * int(altura)

def areaQuadrado():
    os.system("cls")
    lado = input("Medida do lado: ")
    return int(lado)**2
def areaTrapezio():
    os.system("cls")
    baseMenor = input("Medida da base menor: ")
    baseMaior = input("Medida da base maior: ")
    altura = input("Medida da altura: ")
    return (int(baseMenor) + int(baseMaior)) * int(altura) /2

def areaCirculo():
    os.system("cls")
    pi = 3.14
    raio = input("Medida do raio: ")
    return (int(raio)**2) * pi

while True:
    resposta = menu()
    if resposta == "6":
        break
    elif resposta == "1":
        triangulo = areaTriangulo()
        print(f"A área do triângulo é {triangulo}")
    elif resposta == "2":
        retangulo = areaRetangulo()
        print(f"A área do retângulo é {retangulo}")
    elif resposta == "3":
        quadrado = areaQuadrado()
        print(f"A área do quadrado é {quadrado}")
    elif resposta == "4":
        trapezio = areaTrapezio()
        print(f"A área do trapézio é {trapezio}")
    elif resposta == "5":
        circulo = areaCirculo()
        print(f"A área do círculo é {circulo}")
    elif resposta == "erro":
        print("Escolha uma opção válida")
    input("Aperte enter para continuar...")
    
