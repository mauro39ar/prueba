#!/usr/bin/python

ranma = raw_input("ingrese sexo:  ")

saotome = input("ingrese estatura:  ")

if ranma == "femenino" and saotome <  145:
    print "petiza"

elif ranma == "femenino" and 145 < saotome < 170:

    print "normal"

elif ranma == "femenino" and saotome > 170:

    print "alta"

elif ranma == "masculino" and saotome < 160:

    print "petizo"

elif ranma == "masculino" and 160 < saotome < 170:
    
    print "normal"

elif  ranma == "masculino" and saotome > 190:
    
    print "alto"

else: 
    print "fin"
    