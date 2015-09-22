#!/usr/bin/python3

def main():
    x = (1, 2, 3) #tuple -- imutable
    y = [4, 5, 6] #list -- mutable
    z = "texto"

    y.append(10)
    y.insert(0, 9)

    for i in x: print(i)
    for i in y: print(i)
    for i in z: print(i)

    print(z[0])

    print(type(x), x)
    print(type(y), y)

if __name__ == "__main__" : main()