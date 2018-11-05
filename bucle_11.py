def bucle_11():
    nfinal=input("¿Hasta que numero quieres sumar:?")
    suma_pares=0
    suma_impares=0
    for numero in range(1,nfinal+1):
        if(numero%2==0):
            print str(numero), "es par"
            suma_pares=suma_pares+numero
        else:
            print str(numero),"es impar"
            suma_impares=suma_impares+numero
    print "La suma de los numeros pares vale",suma_pares
    print "La suma de los numeros impares vale", suma_impares
    
bucle_11()
