#!/usr/bin/python
cadena =raw_input("ingrese frase:  ")
def inversa (cadena):
    invertida = ""
    cont = len(cadena)
    indice = -1
    while cont >= 1:
        invertida += cadena[indice]
        indice = indice + (-1)
        cont -= 1
    return invertida

inversa(cadena)
print inversa(cadena)
