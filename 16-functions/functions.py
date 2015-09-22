#!/usr/bin/python3

def main():
    funcao(1,2,3,4,5,6,7, um =1, dois = 2, tres = 3)

def funcao(p1,p2, *args, **kwargs):
    print(p1, p2)
    for i in args: print(i, end='')
    for k in kwargs: print(k, kwargs[k])

if __name__ == "__main__" : main()