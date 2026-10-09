import math
from abc import ABC, abstractmethod

class FungsiMatematika(ABC):
    @abstractmethod
    def bentukFungsi(self, x):
        pass
    def hitung(self, x):
        pass
    def analisis(self, x):
        return[]
    def show(self, x):
        print("Hasil perhitungan fungsi: ", self.bentukFungsi(x))
        print("Nilai f(%s) = %s" % (x, self.hitung(x)))

class fungsiKonstan(FungsiMatematika):
    def __init__(self, c):
        self.c = c
    def bentukFungsi(self, x):
        return "%s" % (self.c)
    def hitung(self, x):
        return self.c
    def analisis(self, x):
        return ["Konstan"]
    
class fungsiLinear(FungsiMatematika):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def bentukFungsi(self, x):
        return "%sx + %s" % (self.a, self.b)
    def hitung(self, x):
        return self.a * x + self.b
    def analisis(self, x):
        return ["Linear"]
    
class fungsiKuadrat(FungsiMatematika):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def bentukFungsi(self, x):
        return "%sx^2 + %sx + %s" % (self.a, self.b, self.c)
    def hitung(self, x):
        return self.a * x**2 + self.b * x + self.c
    def analisis(self, x):
        diskriminan = self.b**2 - 4*self.a*self.c
        if diskriminan > 0:
            return ["Kuadrat", "Dua Akar Real"]
        elif diskriminan == 0:
            return ["Kuadrat", "Satu Akar Real"]
        else:
            return ["Kuadrat", "Tidak Ada Akar Real"]

class fungsiFibonacci(FungsiMatematika):
    def bentukFungsi(self,x):
        return "Fibonacci ke-%s" % (x)
    def fibonacci(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)
        
    def hitung(self, x):
            if x >= 1 and x == int(x):
                return self.fibonacci(x)
            return "Input harus bilangan bulat positif"
        
class Main:
    garis = "=" * 50
    def __init__(self):
        self.a = 0.0
        self.b = 0.0
        self.c = 0.0
        self.x = 0.0
    
    def judul(self):
        print(self.garis)
        print("Program Fungsi Matematika")
        print(self.garis)
        
    def input(self):
        self.a = float(input("Masukkan nilai a: "))
        self.b = float(input("Masukkan nilai b: "))
        self.c = float(input("Masukkan nilai c: "))
        self.x = float(input("Masukkan nilai x yang ingin dievaluasi: "))
        print()
    
    def start(self):
        self.judul()
        self.input()
        daftar_fungsi = [
            fungsiKonstan(self.c),
            fungsiLinear(self.a, self.b),
            fungsiKuadrat(self.a, self.b, self.c),
            fungsiFibonacci(),
        ]
        print("--Hasil Evaluasi dan Analisis--")
        for fungsi in daftar_fungsi:
            fungsi.show(self.x)
        print(self.garis)

if __name__ == "__main__":
    main = Main()
    main.start()