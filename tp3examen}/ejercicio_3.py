#!/usr/bin/python

saori = "Soy el mas jodido del maldito universo "

def longitud(saori):

    total = 0

    for i in saori:

        total = total + 1

    return total

longitud(saori)

print('La longitud es %s ' %(longitud(saori)))