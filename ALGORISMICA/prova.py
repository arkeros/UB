#By: Rafael Arquero Gimeno

from math import cos, pi
#cos el necesitem per calcular el cosinus
#pi el necexistem per pasar de graus a radians

def phrase2numbers(phrase):
    NUMBERS     = '0123456789'  #"constant" amb els caracters numerics
    numeric     = ''            #string on guardarem els nombres que trobem a phrase
    nonumeric   = ''            #strign on guardem els no-nombres

    for char in phrase:
        if char in NUMBERS:     #si el caracter es un nombre
            numeric += char
        else:                   #si no es un nombre
            nonumeric += char

    numeric = int(numeric)      #la string numerica a nombre ENTER

    print nonumeric
    print numeric

    return numeric

def compute_cos(degrees):
    rad = pi * degrees / 180    #formula per pasar de graus a radians
    cosinus = cos(rad)          #calculem el cosinus
    print rad                   #imprimim l'angle en radians
    return cosinus

def write_angle(towrite):
    file = open('cos_numbers_rad.txt', 'w')#obrim l'arxiu, si no existeix, el creem
    
    file.write(str(towrite))    #el que escribim ha de ser una string

phrase          = 'angulo45grados'
numbers         = phrase2numbers(phrase)
cos_numbers_rad = compute_cos(numbers)
write_angle(cos_numbers_rad)   
