def f(x):
    return pow(x, 2) +x -6      # edite a funcao aqui

def Bissecao(p):

    a = float(input("Intervalo A: "))
    b = float(input("Intervalo B: "))

    fa = f(a)
    fb = f(b)           # ITERACAO 0
    xant = 0
    xprox = (a + b)/2
    fx = f(xprox)

    print(f"\nITERACAO 0 \na = {a}\nf(a) = {fa}\nb = {b}\nf(b) = {fb}\nx0 = {xprox}\nf(x0) = {fx}\n")

    if fa * fx > 0:
        a = xprox
    else:
        b = xprox

    precisao = abs(xant - xprox)
    print(f"precisao = {precisao}\n")

    cont = 1
    while precisao > p:
        fa = f(a)
        fb = f(b)
        xant = xprox
        xprox = (a + b)/2
        fx = f(xprox)
        print(f"\nITERACAO {cont} \na = {a}\nf(a) = {fa}\nb = {b}\nf(b) = {fb}\nx{cont} = {xprox}\nf(x{cont}) = {fx}\n")
        if fa * fx > 0:
            a = xprox
        else:
            b = xprox

        precisao = abs(xant - xprox)
        print(f"precisao = {precisao}\n")
        cont += 1

    print(f"x = {xprox}\n")


def FalsaPosicao(p):

    a = float(input("Intervalo A: "))
    b = float(input("Intervalo B: "))

    fa = f(a)
    fb = f(b)           # ITERACAO 0
    xant = 0
    xprox = (a * abs(fb) + b * abs(fa)) / float((abs(fa) + abs(fb)))
    fx = f(xprox)
    print(f"\nITERACAO 0 \na = {a}\nf(a) = {fa}\nb = {b}\nf(b) = {fb}\nx0 = {xprox}\nf(x0) = {fx}\n")
    if fa * fx > 0:
        a = xprox
    else:
        b = xprox

    precisao = abs(xant - xprox)
    print(f"precisao = {precisao}\n")

    cont = 1
    while precisao > p:
        fa = f(a)
        fb = f(b)
        xant = xprox
        xprox = (a * abs(fb) + b * abs(fa)) / (abs(fa) + abs(fb))
        fx = f(xprox)
        print(f"\nITERACAO {cont} \na = {a}\nf(a) = {fa}\nb = {b}\nf(b) = {fb}\nx{cont} = {xprox}\nf{cont} = {fx}\n")
        if fa * fx > 0:
            a = xprox
        else:
            b = xprox

        precisao = abs(xant - xprox)
        print(f"precisao = {precisao}\n")
        cont += 1

    print(f"x = {xprox}\n")

def Newton(p):

    x0 = float(input("x0 = "))


def Secante(p):

    xant = float(input("x0 = "))
    xatual = float(input("x1 = "))

    fxant = f(xant)
    fxatual = f(xatual)

    xprox = (xant * fxatual - xatual * fxant) / (fxatual - fxant)

    precisao = abs(xatual - xprox)

    print(f"\nITERACAO 2 \nx0 = {xant}\nf(x0) = {fxant}\nx1 = {xatual}\nf(x1) = {fxatual}\nx2 = {xprox}\n\nprecisao = {precisao}\n")

    cont = 3
    while precisao > p:

        xant = xatual
        xatual = xprox

        fxant = f(xant)
        fxatual = f(xatual)

        xprox = (xant * fxatual - xatual * fxant) / (fxatual - fxant)

        precisao = abs(xatual - xprox)

        print(f"\nITERACAO {cont} \nx{cont-1} = {xant}\nf({cont-1}) = {fxant}\nx{cont} = {xatual}\nf(x{cont}) = {fxatual}\nx{cont+1} = {xprox}\n\nprecisao = {precisao}\n")
        cont += 1

    print(f"x = {xprox}\n")


while (True):

    print("-" * 40)
    op = int(input("Escolha um método para encontrar a raiz:\n\n[0] Sair\n[1] Bissecao\n[2] Falsa Posicao\n[3] Newton\n[4] Secante\n\n>>> "))

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
