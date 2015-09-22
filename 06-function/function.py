#!/usr/bin/python3

def main():
    myFunction(1,10)
    myFunction(70,80)
    myFunction()

def myFunction(ini=7,last=10):
    for i in range(ini,last+1):
         print(i, end = ' \n')

if __name__ == "__main__" : main()