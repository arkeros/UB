# By: Rafael Arquero Gimeno, 30/IX/2012

import math
import cmath

def futval():
    print "Aquest programa calcula el valor futur d'una determinada inversio a 10 anys."
    principal = input("Entra la inversio inicial: ")
    apr = input("Entra l'interes anual: ")
    years = input("Entra els anys que durara l'inversio: ")
    principal *= (1 + apr) ** years#formula de l'interes compost
    print "La quantitat al cap de", years, "anys es:", principal

def convert():
    for celsius in range(0, 100 + 1, 10):#comencant en el 0, fins a 101 elements de 10 en 10
        fahrenheit = 9.0 / 5.0 * celsius + 32
        print celsius, "graus C \t= ", fahrenheit , 'graus Fahrenheit.'#\t es el tabulador

def exp():
    a = 4.0 / 10.0 + 3.5 * 2
    b = 10 % 4 + 6 / 2
    c = abs(4 - 20 / 3) ** 3
    d = cmath.sqrt(4.5 - 5.0) + 7 * 3
    e = 3 * 10 / 3 + 10 % 3
    f = 3L ** 3

    print a
    print b
    print c
    print d
    print e
    print f

def punts():
    print 'Aquesta funcio calcula el pendent de la recta que pasa per dos punts.'
    x1, y1 = input('Escriu el primer punt de la forma x1, y1:')
    x2, y2 = input('Escriu el segon punt de la forma x2, y2:')

    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)
    
    m = (y2 - y1) / (x2 - x1)
    print 'El pendent m de la recta es :', m

def calceuclid(a, b):#funcio 
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)    

def euclid():
    print 'Aquesta funcio calcula la distancia euclidiana entre dos punts.'
    x1, y1 = input('Escriu el primer punt de la forma x1, y1:')
    x2, y2 = input('Escriu el segon punt de la forma x2, y2:')

    euclid = calceuclid([x1, y1], [x2, y2])
    print 'La distancia euclidiana es:', euclid

def euclid2():
    print 'Aquesta funcio calcula la distancia euclidiana SENCERA entre dos punts.'
    x1, y1 = input('Escriu el primer punt de la forma x1, y1:')
    x2, y2 = input('Escriu el segon punt de la forma x2, y2:')

    euclid = calceuclid([x1, y1], [x2, y2])
    euclid = round(euclid)
    print 'La distancia euclidiana SENCERA es:', euclid

def factmenor():
    suprem = 6204484017332394393600000#maxim
    i = 0#primer nombre natural
    continuar = True#per defecte continuarem 

    while continuar:
        fact = math.factorial(i)        
        if(fact < suprem):
            print fact
        else:
            continuar = False
        i += 1

def suma():
    suprem = 1000#umbral
    suma = 0#per defecte la suma es 0

    for i in range(suprem):
        #mateix que if i % 15 == 0: ...
        if i % 3 == 0 and i % 5 == 0:
            suma += i#sumem...

    print suma

def divisible():
    factors = [2, 3, 4, 5, 6, 7, 8, 9, 10]#mes comode definir una llista amb els factors
    i = 0
    found = False

    while not found:
        i += 1
        found = True
        #es mes facil comprobar que hi ha alguna condico que no es compleix
        #que comporbar que 'es compleixen totes
        for factor in factors: #per cada factor de factos que hem definit
            if(i % factor != 0):#hem trobat un
                found = False    # i ja no compleix la condicio

    #aqui s'ha trencat el bucle while, per tant, i es la solucio

    print i

futval()
convert()
exp()
punts()
euclid()
euclid2()
factmenor()
suma()
divisible()
