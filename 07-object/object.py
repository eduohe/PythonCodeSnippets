#!/usr/bin/python3

class Carro:
    def __init__(self, tipo = 'Corsa'):
        self.tipo = tipo
        
    def tipoCarro(self):
        return self.tipo

def main():
    carro1 = Carro()
    print(carro1.tipoCarro())
    carro2 = Carro('Ka')
    print(carro2.tipoCarro())

if __name__ == "__main__" : main()