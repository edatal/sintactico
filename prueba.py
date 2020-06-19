tokens = []
class Token(object):
    def __init__(self):
        self.token = None
        self.tokenType = None
    
token = Token()
token.token = "cout"
token.tokenType = "restricted_word"
tokens.append(token)
token.token = "4"
token.tokenType = "integer"
tokens.append(token)
token.token = "+"
token.tokenType = "operator"
tokens.append(token)
token.token = "5"
token.tokenType = "integer"
tokens.append(token)
token.token = ";"
token.tokenType = "end_sentence"
tokens.append(token)

ig = 0

class Arbol(object):
    def __init__(self):
        self.nombre  = None
        self.dato  = None
        self.hijo = [None,None,None]
    
def match(tokensActual):
    global ig
    global tokens
    if tokens[ig].token == tokensActual:
        if ig < len(tokens)-1:
            ig += 1
    else:
        error()

def sent_cout():
    global ig
    global tokens
    nuevo = Arbol()
    nuevo.nombre = "Cout"
    if tokens[ig] == 'cout':
        match('cout')
        nuevo.hijo[0] = expresion()
        match(';')
    else: error()
    return nuevo

def bloque():
    global ig
    global tokens
    nuevo = Arbol()
    nuevo.nombre = "Bloque"
    if tokens[ig] == '{':
        match('{')
        #nuevo.hijo[0] = lista_sentencias()
        match('}')
    else: error()
    return nuevo

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
        nuevo.hijo[0] = temp
        nuevo.hijo[1] = expresion()
        temp = nuevo
        match(';')
    else: error()
    return temp

def expresion():
    global ig
    global tokens
    nuevo = Arbol()
    temp = expresion_simple()
    if(tokens[ig] == '<=' or tokens[ig] == '<' or tokens[ig] == '>=' or tokens[ig] == '>' or tokens[ig] == '=' or tokens[ig] == '!='):
        if tokens[ig] == '<=':
            match('<=')  
            nuevo.nombre = "<="
            nuevo.hijo[0] = temp
            nuevo.hijo[1] = expresion_simple()
            if (temp.dato <= nuevo.hijo[1].dato): nuevo.dato = True
            else: nuevo.dato = False
            temp = nuevo
        elif tokens[ig] == '<':
            match('<')  
            nuevo.nombre = "<"
            nuevo.hijo[0] = temp
            nuevo.hijo[1] = expresion_simple()
            if (temp.dato < nuevo.hijo[1].dato): nuevo.dato = True
            else: nuevo.dato = False
            temp = nuevo
        elif tokens[ig] == '>':
            match('>')  
            nuevo.nombre = ">"
            nuevo.hijo[0] = temp
            nuevo.hijo[1] = expresion_simple()
            if (temp.dato > nuevo.hijo[1].dato): nuevo.dato = True
            else: nuevo.dato = False
            temp = nuevo
        elif tokens[ig] == '>=':
            match('>=')  
            nuevo.nombre = ">="
            nuevo.hijo[0] = temp
            nuevo.hijo[1] = expresion_simple()
            if (temp.dato >= nuevo.hijo[1].dato): nuevo.dato = True
            else: nuevo.dato = False
            temp = nuevo
        elif tokens[ig] == '=':
            match('=')  
            nuevo.nombre = "="
            nuevo.hijo[0] = temp
            nuevo.hijo[1] = expresion_simple()
            if (temp.dato == nuevo.hijo[1].dato): nuevo.dato = True
            else: nuevo.dato = False
            temp = nuevo
        elif tokens[ig] == '!=':
            match('!=')  
            nuevo.nombre = "!="
            nuevo.hijo[0] = temp
            nuevo.hijo[1] = expresion_simple()
            if (temp.dato != nuevo.hijo[1].dato): nuevo.dato = True
            else: nuevo.dato = False
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
            nuevo.hijo[0] = temp
            nuevo.dato = temp.dato
            nuevo.hijo[1] = termino()
            nuevo.dato += nuevo.hijo[1].dato
            temp = nuevo
        elif tokens[ig] == '-':
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
    while(tokens[ig] == '*' or tokens[ig] =='/' or tokens[ig] == '%'):
        if tokens[ig] == '*':
            match('*') 
            nuevo.nombre = "*"
            nuevo.hijo[0] = temp
            nuevo.dato = temp.dato
            nuevo.hijo[1] = factor()
            nuevo.dato *= nuevo.hijo[1].dato
            temp = nuevo
        elif tokens == '/':
            match('/')  
            nuevo.nombre = "/"
            nuevo.hijo[0] = temp
            nuevo.dato = temp.dato
            nuevo.hijo[1] = factor()
            nuevo.dato /= nuevo.hijo[1].dato
            temp = nuevo
        elif tokens == '%':
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
    while(tokens[ig] == '^'):
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
    if tokens[ig].token == '(':
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
    raiz = sent_cout()
    print("Resultado: " + str(raiz.dato))
    verArbol(raiz)
    