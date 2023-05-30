def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        print("No se puede dividir entre cero.")
        return None

# Solicitar el primer valor al usuario
valor1 = float(input("Ingrese el primer valor: "))
resultado = valor1

while True:
    operador = input("Ingrese el operador (+, -, *, /) o '=' para obtener el resultado: ")

    if operador == '=':
        break

    valor2 = float(input("Ingrese el siguiente valor: "))

    if operador == '+':
        resultado = sumar(resultado, valor2)
    elif operador == '-':
        resultado = restar(resultado, valor2)
    elif operador == '*':
        resultado = multiplicar(resultado, valor2)
    elif operador == '/':
        resultado = dividir(resultado, valor2)
    else:
        print("Operador inválido.")

# Mostrar el resultado final
print("El resultado es:", resultado)