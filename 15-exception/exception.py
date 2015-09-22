#!/usr/bin/python3

def main():
    try:
        arq = open('exemplo.txt')
        for index, linha in enumerate(arq.readlines()):
            print(index, linha, end = '')
    except IOError as e:
        print("arquivo nao encontrado", e)


if __name__ == "__main__" : main()