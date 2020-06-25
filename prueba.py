tokens = []
class Token(object):
    def __init__(self):
        self.token = None
        self.tokenType = None
    
token0 = Token()
token1 = Token()
token2 = Token()
token3 = Token()
token4 = Token()
token0.token = "cin"
token0.tokenType = "restricted_word"
tokens.append(token0)
token1.token = "var"
token1.tokenType = "Identifier"
tokens.append(token1)
token4.token = ";"
token4.tokenType = "end_sentence"
tokens.append(token4)

ig = 0

class Arbol(object):
    def __init__(self):
        self.nombre  = None
        self.dato  = None
        self.hijo = [None,None,None]
        self.sibling = []
    
def match(tokensActual):
    global ig
    global tokens
    if tokens[ig].token == tokensActual:
        if ig < len(tokens)-1:
            ig += 1
    else:
        error()

def programa():
    global ig
    global tokens
    temp = Arbol()
    temp.nombre = "Main"
    match('main')
    match('{')
    temp.hijo[0] = lista_declaracion()
    temp.hijo[1] = lista_sentencias()
    match('}')
    return temp

def lista_declaracion():
    global ig
    global tokens
    temp = Arbol()
    temp.nombre = "Lista Declaracion"
    var = ";"
    while(var == ";"):
        match(';')
        temp.sibling.append(declaracion())
        var = tokens[ig].token 
    return tem

def declaracion():
    global ig
    global tokens
    temp = Arbol()
    temp.nombre = "Declaracion"
    temp.hijo[0] = tipo()
    temp.hijo[1] = lista_variables()
    return temp

def tipo():
    global ig
    global tokens
    if tokens[ig].token == "int":
        match('int')
    if tokens[ig].token == "float":
        match('float')
    if tokens[ig].token == "bool":
        match('bool')

def lista_variables():
    global ig
    global tokens
    temp = Arbol()
    temp.nombre = "Lista variables"
    temp.sibling.append(fin())
    while(tokens[ig].token == ","):
        match(',')
        temp.sibling.append(fin())
    return temp

def lista_sentencias():
    global ig
    global tokens
    temp = Arbol()
    temp.nombre = "Lista Sentencias"
    temp.hijo[0] = sentencia()
    if tokens[ig].token == ';':
        match(';')
        temp.hijo[1] = lista_sentencias()
    return temp
    
def sentencia():
    global ig
    global tokens
    temp = Arbol()
    temp.nombre = "Sentencia"
    if tokens[ig].token == 'seleccion' or tokens[ig].token == 'iteracion' or tokens[ig].token == 'repetecion' or tokens[ig].token == 'sent_cin' or tokens[ig].token == 'sent_cout' or tokens[ig].token == 'bloque' or tokens[ig].token == 'asignacion':
        if tokens[ig].token == 'seleccion':
            temp.hijo[0] = seleccion()
        elif tokens[ig].token == 'iteracion':
            temp.hijo[0] = iteracion()
        elif tokens[ig].token == 'repeticion':
            temp.hijo[0] = repeticion()
        elif tokens[ig].token == 'sent_cin':
            temp.hijo[0] = sent_cin()
        elif tokens[ig].token == 'sent_cout':
            temp.hijo[0] = sent_cout()
        elif tokens[ig].token == 'bloque':
            temp.hijo[0] = bloque()
        elif tokens[ig].token == 'asignacion':
            temp.hijo[0] = asignacion()
    else:
        error()
    return temp

def seleccion():
    global ig
    global tokens
    temp = Arbol()
    temp.nombre = "Seleccion"
    match('if')
    match('(')
    temp.hijo[0] = expresion()
    match(')')
    match('then')
    temp.hijo[1] = bloque()
    if tokens[ig].token == "else":
        match('else')
        temp.hijo[2] = bloque()
    match('end')
    return temp

def iteracion():
    global ig
    global tokens
    temp = Arbol()
    temp.nombre = "Iteracion"
    match('while')
    match('(')
    temp.hijo[0] = expresion()
    match(')')
    temp.hijo[1] = bloque()
    return temp

def repeticion():
    global ig
    global tokens
    temp = Arbol()
    temp.nombre = "Repeat"
    match('do')
    temp.hijo[0] = bloque()
    match('while')
    match('(')
    temp.hijo[1] = expresion()
    match(')')
    match(';')
    return temp

def sent_cin():
    global ig
    global tokens
    temp = Arbol()
    nuevo = Arbol()
    temp.nombre = "Cin"
    match('cin')
    nuevo.nombre = "Indentifier"
    nuevo.dato = tokens[ig].token
    temp.hijo[0] = nuevo
    if ig < len(tokens)-1:
        ig += 1
    else:
        error()
    match(';')
    return temp

def sent_cout():
    global ig
    global tokens
    temp = Arbol()
    temp.nombre = "Cout"
    match('cout')
    temp.hijo[0] = expresion()
    match(';')
    return temp

def bloque():
    global ig
    global tokens
    temp = Arbol()
    temp.nombre = "Bloque"
    match('{')
    temp.hijo[0] = lista_sentencias()
    match('}')
    return temp

def asignacion():
    global ig
    global tokens
    nuevo = Arbol()
    temp = Arbol()
    temp.nombre = "Variable"
    temp.dato = tokens[ig].token
    if ig < len(tokens)-1:
        ig += 1
    else:
        error()
    match(':=')
    nuevo.nombre = "Asignacion"
    nuevo.hijo[0] = temp
    nuevo.hijo[1] = expresion()
    temp = nuevo
    match(';')
    return temp

