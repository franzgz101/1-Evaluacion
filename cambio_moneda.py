def cambio_moneda():
    euros=input("Introduce una cantidad:")
    respuesta=raw_input("¿Dolares o libras (d/l/z/k)?: ")
    if(respuesta=="d"):
        print "Son "+ str(euros*1.15)+ " dolares"
    if(respuesta=="l"):
        print "Son "+ str(euros*0.88)+ " libras"
    if(respuesta=="z"):
        print "Son "+ str(euros*4.31)+ " zlotys"
    if(respuesta=="k"):
        print "Son "+ str(euros*0.002)+ " karinas"

cambio_moneda()
