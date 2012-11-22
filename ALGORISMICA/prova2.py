#By: Rafael Arquero Gimeno

def BoyerMooreHorspool(needle, haystack):
    m = len(needle)
    n = len(haystack)
    if m > n:
        return -1    
    skip = [m] * 256#petita optimitzacio
    for k in range(m - 1):
        skip[ord(needle[k])] = m - k - 1
    skip = tuple(skip)
    k = m -1
    while k < n:
        j = m - 1
        i = k
        while j >= 0 and haystack[i] == needle[j]:
            j -= 1
            i -= 1
        if j == -1:
            return i + 1
        k += skip[ord(haystack[k])]
    return -1        

def open_file(filename):
    words = [''] * 1000#llista que returnarem despres
    
    wordsfile = open(filename, 'r')#obirm l'arziu mode lectura
    wordslines = wordsfile.readlines()#llegim les linies
    wordsfile.close()#tancem arxiu

    for line in range(1000):
        words[line] = wordslines[line][:-1]#-1 per treure \n

    print words[:10]
    return words

def search_subword(vocabulary):
    for word in vocabulary:#aquesta es l'agulla
        matches = []#on guardem el casso d'exit, es a dir, les paraules que contenen l'agulla        

        for pairword in vocabulary:#i aquest el pallar
            if word != pairword and BoyerMooreHorspool(word, pairword) != -1:
                #evidentment, no volem saber si esta disn de ella mateixa
                #esta a algun lloc l'agulla, o sigui, no dona -1
                matches.append(pairword)

        if(len(matches) > 0):#hi ha ocurrencies
            print '-' * 50
            print 'The word <' + word + '> is contained in the following words:'
            print matches        

def mult3(n):
    if n == 0:#aquest cas para la recursio
        return 0
    return 3 + mult3(n -1)

def print_header(title):#funcio per 'decorar' , donar un output mes 'net'
    width = 80
    spacer = '#'

    print
    print
    print spacer * width
    print spacer * width
    
    line = spacer * width
    line = line[:(80 - len(title)) // 2] + title + line
    print line[:80]#[:80] per evitar problemes amb titols de longitud senar...
    
    print spacer * width    
    print spacer * width
    print
    print

#crides a funcions...
print_header('open_file()')
vocabulary = open_file('10.000_deutsche_Worter.txt')

print_header('search_subword()')
search_subword(vocabulary)

print_header('mult3()')
print(mult3(15))
print(mult3(17))

