#Andrew Torrez P
#refactorizando
def menu() :
    print("""
    ******** caluladora  ***********
    1.- Sumar numeros
    2.- Restar números
    3.- Multiplicar números
    4.- division
    5.- salir
    """)

def suma(valor1, valor2) :
    return valor1 + valor2

def resta(valor1, valor2) :
    return valor1 - valor2

def multiplicacion(valor1, valor2) :
    return valor1 * valor2

def division(valor1, valor2) :
    return valor1/valor2


while True:
    menu()
    opcion = int(input("Ingrese su opcion: ")) 
    if opcion==5 :
        print("hasta luego...!!!")
        break
    contador = int(input("cuantos numeros va a calcular? ") )    
    if opcion == 1:
        for numero in range(contador):
            if numero==0:
                respuesta=suma(0,int(input("numero : ")))
            else:
                respuesta=suma(respuesta,int(input("numero : ")))
    if opcion ==2:
        for numero in range(contador):
            if numero==0:
                respuesta=resta(int(input("numero : ")),0) 
            else:
                respuesta=resta(respuesta,int(input("numero : ")))
    if opcion ==3:
        for numero in range(contador):
            if numero==0:
                respuesta=multiplicacion(1,int(input("numero : ")))
            else:
                respuesta=multiplicacion(respuesta,int(input("numero : ")))
    if opcion ==4:
        for numero in range(contador):
            if numero==0:
                respuesta=division(int(input("numero : ")),1)
            else:
                respuesta=division(respuesta,int(input("numero : ")))
    print("las resultado es", respuesta)