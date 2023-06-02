
## Menu Principal Calculadora 
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
       
OFF = False

while OFF is False:
    opcion = input ("Elija la opción deseada\n 1 Calculadora Clásica\n 2 Calculadora de Fracciones\n 3 Calculadora de Conversiones\n 4 OFF\n ")
    opcion = Seleccionar(opcion)

    if opcion == 4:
        print ("OFF")
        OFF = True

    elif opcion == 1:
        """codigo a ejucutar si el usuario selecciona calculadora clasica
        Usaremos el comando import """
        print ("Calculadora Clásica\n")
        import Calculadora_Clasica_Yeremi
    
    elif opcion == 2:
        """codigo a ejucutar si el usuario selecciona calculadora de fracciones
        Usaremos el comando import"""
        print ("Calculadora de Fracciones\n")

    elif opcion == 3:
        """codigo a ejecutar si el usuario selecciona calculadora de conversion
        Usaremos el comando import"""
        print ("Calculadora de Conversiones\n")
    
