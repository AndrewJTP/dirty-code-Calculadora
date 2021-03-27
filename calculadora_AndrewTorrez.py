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
    o = int(input("Ingrese su opcion: ")) 
    if o==5 :
        print("hasta luego...!!!")
        break
    c = int(input("cuantos numeros va a calcular? ") )    
    if o == 1:
        for v in range(c):
            if v==0:
                respuesta=suma(0,int(input("numero : ")))
            else:
                respuesta=suma(respuesta,int(input("numero : ")))
    if o ==2:
        for v in range(c):
            if v==0:
                respuesta=resta(int(input("numero : ")),0) 
            else:
                respuesta=resta(respuesta,int(input("numero : ")))
    if o ==3:
        for v in range(c):
            if v==0:
                respuesta=multiplicacion(1,int(input("numero : ")))
            else:
                respuesta=multiplicacion(respuesta,int(input("numero : ")))
    if o ==4:
        for v in range(c):
            if v==0:
                respuesta=division(int(input("numero : ")),1)
            else:
                respuesta=division(respuesta,int(input("numero : ")))
    print("las resultado es", respuesta)
    if  o !=1 and o !=2 and o !=3 and o !=4 and o !=5:
        print ("opcion invalida") 