#napisz program, który wczytuje liczbę naturalnąi wypisuje wszystkie jej dzielniki
x=int(input("Wpisz liczbe naturalną: "))
y=x
while 0 != y:
    c=x%y
    if(c==0):
        print(y)
    y-=1