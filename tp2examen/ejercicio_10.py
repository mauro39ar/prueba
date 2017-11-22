#!/usr/bin/python

xin = input("ingrese edad: ")

if xin >0 and xin < 2:

    print "la persona es bebe"

elif xin ==2 or xin < 12:

    print "la persona es un ninio"

elif xin == 12 or xin < 18:

    print "la persona es adolescente"

elif xin == 18 or xin <= 45:
    
    print "la persona es adulto"

elif xin == 45 or xin <= 60:

    print "la persona es veterano"

elif xin == 60 or xin < 200:

    print "la persona es abuelo"

else:

    print "sos un dios"