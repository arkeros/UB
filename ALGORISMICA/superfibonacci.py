#http://es.wikipedia.org/wiki/Sucesi%C3%B3n_de_Fibonacci#Algref_3
import time

def fib(n):
    if n <= 0:
        return 0

    i = n - 1
    a, b = 1, 0
    c, d = 0, 1

    while i > 0:
        if i%2 == 1:#i es impar
            a, b = d*b + c*a, d*(b+a) + c*b
        c, d = c**2 + d**2, d* (2*c + d)
        i = i/2

    return a+b 

t0 = time.clock()
print fib(1000000)
tf = time.clock()
print (tf - t0)*1000 , 'ms'
