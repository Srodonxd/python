from ksiazki import Book


dzial=input("Co chcesz zrobić? \n 1)usunąć książke \n 2)dodać książke \n 3)zobaczyć tytuły \n 4)Wyjść \n")
book_list_pre = []
book=Book(book_list_pre)



if(dzial=="1"):
    tytul=input("Tytuł: ")
    book.usun()

elif(dzial=="2"):
    
    tytul=input("Tytuł: ")
    autor=input("Autor: ")
    numer=int(input("Ile: "))
    
    nowe={
        
        "Tytuł":tytul,
        "Autor":autor,
        "Ilość":{
            "wypożyczone":0,
            "dostępne":numer,
            "razem":numer,
        }      
}
    book.dodaj(nowe, tytul, autor)
elif(dzial=="3"):
    book.display_info()


aktualna_lista = book.display_info()
print(aktualna_lista)
for book_info in book.book_list:
    print("NOWA KSIAZKLA::::")  
    print("Tytuł:",book_info["Tytuł"])
    print("Autor:",book_info["Autor"])
    for attribute, value in book_info["Ilość"].items():
        print(attribute + ":", value)


print(aktualna_lista)


book.dodaj(nowe, tytul, autor)
print(book.display_info())

def asd(s, s2, s3, s4):
    a = s / s2
    b = a * s4 - s3
    ####
    wynik = a - b * s2 - (s3-s4)
    return wynik

if asd():
    # Cos tam
else:
    # COs innego
a1 = asd(3, 5, 6, 78) # False
a2 = asd(3,57,81,23) # True

a1 / a2
# 3 5 16 3
# 5 31 6 87
# 5 12 7673 2
print(asd())
2
print(asd())
2
print(asd())