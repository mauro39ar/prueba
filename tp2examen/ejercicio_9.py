#!/usr/bin/python

buffy = input("ingrese cantidad de pasajeros: ")

if buffy >0 and buffy <2:
    
    print "su vehiculo es una bicicleta"
elif buffy == 2 and buffy < 3:
    
    print "su vehiculo es una moto"

elif buffy == 3 or buffy < 6:
    
    print "su vehiculo es una auto"

elif buffy == 6 or buffy <= 12:

    print "su vehiculo es una camioneta"

elif buffy == 13 or buffy < 50:

    print    "su vehiculo es una colectivo"

elif buffy < 51 or buffy < 201:

    print "su vehiculo es una avion"

else:

    print "no tiene vehiculo"