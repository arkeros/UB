# By: Rafa Arquero Gimeno

#aclaracio: com queen el pdf es demanava emprar coleccions, he entes que es tenia que utilitzar
#prioritariament el modul collections.

from collections import deque#per dni()
from collections import defaultdict#per otan()
from random import shuffle #per llista()
from math import floor

def input_number(obj = 'nombre'):
    return input('Introdueix un ' + obj + ': ')

def input_string(obj = 'paraula'):
    return raw_input('Introdueix una ' + obj + ':')

def sumatori(start, end, step):
    res = 0
    
    i = start
    while i <= end:
        res += i
        i += step

    return res

def mentre():
    n = input_number()
    print 'La suma dels primers', n , 'nombres sencers es:', sumatori(1, n, 1)
    print ''

    n = input_number()
    print 'La suma dels primers', n , 'nombres senars es:', sumatori(1, 2*n - 1, 2)
    print ''

    numbers = []
    #condicio del while certa a l'inici 
    #i despres tambe sempre que l'ultim element (-1) no sigui 999
    while numbers == [] or not numbers[-1] == 999:
        n = input_number()
        numbers.append(n)

    #l'ultium  nombre sera el 999, el treiem
    numbers.pop()

    suma = 0
    i = 0
    while i < len(numbers):
        suma += numbers[i]
        i += 1

    print 'La suma de', numbers, 'es:', suma
    print ''

    n = input_number()
    m = n
    times = 0

    while (m % 2 == 0 and m > 1):
        times   += 1
        m /= 2

    print n, 'es divisible entre 2 (amb divisio sencera)', times , 'cops.'

def inversio():
    interes = input("Introdueix l'interes de la inversio en forma de percentatge (%): ")
    interes = float(interes)#per evitar problemes relacionats amb la divisio de ints
    interes /= 100

    year = 0
    capital = 1.0
    while capital < 2:
        capital = capital * (1 + interes)
        year += 1

    interes *= 100

    print "Amb un interes del", interes ,"%, l'inversio trigara", year, "anys en doblarse."

def nota():
    criteri = {0:"Suspens",5:"Aprovat",7:"Notable",9:"Excelent",10:"Matricula"}

    valid = False

    while not valid:
        nota = input('Introdueix una nota entre 0 i 10: ')
        valid = isinstance(nota, (int, long, float)) and nota >= 0 and nota <= 10 
        #ha de ser un real entre 0 i 10 (ambdos inclosos)
        if not valid:
            print 'La nota introduia no es valida, siusplau introdueix un altre.'

    #ho he trobat mes curt i mes dinamic (general) que fer-ho amb ifs
    criteri[4] = criteri[3] = criteri[2] = criteri[1] = criteri[0]
    criteri[6] = criteri[5]
    criteri[8] = criteri[7]   

    print 'Un', nota, 'equival a', criteri[floor(nota)], '.'    
   

def dni():
    #he utilitzar un deque, en comptes d'un string, perque segons l'enunciat he entes que calia utilitzar una coleccio
    chars = deque('TRWAGMYFPDXBNJZSQVHLCKE')
    valid = False

    while not valid:
        dni = input_number('DNI')
        valid = isinstance(dni, (int, long)) and dni < 10**8 and dni > 0
        #ha de ser un enter major que 0 i de 7 xifres o menys (el mateix que menor a 10^8)
        if not valid:
            print 'El dni introduit no es correcte, siusplau introdueix un altre.'

    char = chars[dni % 23]

    print 'La lletra que correspon al dni', dni, 'es', char, '.'

def llista():
    words = deque()
    
    print 'Introdueix una serie de paraules. Per acabar has de premer ENTER dos cops.'

    while len(words) == 0 or words[-1] is not "":
        word = input_string()
        words.append(word)
    words.pop()   

    shuffle(words)
    print words

def otan():    
    alphabet = {"alpha","bravo","charlie","delta","echo","foxtrot","golf","hotel","india",\
                "julit","kilo","lima","mike","november","oscar","papa","quebec","romeo",\
                "sierra","tango","uniform","victor","whiskey","xray","yankee","zulu"}

    tmp = defaultdict(lambda : '')
    #si el carecter no esta en l'alfabet de la otan,
    #mostrar un caracter buit ('')  per defecte

    for word in alphabet:
        tmp[word[:1].lower()] = word.capitalize()

    alphabet = tmp
        
    word = input_string()

    otan = ''

    for char in word:
        otan += alphabet[char.lower()] + ' '

    print otan
    
mentre()
inversio()
nota()
dni()
llista()
otan()
