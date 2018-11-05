def bucle_10():
    nfinal=input("¿Hasta que numero quieres sumar:?")
    numero_pares=0
    numero_impares=0
    for numero in range(1,nfinal+1):
        if(numero%2==0):
            print str(numero), "es par"
            numero_pares=numero_pares+1
        else:
            print str(numero),"es impar"
            numero_impares=numero_impares+1
    print "He contado ",numero_pares, "numeros pares"
    print "He contado ",numero_impares, "numeros impares"
    
bucle_10()
