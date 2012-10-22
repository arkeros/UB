#By: Rafa Arquero

from string import split, upper
from collections import Counter

def input_number(obj = 'nombre'):
    return input('Introdueix un ' + obj + ': ')

#aquesta funcio serveix per forcar a l'usuario a introduir entrades valides
def valid_input(obj = 'un nombre', vartype = int, validation = lambda x: True):
    valid = False

    while not valid:
        var = raw_input('Introdueix ' + obj + ': ')
        try:#probem de pasar de string 
            var = vartype(var)
            valid = validation(var)
        except ValueError:#no hem pogut fer el cast
            valid = False
            
        if not valid:
            print '[!] Siusplau introdueix una entrada valida.'    

    return var 

def nombres():
    numbers = []

    print "Aquest programa et demana 5 nombres i et retorna el mes proper al primer."

    for i in range(5):
        numbers.append(input_number())

    n = numbers[1]#quan comencem, com nomes hem mirat un nombre, es aquest el mes gran
    for i in range(2, 5):
        #el valor absolut a matematiques es defineix com la distancia
        if abs(numbers[i] - numbers[0]) < abs(n - numbers[0]):#si es millor que el millor que haviem trobat
            n = numbers[i]#aquest es el millor ara

    print 'El' , n, 'es el nombre mes proper al primer (', numbers[0], ').'

def consonant():
    VOWELS      = 'AEIOU'#"constant" amb les vocals
    CONSONANTS  = 'BCDFGHJKLMNPQRSTVWXYZ'#"constant" amb les consonants
    
    print "Blallblalbllallabla."

    phrase  = valid_input('una frase',      str, lambda x: len(x) > 0)
    c       = valid_input('una consonant',  str, lambda x: len(x) == 1 and x.upper() in 'BCDFGHJKLMNPQRSTVWXYZ')
    n       = valid_input('un natural',     int, lambda x: x >= 0)
    
    freq = Counter(phrase)#contem els caracters
    nvowels = 0
    for char in freq:
        if char.upper() in VOWELS:#si es una vocal
            nvowels += freq[char]

    i = 0
    while nvowels > n and i < len(phrase):
        if phrase[i].upper() in VOWELS:#si el caracter es una vocal
            phrase = phrase[:i] + c + phrase[i+1:]#el canviem per la consonant
            nvowels -= 1
        i += 1

    print phrase

def seq():
    print "Bablalblallbalblabl."
    
    n   = valid_input('un natural de 5 xifres o mes', int, lambda x: x >= 10000)
    ns  = str(n)

    seq = 0
    bestprod = 0#on es guarda el millor producte trobat
    for i in range(0, len(ns) - 5 + 1):
        subns = ns[i:5+i] #sequencia de 5 xifres de n comensant per la posicio i
        prod = 1#inicialtzem prod com a 1, el element neutre del producte
        
        for digit in subns:#per cada difit de subns
            prod *= int(digit)

        if prod > bestprod:#hem trobat una nova millor sequencia
            bestprod = prod#actualitzem el millor producte
            seq = int(subns)

    print seq
            
nombres()
consonant()
seq()