def expresion():
    global ig
    global tokens
    nuevo = Arbol()
    temp = expresion_simple()
    if(tokens[ig].token == '<=' or tokens[ig].token == '<' or tokens[ig].token == '>=' or tokens[ig].token == '>' or tokens[ig].token == '=' or tokens[ig].token == '!='):
        if tokens[ig].token == '<=':
            match('<=')  
            nuevo.nombre = "<="
            nuevo.hijo[0] = temp
            nuevo.hijo[1] = expresion_simple()
            if (temp.dato <= nuevo.hijo[1].dato): 
                nuevo.dato = True
            else: 
                nuevo.dato = False
            temp = nuevo
        elif tokens[ig].token == '<':
            match('<')  
            nuevo.nombre = "<"
            nuevo.hijo[0] = temp
            nuevo.hijo[1] = expresion_simple()
            if (temp.dato < nuevo.hijo[1].dato): 
                nuevo.dato = True
            else: 
                nuevo.dato = False
            temp = nuevo
        elif tokens[ig].token == '>':
            match('>')  
            nuevo.nombre = ">"
            nuevo.hijo[0] = temp
            nuevo.hijo[1] = expresion_simple()
            if (temp.dato > nuevo.hijo[1].dato): 
                nuevo.dato = True
            else: 
                nuevo.dato = False
            temp = nuevo
        elif tokens[ig].token == '>=':
            match('>=')  
            nuevo.nombre = ">="
            nuevo.hijo[0] = temp
            nuevo.hijo[1] = expresion_simple()
            if (temp.dato >= nuevo.hijo[1].dato): 
                nuevo.dato = True
            else: 
                nuevo.dato = False
            temp = nuevo
        elif tokens[ig].token == '=':
            match('=')  
            nuevo.nombre = "="
            nuevo.hijo[0] = temp
            nuevo.hijo[1] = expresion_simple()
            if (temp.dato == nuevo.hijo[1].dato): 
                nuevo.dato = True
            else: 
                nuevo.dato = False
            temp = nuevo
        elif tokens[ig].token == '!=':
            match('!=')  
            nuevo.nombre = "!="
            nuevo.hijo[0] = temp
            nuevo.hijo[1] = expresion_simple()
            if (temp.dato != nuevo.hijo[1].dato): 
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
    while(tokens[ig].token == '+' or tokens[ig].token == '-'):
        if tokens[ig].token == '+':
            match('+')  
            nuevo.nombre = "+"
            nuevo.hijo[0] = temp
            nuevo.dato = temp.dato
            nuevo.hijo[1] = termino()
            nuevo.dato += nuevo.hijo[1].dato
            temp = nuevo
        elif tokens[ig].token == '-':
            match('-') 
            nuevo.nombre = "-"
            nuevo.hijo[0] = temp
            nuevo.dato = temp.dato
            nuevo.hijo[1] = termino()
            nuevo.dato -= nuevo.hijo[1].dato
            temp = nuevo
    return temp

def termino():
    global ig
    global tokens
    nuevo = Arbol()
    temp = factor()
    while(tokens[ig].token == '*' or tokens[ig].token =='/' or tokens[ig].token == '%'):
        if tokens[ig].token == '*':
            match('*') 
            nuevo.nombre = "*"
            nuevo.hijo[0] = temp
            nuevo.dato = temp.dato
            nuevo.hijo[1] = factor()
            nuevo.dato *= nuevo.hijo[1].dato
            temp = nuevo
        elif tokens[ig].token == '/':
            match('/')  
            nuevo.nombre = "/"
            nuevo.hijo[0] = temp
            nuevo.dato = temp.dato
            nuevo.hijo[1] = factor()
            nuevo.dato /= nuevo.hijo[1].dato
            temp = nuevo
        elif tokens[ig].token == '%':
            match('%')  
            nuevo.nombre = "%"
            nuevo.hijo[0] = temp
            nuevo.dato = temp.dato
            nuevo.hijo[1] = factor()
            nuevo.dato %= nuevo.hijo[1].dato
            temp = nuevo
    return temp

def factor():
    global ig
    global tokens
    nuevo = Arbol()
    temp = fin()
    while(tokens[ig].token == '^'):
        match('^')
        nuevo.nombre = "^"
        nuevo.hijo[0] = temp
        nuevo.dato = temp.dato
        nuevo.hijo[1] = fin()
        nuevo.dato **= nuevo.hijo[1].dato
        temp = nuevo
    return temp

def fin():
    global ig
    global tokens
    temp = Arbol()
    if tokens[ig].tokenType == 'special_caracter':
        match('(')
        temp = expresion()
        match(')')
    elif tokens[ig].tokenType == "integer" or tokens[ig].tokenType == "float":
        temp.nombre = tokens[ig].tokenType
        if tokens[ig].tokenType == "integer":
            temp.dato = int (tokens[ig].token)
        elif tokens[ig].tokenType == "float":
            temp.dato = float (tokens[ig].token)
        if ig < len(tokens)-1:
            ig += 1
    elif tokens[ig].tokenType == "identifier":
        temp.nombre = tokens[ig].tokenType
        temp.dato = tokens[ig].token
    else:
        error()
    return temp

def error():
    print("Error Sintactico")

def verArbol(arbol):
    if(arbol != None):
        print("Nodo-> " + arbol.nombre)
        print("Valor-> " + str(arbol.dato))
        verArbol(arbol.hijo[0])
        verArbol(arbol.hijo[1])
    return


if __name__== "__main__":
    raiz = Arbol()
    raiz = sent_cin()
    print("Resultado: " + str(raiz.dato))
    verArbol(raiz)
    