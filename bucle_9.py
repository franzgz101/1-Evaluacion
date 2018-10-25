def bucle_9():
    print"*********************************"
    print"** EL CONSTRUCTOR DE PIRAMIDES **"
    print"*********************************"
    print"Indica, oh Faraón, de que altura deseas tu piramide. "
    altura=input("altura = ")
    for fil in range(1,altura+1):
        for col in range(1,altura+2-fil):
            print "*",
        print " "

bucle_9()

