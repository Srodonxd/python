#Napisz program, który pobierze od użytkownika listę liczb całkowitych, a następnie wyświetli sumę, średnią oraz odchylenie standardowe tych liczb.
import math
print("podaj 5 liczb")
listaa=[]
lista=[int(num) for num in listaa]
kwadrat=wynik_odchylenia=suma_odchylenia=odchylenie=d=c=i=suma=srednia=0

while i!=5:
    x=int(input())
    lista.append(x)
    i+=1
dlugosc_listy=len(lista)

while c!=dlugosc_listy:
    suma=suma+lista[c]
    srednia=suma/dlugosc_listy
    c+=1
print("suma: ",suma)
print("średnia: ",srednia)

while d!=dlugosc_listy:
    odchylenie= lista[d] - srednia
    odchylenie1=int(odchylenie)
    kwadrat=math.pow(odchylenie1,2)
    suma_odchylenia=suma_odchylenia+kwadrat
    d+=1
wynik_odchylenia=suma_odchylenia/srednia
wynik_odchylenia=math.sqrt(wynik_odchylenia)
print("odchylenie standardowe: ",round(wynik_odchylenia,3))


