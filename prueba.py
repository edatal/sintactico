token = ["44","+","2","*","5"]
ig = 0

class Arbol(object):
    def __init__(self):
        self.nombre  = None
        self.dato  = None
        self.der = None
        self.izq  = None
    
def match(tokenActual):
    global ig
    global token
    if token[ig] == tokenActual:
        if ig < len(token)-1:
            ig += 1
    else:
        error()

def expresion():
    global ig
    global token
    nuevo = Arbol()
    temp = termino()
    while(token[ig] == '+' or token[ig] == '-'):
        if token[ig] == '+':
            match('+')  
            nuevo.nombre = "+"
            nuevo.izq = temp
            nuevo.dato = temp.dato
            nuevo.der = termino()
            nuevo.dato += nuevo.der.dato
            temp = nuevo
        elif token[ig] == '-':
            match('-') 
            nuevo.nombre = "-"
            nuevo.izq = temp
            nuevo.dato = temp.dato
            nuevo.der = termino()
            nuevo.dato -= nuevo.der.dato
            temp = nuevo
    return temp

def termino():
    global ig
    global token
    nuevo = Arbol()
    temp = factor()
    while(token[ig] == '*' or token[ig] =='/' or token[ig] == '%'):
        if token[ig] == '*':
            match('*') 
            nuevo.nombre = "*"
            nuevo.izq = temp
            nuevo.dato = temp.dato
            nuevo.der = factor()
            nuevo.dato *= nuevo.der.dato
            temp = nuevo
        elif token == '/':
            match('/')  
            nuevo.nombre = "/"
            nuevo.izq = temp
            nuevo.dato = temp.dato
            nuevo.der = factor()
            nuevo.dato /= nuevo.der.dato
            temp = nuevo
        elif token == '%':
            match('%')  
            nuevo.nombre = "%"
            nuevo.izq = temp
            nuevo.dato = temp.dato
            nuevo.der = factor()
            nuevo.dato %= nuevo.der.dato
            temp = nuevo
    return temp

def factor():
    global ig
    global token
    nuevo = Arbol()
    temp = fin()
    while(token[ig] == '^'):
        match('^')
        nuevo.nombre = "^"
        nuevo.izq = temp
        nuevo.dato = temp.dato
        nuevo.der = fin()
        nuevo.dato **= nuevo.der.dato
        temp = nuevo
    return temp

def fin():
    global ig
    global token
    temp= Arbol()
    if token[ig] == '(':
        match('(')
        temp = expresion()
        match(')')
    elif token[ig].isdigit():
        temp.nombre = "Factor"
        temp.dato = int (token[ig])
        if ig < len(token)-1:
            ig += 1
    else:
        error()
    return temp

def error():
    print("Error Sintactico")

def verArbol(arbol):
    if(arbol != None):
        print("Nodo-> " + arbol.nombre)
        print("Valor-> " + str(arbol.dato))
        verArbol(arbol.izq)
        verArbol(arbol.der)
    return


if __name__== "__main__":
    raiz = Arbol()
    raiz = expresion()
    print("Resultado: " + str(raiz.dato))
    verArbol(raiz)
    