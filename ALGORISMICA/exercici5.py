#By: Rafa Arquero Gimeno

import time
import math
import collections

def input_number(obj = 'nombre'):
    return input('Introdueix un ' + obj + ': ')

def format_time(time):#time en segons, perque es unitat del sistema internacional...
    units = collections.OrderedDict({604800000:'w',86400000:'d',3600000:'h',60000:'m',1000:'s',1:'ms'})#definim les unitats, com a key el seu valor en ms
    units = collections.OrderedDict(sorted(units.items(), key=lambda t: -t[0]))#ordenar per clau de mes gran a mes petita    
    output = ''    

    time = time * 1000#a milisegons
    
    for key in units:#per cada unitat
        n = time//key
        if n >= 1:#si hi ha unitar, 
            output += str(int(n)) + units[key] + ' '#afegim el valor de la unitat + l'unitat a la sortida
        time %= key#el seguent valor a tractar, es el que encara no esta representat

    if output == '':#en el remot cas en que encara no tinguesim sortida
        output = str(time) + units[1]#donem la sortida com a ms

    return output

def benchmark():
    t0 = time.clock()

    for i in range(1, 3000):
        math.factorial(i)

    tf = time.clock()

    return tf - t0

#L'enunciat demanava l'algorisme recursiu, que es aquest
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n-2)

#a continuacio comento un de complexitat logaritmica per si es podia utilitzar un altre mes eficient
#def fibonacci(n):
#http://es.wikipedia.org/wiki/Sucesi%C3%B3n_de_Fibonacci#Algref_3
#    if n <= 0:
#        return 0
#
#    i = n - 1
#    a, b = 1, 0
#    c, d = 0, 1
#
#    while i > 0:
#        if i%2 == 1:#i es impar
#            a, b = d*b + c*a, d*(b+a) + c*b
#        c, d = c**2 + d**2, d* (2*c + d)
#        i = i/2
#
#    return a+b 

def mcd_euclides(n, m):
    while m is not 0:
        n, m = m, n%m

    return n

def gen_primes(suprem):
    numbers = dict.fromkeys(range(2, suprem+1, 1), True)
    #crea el diccionari de nombres, per defecte, tots son primers
    primes = []

    lastprime = 2#ultim nombre primer trobat

    while lastprime < math.sqrt(suprem):
        for i in range(lastprime * 2, suprem + 1, lastprime):#multiples de lastprime
            numbers[i] = False#el tatxem

        i = lastprime + 1
        lastprime = 0
        while lastprime == 0 and i < suprem:
            if numbers[i]:#si no esta tatxat
                lastprime = i
            i += 1            

    for i in range(2, suprem+1, 1):
        if numbers[i]:#si es primer
            primes.append(i)#l'afegim a la seva llista

    return primes

def isprime(n):#retorna true si es primer, false si no ho es
    i = 2
    
    while i <= math.sqrt(n):
        if n % i == 0:#Si es divisible
            print i
            return False#llavors no es primer, esa dir, es compost
        i += 1            

    return True #si no hem trobat cap divisor, es primer

def isprimefermat(n):
    #http://es.wikipedia.org/wiki/Peque%C3%B1o_teorema_de_Fermat
    tests = [2, 3, 5]#a's a provar

    for a in tests:
        if a ** (n - 1) % n != 1:#si no compleix el teorema
            return False#no es primer

    #si ha pasat tots els tests
    return True#Es primer
    

#Funcions d'interaccio amb l'usuari

def fib1():
    print 'Aquest programa calcula el terme n-esim de la successio de Fibonacci.'
    n = input_number()

    t0 = time.clock()
    f = fibonacci(n)
    tf = time.clock()

    print 'El terme', n , 'de la successio de Fibonacci es', f, '.'
    print 'Ha trigat', format_time(tf - t0), '.'

def mcd():
    print "Aquest programa calcula el M.C.D. de dos nombres enters emprant l'algorisme d'Euclides."

    a, b = input_number(), input_number()
    mcd = mcd_euclides(a, b)

    print 'El M.C.D. de', a, 'i', b, 'es', mcd, '.'

def era1():
    print "Aquest programa imprimeix per pantalla tots els nombres primers menors o iguals que un nombre introduit per l'usuari."
    n = input_number()
    primes = gen_primes(n)
    print primes

def era2():
    n = 1000000
    print "Aquest programa imprimeix per pantalla tots els nombres primers menors que", n , ", quants hi han i quan triga."

    t0      = time.clock()
    primes  = gen_primes(n)
    tf      = time.clock()

    print primes
    print "Hi han", len(primes), "nombres primers." 
    print "Ha trigat", format_time(tf - t0), "."

def factorp():
    print "Aquest programa determina si un nombre donat per l'usuari es primer o compost, mitjancant la tecnica de la factoritzacio i calcula quan triga."
    n = input_number()

    t0      = time.clock()
    tmp     = isprime(n)
    tf      = time.clock()

    print "El", n , "es un nombre",
    if tmp:
        print "primer."
    else:
        print "compost."
    print "Ha trigat", format_time(tf - t0), "."

def fermatp():
    print "Aquest programa comprova si un nomre es primer mitjancant el teorema petit de Fermat i quan triga a fer-ho."

    n = input_number()

    t0      = time.clock()
    caca    = isprimefermat(n)
    tf      = time.clock()

    print "El", n , "es un nombre",
    if caca:
        print "primer."
    else:
        print "compost."
    print "Ha trigat", format_time(tf - t0), "."
        
fib1()
mcd()
era1()
era2()
factorp()
fermatp()
