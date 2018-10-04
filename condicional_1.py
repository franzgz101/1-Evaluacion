def condicional_1():
    nombre=raw_input("Dime tu nombre")
    respuesta=raw_input(nombre + " ¿Vienes o te vas?")
    if(respuesta == "voy" or respuesta == "vengo"):
        print "Hola "+ nombre
    else:
        print "Adios "+ nombre

condicional_1()
