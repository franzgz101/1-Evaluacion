def bucle_4():
    for i in range(1,101):
        if (i%2==0):
            print str(i)+ " es par",
        else:
            print str(i)+ " es impar",
        if (i%3==0):
            print "y es divisible para 3"
        print "\n"
        
bucle_4()
