
def Seleccionar(entrada):
    """esta funcion retorna un numero entero mayor a 0"""
    while (entrada):
        try:
            numero = int(entrada)
            if numero > 0 and numero < 5:
                entrada = False
            else:
                entrada = input("Ingrese una opcion correcta\n") 
        except:
            entrada = input("ingrese una opcion correcta\n")
    return int(numero)         


opcion = input ("Elija la opcion deseada\n 1 Calculadora Clasica\n 2 Calculadora de Fracciones\n 3 Calculadora de Conversiones\n 4 OFF\n ")
opcion = Seleccionar(opcion)
if opcion == 4:
    print ("OFF")
elif opcion == 1:
    """codigo a ejucutar si el usuario selecciona calculadora clasica"""
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
    valor1 = float(input("Ingrese el primer valor:\n "))
    resultado = valor1
    salida = True
    while salida is True:
        operador = input("Ingrese el operador (+, -, *, /) o '=' para obtener el resultado: \n")
        
        if operador == "=":
            salida = False
        else:
            valor2 = float(input("Ingrese el siguiente valor: \n"))

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
    print("El resultado es:\n", resultado)
       
        



    
elif opcion == 2:
    """codigo a ejucutar si el usuario selecciona calculadora de fracciones"""

elif opcion == 3:
    """codigo a ejecutar si el usuario selecciona calculadora de conversion"""
    
