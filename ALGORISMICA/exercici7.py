#By: Rafael Arquero Gimeno

from math import floor, ceil
from random import sample
import time

#funcio d'ordenacio auxiliar
def quicksort(numbers):
    if len(numbers) <= 1:
        return numbers
    
    numbers = tuple(numbers)#optimitzacio
    pivot = numbers[0]
    subnumbers = [[] for x in range (2)]#zero mes petits, 1 mes grans
    for n in numbers[1:]:
        subnumbers[int(n > pivot)].append(n)

    return quicksort(subnumbers[0]) + [pivot] + quicksort(subnumbers[1])   

def negatius(numbers):
    #[!] per definicio 0 no es ni positiu ni negatiu, el poso al mitj
    numbers = tuple(numbers)
    groups = [[] for x in range (3)]#0 negatius, 1 zeros i 2 positius

    for n in numbers:
        groups[int(n == 0) + 2 * int(n > 0)].append(n)

    return groups[0] + groups[1] + groups[2]

def exponent(base, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:     
        return exponent(base, floor(exp/2.0)) * exponent(base, ceil(exp/2.0))

def reverse(string):
    l = len(string)
    if(l <= 1):
        return string    
    pivot = l // 2 #len / 2, sense decimals
    return reverse(string[pivot:]) +  reverse(string[:pivot])

#complexitat O(n * log(n))
#segons Teorema de master: T(n)=aT(n/b)+O(n^d)
#a = 2;b = 2;d = 1; (d = log a) => O(n log(n))
def aprop(numbers, ordered=False):
    if not ordered:#primera iteracio
        numbers = quicksort(numbers)

    l = len(numbers)
    if l <= 2:
        return numbers

    lpair = aprop(numbers[:int(ceil(l / 2)) + 1], True)#+1 per asegurar element en comu
    rpair = aprop(numbers[int(floor(l / 2)):], True)

    ldist, rdist = abs(lpair[0] - lpair[1]), abs(rpair[0] - rpair[1])

    if rdist < ldist:
        return rpair
    else:
        return lpair

def elimina(numbers):
    numbers = tuple(quicksort(numbers))#n log n, tuple per optimitzar
    l = len(numbers)
    uniques = [0] * l#per evitar appends!! creem la llista amb tamany maxim

    size = 1
    uniques[0] = numbers[0]#trivial
    #cost O(n)
    for i in range(1, l):
        if numbers[i - 1] != numbers[i]:#diferent de l'anterior?
            uniques[size] = numbers[i]#doncs afegim l'anterior
            size += 1            

    return uniques[:size]

'''a = []
for i in range(10):#per poder tenir repetits
    a += sample(range(-1000000, 1000000), 10)'''
a = [-9,8,0,1,3,-23,4,9,-4]

print negatius(a)

print exponent(2, 9)

print reverse("Hola, com estas?")

print aprop(a)

print elimina(a)
