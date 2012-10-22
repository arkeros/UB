#By: Rafael Arquero Gimeno
# 5 / X / 2012

import string

#funcions per estalviar codi
def input_frase(obj = 'frase'):
    return raw_input("Introdueix una " + obj + ": ")

def cesar_cifrar(frase, clau):
    alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    first = 0
    cesar = ''

    for char in frase:#per cada lletra de la frase
        if alfabet.find(str.upper(char)) == -1:#si es un caracter que no perrtany al alfabet
            cesar += char#afegir tal cual
        else:#es una lletra del alfabet
            n = alfabet.find(str.upper(char)) + clau #posicio al alfabet del caracter
            if char.isupper():
                first = ord('A')
            else:
                first = ord('a')
            cesar += chr(first + (n % len(alfabet))) #%es per que sigui el mateix demanar la n + 2 lletra que la 2

    return cesar

def find_in_file(target, filename, sensitive = True):#ultim param defineix si hi ha diferencia entre majuscules i minuscules
    file = open(filename, 'r')
    txt = file.read()
    l = len(target) #calculo nomes un cop la longitud de la paraula a cercar

    if not sensitive:#si NO distingueix entre minuscules i majuscules
        txt = str.upper(txt)
        target = str.upper(target)        

    times = 0 #cops que l'hem trobat
    i = 0
    for char in txt:
        if char == target[0]:#si trobem el primer caracter, crec que es mes eficient que no comprobar-ho abans
            if txt[i:i + l] == target:
                times += 1
            
        i += 1 #itera la posicio del caracter al text
        
    return times






#aquesta fruncio dona l'acronim d'una frase
def acro():
    acro = ''
    frase = input_frase() 
    words = string.split(frase, ' ')
    for word in words:
        acro = acro + word[:1]

    acro = str.upper(acro) #a majuscules
    print "L'acronim de <"+ frase+ "> es:", acro
    return acro

def paraules():
    frase = input_frase()
    n = 0
    words = string.split(frase, ' ')
    #n = len(words)#manera mes curta
    for word in words:#aquest for es per que no dongui problemes amb mes d'un espai en blanc
        if word is not '':
            n += 1
    print n
    return n

def cesar():
    frase = input_frase()
    clau  = input('Introdueix una clau n (enter): ')
    
    cesar = cesar_cifrar(frase, clau)
    
    print cesar
    return cesar

def lyrics():
    file = open('lletra.txt', 'r')
    text = file.readlines()
    file.close()

    lletra_cesar = ''
    i = 1#var que conta les lines

    for line in text:
        lletra_cesar += str(i) + "\t" + line
        i += 1
        

    file = open('lletra_cesar.txt', 'w')
    lletra_cesar = cesar_cifrar(lletra_cesar, 5)        

    file.write(lletra_cesar)
    file.close()

    return 'lletra_cesar.txt creat!'

def sequencia():
    filename = 'lletra.txt'    
    vegades = find_in_file('th', filename, False)
    #he asumit que no cal distingir entre majuscules i minuscules
    #si cal fer-ho, cambieu el tercer arguemtn per True

    print '"th" apareix a ', filename, vegades, 'vegades.' 
    return vegades

def paraula():
    filename = 'lletra.txt' 
    word = input_frase('paraula')

    vegades = find_in_file(word, filename, False)
    #he asumit que no cal distingir entre majuscules i minuscules
    #si cal fer-ho, cambieu el tercer arguemtn per True
    
    print '"' + word + '" apareix a ', filename, vegades, 'vegades.'
    return vegades

acro()
paraules()
cesar()
lyrics()
sequencia()            
paraula()
