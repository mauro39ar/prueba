#!/*usr/bin/python

sakura = input ("ingrese longitud 1:  ")

card = input ("ingrese longitud 2:  ")

captor = input ("ingrese longitud 3:  ")

if (sakura < card + captor and card < sakura +captor and captor < sakura + card): 

    print "se transforma en un triangulo"

else:

    print "no se transforma en triangulo"