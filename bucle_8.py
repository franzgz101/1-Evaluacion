def bucle_8():
    print"*********************************"
    print"** EL CONSTRUCTOR DE PIRAMIDES **"
    print"*********************************"
    print"Indica, oh Fara�n, de que altura deseas tu piramide. "
    altura=input("altura = ")
    for fil in range(1,altura+1):
        for col in range(1,fil+1):
            print "*",
        print " "

bucle_8()
