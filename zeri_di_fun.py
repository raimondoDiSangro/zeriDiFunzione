# -*- coding: utf-8 -*-
"""
Calcolo degli zeri di funzione

Esercizi per l'esame di Calcolo Numerico

"""

def bisezioni(f,a,b,tol,nmax):
    nit=0
    err=.5*(b-a)
    fa=f(a)
    fb=f(b)
    while err>tol and nit<nmax:
        x=.5*(a+b)
        fx=f(x)
        if fa*fx<0:
            b=x
            fb=fx
        else:
            a=x
            fa=fx
        err=.5*err
        nit+=1
    return (x,nit)

def newton(f,df,x0,tol,nmax):
    nit=0
    err=tol+1
    while err>tol and nit<nmax:
        dfx0=df(x0)
        if dfx0==0:
            print('denominatore nullo')
            nit=-1
            return (x0,nit)
        fx0=f(x0)
        delta=-fx0/dfx0
        x1=x0+delta
        err=abs(delta)
        x0=x1
        nit+=1
    if err>tol:
        print('raggiunto nmax con err>tol')
        nit=-2
    return (x1,nit)
