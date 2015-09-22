#!/usr/bin/python3

def main():
    try:
        for linha in ler('exemplo.txt2'):
            print(linha, end = '')
    except IOError as e:
        print("arquivo nao encontrado", e)
    except ValueError as e:
        print("Tipo de arquivo invalido", e)

def ler(nomearquivo):
    if nomearquivo.endswith('.txt'):
        arq = open('exemplo.txt')
        return arq.readlines()
    else: raise ValueError('A extensao do arquivo deve ser .txt')

if __name__ == "__main__" : main()