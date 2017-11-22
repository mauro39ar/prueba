#!/usr/bin/python

saori= raw_input("ingrese caracter: ")

def caracter(saori):

	if ((saori == "a") or (saori == "e") or (saori == "i") or (saori == "o") or (saori == "u")):

		return True

	else:
		return "false"

caracter (saori)
print (caracter(saori))