##1Diferencia entre variable contadora,acumuladora e interruptora
## 2Corregir el codigo
## 3Descomponer en producto de factores
##4Lee tres lados y di si el triángulo es rectángula

##1La variable acumuladora es aquella que va sumando números (Acumulándolas)
##1La contadora es aquella que cuenta el numero de elementos que tu le marcas
##1La variable interruptora es aquella que devulve dos valores true and false


##a)
##def hago.algo():
##x=input("Dime un numero):
##y=0
##for cont in range(0,10,1):
##y=y+cont
##print("y")
##b)añade lo necesario para repettir o salir

def hago_algo():
    y=0
    for cont in range(0,10,1):
        y=y+cont
        print y
hago_algo()        
    
##x ejemp cambialo para que x sea el numero limte del bucle
def hago_algo():
    x=input("dime un numero")
    y=0
    for cont in range(0,x,1):
        y=y+cont
        print y
hago_algo()        
    
