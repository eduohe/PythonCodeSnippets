#!/usr/bin/python3

def main():
    s = "esse é meu texto"
    for i, c in enumerate(s):
        if c == 't': continue
        if c == 'x': break
        print(i, c)
    print('fim')
if __name__ == "__main__" : main()