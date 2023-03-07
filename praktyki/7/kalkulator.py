class Kalkulator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def suma(self):
        wynik=self.a+self.b
        return wynik
    def roznica(self):
        wynik=self.a-self.b
        return wynik
    def mnozenie(self):
        wynik=self.a*self.b
        return wynik
    def dzielenie(self):
        wynik=self.a/self.b
        return wynik

dzial=input("co chcesz robobić? \n 1)dodawanie \n 2)odejmownie \n 3)mnożenie \n 4)dzielenie \n ")
a=int(input("podaj pierwszą liczbe: "))
b=int(input("podaj drugą liczbe: "))
kalkulator=Kalkulator(a,b)

if(dzial=="1"):
    wynik=kalkulator.suma()
elif(dzial=="2"):
    wynik=kalkulator.roznica()
elif(dzial=="3"):
    wynik=kalkulator.mnozenie()
elif(dzial=="4"):
    wynik=kalkulator.dzielenie()
else:
    wynik="błąd obliczeń"
    
print("Wynik: ",wynik)