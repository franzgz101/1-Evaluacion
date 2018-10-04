def condicional_2():
    nombre="Fran"
    respuesta=raw_input("¿Que hora es (1-24)" )
    if(int(respuesta) < 14):
        print "Buenos dias " + nombre
    if(int(respuesta) > 13 and 20 ):
        print "Buenas tardes " + nombre

condicional_2()
