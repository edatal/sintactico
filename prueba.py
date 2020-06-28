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
token5 = Token()
token6 = Token()
token7 = Token()
token8 = Token()
token9 = Token()
token10 = Token()
token11 = Token()
token12 = Token()
token13 = Token()
token14 = Token()
token15 = Token()
token16 = Token()
token17 = Token()
token18 = Token()

token0.token = "main"
token0.tokenType = "restricted_word"
tokens.append(token0)

token1.token = "{"
token1.tokenType = "special_character"
tokens.append(token1)

token2.token = "int"
token2.tokenType = "restricted_word"
tokens.append(token2)

token3.token = "a"
token3.tokenType = "identifier"
tokens.append(token3)

token4.token = ";"
token4.tokenType = "end_sentence"
tokens.append(token4)

token5.token = "float"
token5.tokenType = "restricted_word"
tokens.append(token5)

token6.token = "c"
token6.tokenType = "identifier"
tokens.append(token6)

token7.token = ";"
token7.tokenType = "end_sentence"
tokens.append(token7)

token8.token = "cout"
token8.tokenType = "restricted_word"
tokens.append(token8)

token9.token = "4"
token9.tokenType = "integer"
tokens.append(token9)

token10.token = ";"
token10.tokenType = "end_sentence"
tokens.append(token10)

token11.token = "}"
token11.tokenType = "special_character"
tokens.append(token11)

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
        print(tokens[ig].token)
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
    return temp

def lista_declaracion():
    global ig
    global tokens
    temp = Arbol()
    temp.nombre = "Lista Declaracion"
    temp.sibling.append(declaracion())
    match(';')
    while (temp.sibling[len(temp.sibling)-1] != None):
        temp.sibling.append(declaracion())
        if temp.sibling[len(temp.sibling)-1] != None:
            match(';')
    return temp

def declaracion():
    global ig
    global tokens
    if (tokens[ig].token == 'int' or tokens[ig].token == 'float' or tokens[ig].token == 'bool'):
        temp = Arbol()
        temp.nombre = "Declaracion"
        temp.hijo[0] = tipo()
        temp.hijo[1] = lista_variables()
        return temp

def tipo():
    global ig
    global tokens
    temp = Arbol()
    temp.nombre = "Tipo"
    if tokens[ig].token == "int":
        temp.dato = tokens[ig].token
        match('int')
    elif tokens[ig].token == "float":
        temp.dato = tokens[ig].token
        match('float')
    elif tokens[ig].token == "bool":
        temp.dato = tokens[ig].token
        match('bool')
    return temp

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
    temp.sibling.append(sentencia())
    while temp.sibling[len(temp.sibling)-1] != None:
        temp.sibling.append(sentencia())
    return temp
    
def sentencia():
    global ig
    global tokens
    if tokens[ig].token == 'if' or tokens[ig].token == 'while' or tokens[ig].token == 'do' or tokens[ig].token == 'cin' or tokens[ig].token == 'cout' or tokens[ig].token == '{' or tokens[ig].tokenType == 'identifier':
        temp = Arbol()
        temp.nombre = "Sentencia"
        if tokens[ig].token == 'if':
            temp.hijo[0] = seleccion()
        elif tokens[ig].token == 'while':
            temp.hijo[0] = iteracion()
        elif tokens[ig].token == 'do':
            temp.hijo[0] = repeticion()
        elif tokens[ig].token == 'cin':
            temp.hijo[0] = sent_cin()
        elif tokens[ig].token == 'cout':
            temp.hijo[0] = sent_cout()
        elif tokens[ig].token == '{':
            temp.hijo[0] = bloque()
        elif tokens[ig].tokenType == 'identifier':
            temp.hijo[0] = asignacion()
        return temp
    #else:
    #    error()

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
    nuevo.nombre = "identifier"
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
        if ig < len(tokens)-1:
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
        for s in arbol.sibling:
            verArbol(s)
        verArbol(arbol.hijo[0])
        verArbol(arbol.hijo[1])
        verArbol(arbol.hijo[2])
    return


if __name__== "__main__":
    raiz = programa()
    verArbol(raiz)
    