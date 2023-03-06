#Napisz program, który poprosi użytkownika o podanie liczby całkowitej i wyświetli informację, czy podana liczba jest parzysta czy nieparzysta.
x=int(input("podaj liczbe: "))
y=x%2
if(y!=0):
    print("liczba jest nieparzysta")
else:
    print("liczba jest parzysta")
