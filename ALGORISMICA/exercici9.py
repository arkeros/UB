#Autor: Rafael Arquero Gimeno

import math
import random
import time
import collections

#agafa length bits comencant a contar per la dreta
# bitsplit(101001, 0, 3) = 001
def bitsplit(n, first, length):
    return (n >> first) & (2 ** length - 1)

def binlen(n):#longitud d'un enter representat en binari
    if n == 0:
        return 1
    return int(math.log(n) // math.log(2)) + 1

#distancia euclideana en un espai de d dimensions
def euclidean_distance(p, q):
    dimension = len(p)#dimensio de l'espai
    return math.sqrt(sum([(p[d] - q[d]) ** 2 for d in xrange(dimension)]))

def Gray2Int(n):
    length = binlen(n)
    shift = 1
    while shift < length:
        n ^= (n >> shift)
        shift *= 2
    return n

def Int2Gray(n):#nombre natural a codificacio binaria de gray en forma int   
    return (n >> 1) ^ n

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

#
# GENETICS
#

def mutate(gen, prob):
    length = binlen(gen)
    for i in xrange(length):
        if random.random() < prob:#ha de mutar 
            gen ^ (2 ** i)# ^ == XOR; 2 ** int genera un binary amb nomes un 1 , tot equival a negar la posicio i per la dreta
    return gen

def reproduce(male, female):
    babies = [0] * 2
    length  = max(binlen(male), binlen(female))#bits que considerarem

    male    = ('{0:0' + str(length) + 'b}').format(male)
    female  = ('{0:0' + str(length) + 'b}').format(female)

    for digit in xrange(length):#per cada gen del cromosoma, (bit)
        i = length - digit - 1 #posicio del bit en els pares
        if male[i] == female[i]:#si el bit es el mateix, cap problema, sel posem als dos el mateix tambe
            babies[0] += int(male[i])   * (2 ** digit)
            babies[1] += int(female[i]) * (2 ** digit)
        else:#els pares tenen el bit diferent: un te un 0 i l'altre un 1
            towhogoes = int(male[i]) ^ int(random.random() < 0.5)#a quin fill posem l'1??? 50% de probabilitats d'un o l'altre
            babies[towhogoes] += 2 ** digit            
    
    for baby in babies: 
        yield baby

def gen_uniques(genes, gen2dom):
    genes.sort(lambda a, b: cmp(a[0], b[0]))
    genes = tuple(genes)#tuple per optimitzar
    l = len(genes)
    uniques = [0] * l#per evitar appends!! creem la llista amb tamany maxim

    size = 1
    uniques[0] = genes[0]#trivial
    for i in xrange(1, l):
        if gen2dom(genes[i - 1][0]) != gen2dom(genes[i][0]):#diferent de l'anterior?
            uniques[size] = genes[i]#doncs afegim l'anterior
            size += 1
            
    return uniques[:size]    

def diversityselection(population, limit, bestprob, gen2dom):
    probs           = [0] * len(population)
    probs[0]        = bestprob
    for x in xrange(1, len(population)):
        probs[x] = bestprob * (1 - sum(probs[:x]))
    population.sort(lambda a, b: -1 * cmp(a[1], b[1]))
    survivors       = [0] * limit     
    survivors[0]    = population[0]#el millor individu pasa automaticament
    population      = population[1:]
    
    diversities     = map(lambda gen: [gen[0], 0], population)#inicialitza les diversitats a zero
    for i in xrange(1, limit):
        for key in xrange(len(diversities)):#calculem la diversitat de tota la poblacio respecte al que ja ha pasat
            distance = euclidean_distance(gen2dom(diversities[key][0]), gen2dom(survivors[i - 1][0]))
            if distance == 0:
                distance = 10 ** -8#epsilon, per evitar errors amb 0
            diversities[key][1] += distance ** -2    
        idiversities = diversities[:]
        idiversities.sort(lambda a, b: cmp(a[1], b[1]))
        #diversities[k] = (gen en gray, suma diversitats respecte ja seleccionats)
        #mirall de population, en comptes de guarar imatges, guarda diversitats

        orddiv = dict()
        k = 1
        for gen in idiversities:
            orddiv[gen[0]] = k
            k += 1
        
        ordboth = map(lambda k: (population[k][0], k + 1 + orddiv[population[k][0]]), xrange(0, len(population)))
        ordboth.sort(lambda a, b: cmp(a[1], b[1]))

        selected, j = None, 0
        while selected == None:
            if random.random() < probs[j]:#el seleccionem com a supervivent?
                selected = ordboth[j]
            j = (j + 1) % len(ordboth)

        #a quin individu correspon aquest genoma?
        popindex = 0
        while population[popindex][0] != selected[0]:
            popindex += 1

        survivors[i] = population[popindex]     
        del population[popindex]
        del diversities[popindex]
    return survivors[:limit]

def genetic_max(function, dom, step = 0.01, maxpop = 50, bestprob=2.0/3, mutprob=0.01):
    dimension = len(dom)#dimensio de la funcio (1 variable, 2 variables...)

    t0 = time.clock()
    
    genomebits = 1
    for d in xrange(dimension):
        genomebits *= (dom[d][1] - dom[d][0]) / step
    genomebits = binlen(genomebits) #constant que diu quants bits de llargada te el genoma
    genomebits = int(math.ceil(1.0 * genomebits / dimension) * dimension)#bits multiple de dimension

    #transforma el gen a un punt del domini
    gen2dom    = lambda n : tuple([round((1/step)*(dom[d][0] + (dom[d][1] - dom[d][0]) * Gray2Int( bitsplit(n, genomebits*d/dimension, genomebits/dimension) ) / (2.0 ** (genomebits / dimension)))) * step for d in xrange(dimension)])
    sample     = random.sample(xrange(2 ** genomebits), maxpop)#xrange es mes eficient que range per pasar-ho com a argument
    population = [(n, function(*gen2dom(n))) for n in sample]# (gen, imatge o adaptacio)
    population.sort(lambda a, b: -1 *cmp(a[1], b[1]))
    del(sample)

    #la probabilitat de seleccio no varia!
    selprobs            = [[0] for x in xrange(250)]    
    selprobs[0]         = bestprob
    for i in xrange(len(selprobs)):
        selprobs[i] = selprobs[0] * (1 - sum(selprobs[:i]))

    generation      = 0
    avaluations     = maxpop#contador de cops que avaluem la funcio, de moment ja ho em fet "maxpoblacio" cops
    historial       = []#guardarem el millor individu per observar quin es el progres de l'evolucio
    stopgeneration  = False
    while not stopgeneration:
        #[!] Atencio, population ja esta ordenat de millor a pitjor!
         
        #reproduccio
        parents = population[:]
        while len(parents) > 0:
            pair = [None, None]

            if len(parents) > 2:
                for j in xrange(2):
                    selected, i = None, 0
                    while selected == None:
                        if random.random() < selprobs[i]:#el seleccionem com a pare?
                            selected = parents[i]
                            del parents[i] 
                        i = (i + 1) % len(parents)
                    pair[j] = selected
            else:
                pair = parents[:]
                del parents[0]
                del parents[0]

            children = reproduce(pair[0][0], pair[1][0])
            for i in xrange(2):
                child = mutate(children.next(), mutprob)
                population.append((child, function(*gen2dom(child))))
                avaluations += 1
        #fi reproduccio
            
        #seleccio per diversitat
        population  = gen_uniques(population, gen2dom)#no vull individus repetits
        population  = diversityselection(population, maxpop, bestprob, gen2dom)
        population.sort(lambda a, b: -1 * cmp(a[1], b[1]))#ordenem per imatges
        #fi seleccio per diversitat
    
        generation    += 1
        elapsed        = time.clock() - t0
        historial.append(population[0])
        #print generation, 'f', gen2dom(population[0][0]), '=', population[0][1]   
        stopgeneration = elapsed > 9.5 or generation > 10 and historial[-1][0] == historial[-10][0]#si en 10 generacions no ha variat o ja han pasat 9 segons

    #ara en population tenim la poblacio guanyadora
    #esbrinem quants maxims retornarem
    selected = []#els maxims que retornarem
    image = population[0][1]
    k = 0
    while k < maxpop and image > population[0][1] * 0.99:#1% de tolerancia en la imatge
        ind = population[k]
        valid = True
        for sel in selected:
            distance = euclidean_distance(gen2dom(ind[0]), sel[0])
            if distance < max(1000 * step, 0.01):#si les x estan a prop d'un que ja hem escogit, fora!
                valid = False

        if valid:
            selected.append((gen2dom(ind[0]) , ind[1]))

        k += 1
        image = population[k%maxpop][1]
        
        
    return {"generations":generation,"max":selected,"avaluations":avaluations}

#
# UNA DIMENSIO
#

def func1d(x):
    return x * math.sin(10 * math.pi * x) + 1.0

def frange1d(start, end, step=1.0):
    x = start
    while x <= end:
        yield x
        x += step

def search1d():    
    t0 = time.clock()
    output = genetic_max(func1d, [[-1.0, 2.0]], 0.01, 30)
    tf = time.clock()
    elapsed = format_time(tf - t0) 
    print "La funcio {0} te {1} maxims al voltant del valor {2}. S'han dut a terme {3} avaluacions de la funcio en {4}. Es donen per als seguents valors:".format(
        "func1d",
        len(output['max']),
        output['max'][0][1],
        output['avaluations'],
        elapsed)
    print '{:>10}'.format('x')
    for maximum in output['max']:
        print '{:>10}'.format(*maximum[0])
    print ""
        
    t0 = time.clock()
    output = genetic_max(func1d, [[-1.0, 2.0]], 0.0001, 40)
    tf = time.clock()
    elapsed = format_time(tf - t0) 
    print "La funcio {0} te {1} maxims al voltant del valor {2}. S'han dut a terme {3} avaluacions de la funcio en {4}. Es donen per als seguents valors:".format(
        "func1d",
        len(output['max']),
        output['max'][0][1],
        output['avaluations'],
        elapsed)
    print '{:>10}'.format('x')
    for maximum in output['max']:
        print '{:>10}'.format(*maximum[0])
    print ""
        
    t0 = time.clock()
    output = genetic_max(func1d, [[-1.0, 2.0]], 0.000001, 60)
    tf = time.clock()
    elapsed = format_time(tf - t0) 
    print "La funcio {0} te {1} maxims al voltant del valor {2}. S'han dut a terme {3} avaluacions de la funcio en {4}. Es donen per als seguents valors:".format(
        "func1d",
        len(output['max']),
        output['max'][0][1],
        output['avaluations'],
        elapsed)
    print '{:>10} '.format('x')
    for maximum in output['max']:
        print '{:>10}'.format(*maximum[0])
    print ""
        
    t0 = time.clock()
    output = genetic_max(func1d, [[-1.0, 2.0]], 0.00000001, 100)
    tf = time.clock()
    elapsed = format_time(tf - t0) 
    print "La funcio {0} te {1} maxims al voltant del valor {2}. S'han dut a terme {3} avaluacions de la funcio en {4}. Es donen per als seguents valors:".format(
        "func1d",
        len(output['max']),
        output['max'][0][1],
        output['avaluations'],
        elapsed)
    print '{:>10} '.format('x')
    for maximum in output['max']:
        print '{:>10}'.format(*maximum[0])
    print ""

#
# DUES DIMENSIONS
#

def func2d(x, y):
    return 200.0 - (x ** 2 + y - 11.0) ** 2 - (x + y**2 -7) ** 2

def frange2d(start, end, step=1.0):    
    x = start    
    while x <= end:
        y = start
        while y <= end:
            yield x, y
            y += step
        x += step

def search2d():
    t0 = time.clock()
    output = genetic_max(func2d, [[-6.0, 6.0], [-6.0, 6.0]], 0.0005, 80, 0.5)
    tf = time.clock()
    elapsed = format_time(tf - t0) 
    print "La funcio {0} te {1} maxims al voltant del valor {2}. S'han dut a terme {3} avaluacions de la funcio en {4}. Es donen per als seguents valors:".format(
        "func2d", len(output['max']),
        output['max'][0][1],
        output['avaluations'],
        elapsed)
    print '{:>10} {:>10}'.format('x', 'y')
    for maximum in output['max']:
        print '{:>10} {:>10}'.format(*maximum[0])

#
# CRIDES
#

search1d()
search2d()
