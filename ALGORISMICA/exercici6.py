#By: Rafa Arquero Gimeno

import time
import collections

#[reutilitzacio de codi]aquesta funcio l'he aprofitat d'una practica anterior meva
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

def levenshtein(haystack, needle):#pajar, agulla
    cols, rows = len(haystack) + 1, len(needle) + 1#calculem quantes columnes i files hi han. Tambe contem les nules-trivials
    E = [[0] * cols for x in range(rows)]#inicialitzem la matriu de les distancies

    for i in range(rows):#valors trivials de la primera columna
        E[i][0] = i

    for row in range(1, rows):
        for col in range (1, cols):
            E[row][col] = min(E[row][col-1] + 1, E[row-1][col] + 1, E[row-1][col-1] + int(needle[row - 1] != haystack[col - 1])) #aqui hi ha un petit truc, convertir un boolea en un enter, 0 o 1 y sumar

    return E

def dna():
    needles = ['AGATACATTAGACAATAGAGATGTGGTC', 'GTCAGTCTGGCCTTGCCATTGGTGCCACCA', 'TACCGAGAAGCTGGATTACAGCATGTACCATCAT']#patrons a buscar

    file = open('HUMAN-DNA.txt', 'r+')
    genome = file.readlines()#llegim l'arxiu i el guardem les linies en una llista

    for needle in needles:#per cada agulla a trovar
        t0          = time.clock()
        
        mincost     = len(needle)#el pitjor cost posible es on s'hagin de canviar totes les lletres
        bestmatch   = ''#millor substring trovat
        beststart   = 0#posicio on comença la substring a la linia
        bestend     = 0#posicio on acaba la substring a la linia
        bestline    = 0#linia de l'arxiu on hem trobat el substr mes semblant a l'agulla
        
        nline       = 1#la primera linia es 1, no pas 0
        
        for line in genome:
            distance    = levenshtein(line, needle)
            linemincost = min(distance[-1][:])#menor cost d'aquesta linia del genoma
            
            if linemincost < mincost:#hem trovat un nou millor substring!!!
                lastrow     = distance[-1][:]

                #actualitzem millors valors....
                mincost     = linemincost
                bestline    = nline                
                bestend     = lastrow.index(min(lastrow))#volem la posicio del valor minim de l'ultima fila

                col = bestend#columna 
                row = len(needle)#comencem al final (ultima fila)

                #nomes aturem quan hem arribat a la primera fila
                while row != 1:
                    #mirem quinna casella te el valor minim, d'entre la oest, nord i nord-oest.
                    #cal tenir en compte en la casella nord si coincideixen els caracters de l'agulla i el pallar
                    backtrack = min(distance[row][col-1], distance[row-1][col-1], distance[row-1][col] - int(needle[row - 1] != line[col - 1]))

                    #sabem quin es el valor minim, mirem on esta (row i col)
                    if backtrack == distance[row][col-1]:
                        col -= 1
                    elif backtrack == distance[row-1][col-1]:
                        row, col = row - 1, col - 1
                    else:
                        row -= 1

                beststart   = col                           #columna on comença la paraula
                bestmatch   = line[beststart - 1:bestend]   #substring del pajar que s'asembla mes a l'agulla (patro)

                if mincost == 0:#si la substring es identica... 
                    break#parem ja el bucle for, es imposible millorar-ho, aixi ens estalviem malbaratar temps de calcul.

            nline += 1
            
        tf = time.clock()
        
        print 'El patro ' + needle + ' es troba a la linia ' + str(bestline) + ', posicio ' + str(beststart) + ', del cromosoma 2 huma, i la seva distancia d\'edicio es ' + str(mincost) + '.'
        print 'El substring del cromosoma huma mes semblant es ' + bestmatch + '.'
        print 'El temps de calcul ha estat ' + format_time(tf - t0) + '.'

dna()
