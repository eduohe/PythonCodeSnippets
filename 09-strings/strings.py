#!/usr/bin/python3

def main():
    numero = 3
    
    texto = 'Teste de string'
    texto2 = '{} Teste de string'.format(2) #python 3
    texto3 = '%s Teste de string' % numero # python 2
    texto4 = 'Linha 1\n Linha2'
    texto5 = r'Linha 1\n Linha2'
    texto6 = '''\
Texto em python
com varias
linhas
'''
   
    print(type(texto), texto)
    print(type(texto2), texto2)
    print(type(texto3), texto3)
    print(type(texto4), texto4)
    print(type(texto5), texto5)
    print(type(texto6), texto6)

if __name__ == "__main__" : main()