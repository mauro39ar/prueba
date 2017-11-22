#!/usr/bin/python

amy = input ("ingrese numero(del 1 al 7): ")

lita=["domingo", "lumnes", "martes", "miercoles", "jueves", "viernes", "sabado"]

if amy > 0 and amy <=7:

    print "el dia de la semana es %s" % (lita[amy-1])

else:

    print "el numero ingresado es incorrecto"