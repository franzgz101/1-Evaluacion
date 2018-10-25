def bucle_7():
    print"*********************************"
    print"** EL CONSTRUCTOR DE PIRAMIDES **"
    print"*********************************"
    print"Indica, oh Faraón, de que altura deseas tu piramide. "
    altura=input("altura = ")
    for fill in range(1,altura+1):
        for i in range(1,altura+1):
            print "*",
        print " "

bucle_7()
