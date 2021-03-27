#Andrew Torrez P
#refactorizando
while True:
    o = 0
    print("""
    ******** caluladora  ***********
    1.- Sumar numeros
    2.- Restar números
    3.- Multiplicar números
    4.- dividar
    5.- salir
    """)
    o = int(input("Ingrese su opcion: ") )     

    if o == 1:
        c = int(input("cuantos numeros va a sumar? ") ) 
        s=0
        for v in range(c):
            if v==0:
                s=s+int(input("numero : ") ) 
            else:
                print("resultado parcial: ",s)
                s=s+int(input("mas : ") ) 
        print("las suma total es",s)
    if o ==2:
        c = int(input("cuantos numeros va a restar? ") ) 
        r=0
        for v in range(c):
            if v==0:
                r=int(input("numero : ") ) 
            else:
                print("resultado parcial: ",r)
                r=r-int(input("menos : ") )
        print("las resta total es",r)
    if o ==3:
        c = int(input("cuantos numeros va a multiplicar? ") ) 
        m=1
        for v in range(c):
            if v==0:
                m=m*int(input("numero : ") ) 
            else:
                print("resultado parcial: ",m)
                m=m*int(input("por : ") )
        print("el resultado total es",m)
    if o ==4:
        c = int(input("cuantos numeros va a dicidir? ") ) 
        d=1
        for v in range(c):
            if v==0:
                d=int(input("numero : ") ) 
            else:
                print("resultado parcial: ",d)
                d=d/int(input("dividido entre : ") )
        print("el resultado total es",d)
    if o==5 :
        print("hasta luego...!!!")
        break
    if  o !=1 and o !=2 and o !=3 and o !=4 and o !=5:
        print ("opcion invalida") 