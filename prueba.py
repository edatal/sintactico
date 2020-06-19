tokens = ["var",":=","2","-","(","44","+","2","*","5",")"]
ig = 0

class Arbol(object):
    def __init__(self):
        self.nombre  = None
        self.dato  = None
        self.der = None
        self.izq  = None
    
def match(tokensActual):
    global ig
    global tokens
    if tokens[ig] == tokensActual:
        if ig < len(tokens)-1:
            ig += 1
    else:
        error()

def asignacion():
    global ig
    global tokens
    nuevo = Arbol()
    temp = Arbol()
    temp.nombre = "Variable"
    temp.dato = tokens[ig]
    if ig < len(tokens)-1:
        ig += 1
    else:
        error()
    if tokens[ig] == ':=':
        match(':=')
        nuevo.nombre = "Asignacion"
        nuevo.izq = temp
        nuevo.der = expresion()
        nuevo.dato = nuevo.der.dato
        temp = nuevo
        match(';')
    else:
        error()
    return temp

def expresion():
    global ig
    global tokens
    nuevo = Arbol()
    temp = expresion_simple()
    if tokens[ig] == '<=' or tokens[ig] == '<' or tokens[ig] == '>' or tokens[ig] == '>=' or tokens[ig] == '=' or tokens[ig] == '!=':
        if tokens[ig] == '<=':
            match('<=')  
            nuevo.nombre = "<="
            nuevo.izq = temp
            nuevo.der = expresion_simple()
            if temp.dato <= nuevo.der.dato:
                nuevo.dato = True
            else:
                nuevo.dato = False
            temp = nuevo
        elif tokens[ig] == '<':
            match('<')  
            nuevo.nombre = "<"
            nuevo.izq = temp
            nuevo.der = expresion_simple()
            if temp.dato < nuevo.der.dato:
                nuevo.dato = True
            else:
                nuevo.dato = False
            temp = nuevo
        elif tokens[ig] == '>':
            match('>')  
            nuevo.nombre = ">"
            nuevo.izq = temp
            nuevo.der = expresion_simple()
            if temp.dato > nuevo.der.dato:
                nuevo.dato = True
            else:
                nuevo.dato = False
            temp = nuevo
        elif tokens[ig] == '>=':
            match('>=')
            nuevo.nombre = ">="
            nuevo.izq = temp
            nuevo.der = expresion_simple()
            if temp.dato >= nuevo.der.dato:
                nuevo.dato = True
            else:
                nuevo.dato = False
            temp = nuevo
        elif tokens[ig] == '=':
            match('=')
            nuevo.nombre = "="
            nuevo.izq = temp
            nuevo.der = expresion_simple()
            if temp.dato == nuevo.der.dato:
                nuevo.dato = True
            else:
                nuevo.dato = False
            temp = nuevo
        elif tokens[ig] == '!=':
            match('!=')
            nuevo.nombre = "!="
            nuevo.izq = temp
            nuevo.der = expresion_simple()
            if temp.dato != nuevo.der.dato:
                nuevo.dato = True
            else:
                nuevo.dato = False
            temp = nuevo
    return temp

def expresion_simple():
    global ig
    global tokens
    nuevo = Arbol()
    temp = termino()
    while(tokens[ig] == '+' or tokens[ig] == '-'):
        if tokens[ig] == '+':
            match('+')  
            nuevo.nombre = "+"
            nuevo.izq = temp
            nuevo.dato = temp.dato
            nuevo.der = termino()
            nuevo.dato += nuevo.der.dato
            temp = nuevo
        elif tokens[ig] == '-':
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
    global tokens
    nuevo = Arbol()
    temp = factor()
    while(tokens[ig] == '*' or tokens[ig] =='/' or tokens[ig] == '%'):
        if tokens[ig] == '*':
            match('*') 
            nuevo.nombre = "*"
            nuevo.izq = temp
            nuevo.dato = temp.dato
            nuevo.der = factor()
            nuevo.dato *= nuevo.der.dato
            temp = nuevo
        elif tokens == '/':
            match('/')  
            nuevo.nombre = "/"
            nuevo.izq = temp
            nuevo.dato = temp.dato
            nuevo.der = factor()
            nuevo.dato /= nuevo.der.dato
            temp = nuevo
        elif tokens == '%':
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
    global tokens
    nuevo = Arbol()
    temp = fin()
    while(tokens[ig] == '^'):
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
    global tokens
    temp= Arbol()
    if tokens[ig] == '(':
        match('(')
        temp = expresion()
        match(')')
    elif tokens[ig].isdigit():
        temp.nombre = "Factor"
        temp.dato = int (tokens[ig])
        if ig < len(tokens)-1:
            ig += 1
    else:
        error()
    return temp

def error():
    print("Error Sintactico \n")

def verArbol(arbol):
    if(arbol != None):
        print("Nodo-> " + arbol.nombre)
        print("Valor-> " + str(arbol.dato))
        verArbol(arbol.izq)
        verArbol(arbol.der)
    return


if __name__== "__main__":
    raiz = Arbol()
    raiz = asignacion()
    print("Resultado: " + str(raiz.dato) + "\n")
    verArbol(raiz)
    