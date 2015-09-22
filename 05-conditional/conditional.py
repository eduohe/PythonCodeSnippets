#!/usr/bin/python3

def main():
    x, y = 2,2
    if x < y:
        print("x < y")
    elif x == y:
        print("x = y")
    else:
        print("x > y")

    result = "<=" if x <= y else ">="
    print(result)


if __name__ == "__main__" : main()