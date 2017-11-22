#!/usr/bin/python

leia = raw_input("ingrese palaba para verificar si es polindromo:  ")
def palindromo(leia):

    if leia == leia[::-1]:

        return True

    else:

        return False

palindromo(leia)

print palindromo(leia)
