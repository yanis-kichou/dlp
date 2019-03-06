from prime import is_probable_prime
from math import sqrt
import random


#Exercice 1
#Q1
def PGCD(a,b):
    while b!=0:
        r=a%b
        a,b=b,r
    return a
def bezout(a, b):
    if a==0 and b==0 : return (0,0,0)
    if b==0: return (a//abs(a),0,abs(a))
    (u,v,p)=bezout(b,a%b)
    return (v,(u-v*(a//b)),p)

#Q2
def inv_mod(a, n):
    for i in range(1,n):
        if(((i*a) % n) == 1):
            return i
    return n


def invertibles(N):
    inv=list()
    for i in range(N):
        if(inv_mod(i,N)!=N):
            inv.append(i)
    return inv


#Q3
def phi(N):
    inversible=invertibles(N)
    phiN=0
    for i in inversible:
        if(PGCD(i,N)==1 and i<N):
            phiN+=1
    return phiN


#Exercice 2
#Q1
def exp(a, n, p):
    return math.exp(a,p)%n


#Q2
def factor(n):
   return


#Q3
def order(a, p, factors_p_minus1):
    return


#Q4
def find_generator(p, factors_p_minus1):
    return


#Q5
def generate_safe_prime(k):
    return


#Q6
def bsgs(n, g, p):
    return


#Q8
def next(x, a, b, n, h, p):
    return


#Q9
def rho_pollard(n, h, q, p):
    return
