#from sympy import *
def f(x):
    return x**3 - 2*(x**2) - 5      # edite a funcao aqui

def Bissecao(p):

    a = float(input("Intervalo A: "))
    b = float(input("Intervalo B: "))

    fa = f(a)
    fb = f(b)           # ITERACAO 0
    xant = 0
    xprox = (a + b)/2
    fx = f(xprox)

    print("\nITERACAO 0 \na ="+str(a)+"\nf(a) = "+str(fa)+"\nb = "+str(b)+"\nf(b) = "+str(fb)+"\nx0 ="+str(xprox)+"\nf(x0) = "+str(fx)+"\n")

    if fa * fx > 0:
        a = xprox
    else:
        b = xprox

    precisao = abs(xant - xprox)
    print("precisao = "+str(precisao)+"\n")

    count = 1
    while precisao > p:
        fa = f(a)
        fb = f(b)
        xant = xprox
        xprox = (a + b)/2
        fx = f(xprox)
        print("\nITERACAO "+str(count)+" \na = "+str(a)+" \nf(a) = "+str(fa)+" \nb = "+str(b)+" \nf(b) = "+str(fb)+" \nx"+str(count)+"  = "+str(xprox)+" \nf(x"+str(count)+" ) = "+str(fx)+" \n")
        if fa * fx > 0:
            a = xprox
        else:
            b = xprox

        precisao = abs(xant - xprox)
        print("precisao = "+str(precisao)+"\n")
        count += 1

    print("x = "+str(xprox)+"\n")


def FalsaPosicao(p):

    a = float(input("Intervalo A: "))
    b = float(input("Intervalo B: "))

    fa = f(a)
    fb = f(b)           # ITERACAO 0
    xant = 0
    xprox = (a * abs(fb) + b * abs(fa)) / float((abs(fa) + abs(fb)))
    fx = f(xprox)
    print("\nITERACAO 0 \na ="+str(a)+"\nf(a) = "+str(fa)+"\nb = "+str(b)+"\nf(b) = "+str(fb)+"\nx0 ="+str(xprox)+"\nf(x0) = "+str(fx)+"\n")
    if fa * fx > 0:
        a = xprox
    else:
        b = xprox

    precisao = abs(xant - xprox)
    print("precisao = "+str(precisao)+"\n")

    count = 1
    while precisao > p:
        fa = f(a)
        fb = f(b)
        xant = xprox
        xprox = (a * abs(fb) + b * abs(fa)) / (abs(fa) + abs(fb))
        fx = f(xprox)
        print("\nITERACAO "+str(count)+" \na = "+str(a)+" \nf(a) = "+str(fa)+" \nb = "+str(b)+" \nf(b) = "+str(fb)+" \nx"+str(count)+"  = "+str(xprox)+" \nf(x"+str(count)+" ) = "+str(fx)+" \n")
        if fa * fx > 0:
            a = xprox
        else:
            b = xprox

        precisao = abs(xant - xprox)
        print("precisao = "+str(precisao)+"\n")
        count += 1

    print("x = "+str(xprox)+"\n")

def Newton(p):

    # x0 = float(input("x0 = "))
    # count = 0
    # while precisao > p:
    #
    #     x1 = x0 - f(x0)/diff(f(x),x).subs(x,x0)
    #     precisao = abs((x1 - x0)/x1)
    #     count += 1
    #     print("\nITERACAO "+str(count)+"\n x"+str(count)+" = "+str(x1)+"\n precisao = "+str(precisao))
    #
    # print("x = "+str(x1)+"\n")

def Secante(p):

    xant = float(input("x0 = "))
    xatual = float(input("x1 = "))

    fxant = f(xant)
    fxatual = f(xatual)

    xprox = (xant * fxatual - xatual * fxant) / (fxatual - fxant)

    precisao = abs(xatual - xprox)

    print("\nITERACAO 0 \nx0 = "+str(xant)+"\nf(x0) = "+str(fxant)+"\nx1 = "+str(xatual)+"\nf(x1) = "+str(fxatual)+"\nx2 = "+str(xprox)+"\n\nprecisao = "+str(precisao)+"\n")

    count = 3
    while precisao > p:

        xant = xatual
        xatual = xprox

        fxant = f(xant)
        fxatual = f(xatual)

        xprox = (xant * fxatual - xatual * fxant) / (fxatual - fxant)

        precisao = abs(xatual - xprox)

        print("\nITERACAO "+str(count)+" \nx"+str(count-1)+" = "+str(xant)+"\nf("+str(count-1)+") = "+str(fxant)+"\nx"+str(count)+" = "+str(xatual)+"\nf(x"+str(count)+") = "+str(fxatual))
        print("\nx"+str(count+1)+" = "+str(xprox)+"\n\nprecisao = "+str(precisao)+"\n")
        count += 1

    print("x = "+str(xprox)+"\n")


while (True):

    print("-" * 40)
    op = int(input("Escolha um método para encountrar a raiz:\n\n[0] Sair\n[1] Bissecao\n[2] Falsa Posicao\n[3] Newton\n[4] Secante\n\n>>> "))

    if (op == 1):
        Bissecao(float(input("\nPrecisao: ")))
    elif op == 2:
        FalsaPosicao(float(input("\nPrecisao: ")))
    # elif op == 3:
    #     Newton(float(input("\nPrecisao: ")))
    elif op == 4:
        Secante(float(input("\nPrecisao: ")))
    else:
        break
