 #!/usr/bin/python   
lista=[1,2,3,4,5,]

def sum (lista):
    suma = 0
    for i in lista:
        suma += i
    return suma
       
   
def multipli (lista):
    multiplicacion = 1
    for i in lista:
        multiplicacion *= i
    return multiplicacion
sum(lista)
multipli(lista)

print sum(lista)
print multipli(lista)