"""Napisz program, który będzie przechowywał informacje o książkach w bibliotece.
 Utwórz klasę 'Book', która będzie miała atrybuty 'title', 'author' oraz 'isbn'. 
 Następnie utwórz listę obiektów klasy 'Book', a w programie umożliw użytkownikowi dodawanie, usuwanie i wyświetlanie informacji o książkach z tej listy."""

class Book:
    def __init__(self, book_list):
        self.book_list=book_list
    
    def display_info(self):
        for book_info in book_list:
            print()    
            print("Tytuł:",book_info["Tytuł"])
            print("Autor:",book_info["Autor"])
            for attribute, value in book_info["Ilość"].items():
                print(attribute + ":", value)
    
    def dodaj(self, nowe):
        ilosc=0
        for item in book_list:
            if(tytul in item and autor in item):
                ilosc+=1
            else:
                self.book_list.append(nowe)
                break
    def usun(self):
        index=book_list.index(tytul)
        del book_list[index]            
    
    
        
        # Jesli istnieje update, jesli nie dddodac do listy slef.book_list.append(...)
        # nie masz zmiennej tytul i autor, musisz to wziac z nowe['tytul'] i nowe['autor'] bo przekazujesz slownik


        # Znajdx rozwiazanie w necie jak znalezc klucz slownika w liscie albo tak jak mowis zpoprostu petla w self.book_list i porownujesz tytuly

            # Ilosc ? Czego, skad? To masz ilosc jakiejs zmiennej, no tak a jak juz masz ich 5? to dodasz o 1 do ilosci a w klasie nie zmieni sie wartosc tylko tam u gory
            # potem znowu ktos dodaje i zamiast 2 ma 3 etc.
            # wykonaj te instrukcje wyzej
            

dzial=input("Co chcesz zrobić? \n 1)usunąć książke \n 2)dodać książke \n 3)zobaczyć tytuły \n 4)Wyjść \n")

book_list=[
                {
                "Tytuł":"IT",
                "Autor":"nie pamiętam",
                "Ilość":{
                    "wypożyczone":2, 
                    "dostępne":3, 
                    "razem":5
                        }
                }, 
                {
                    "Tytuł":"w pustyni i w puszczy", 
                    "Autor":"nie pamiętam", 
                    "Ilość":{
                        "wypożyczone":1, 
                        "dostępne":2, 
                        "razem":3
                            }
                }
            ]

book=Book(book_list)
if(dzial=="1"):
    tytul=input("Tytuł: ")
    book.usun()
elif(dzial=="2"):
    
    tytul=input("Tytuł: ")
    autor=input("Autor: ")
    numer=input("Ile: ")
    
    nowe={

        "Tytuł":tytul,
        "Autor":autor,
        "Ilość":{
            "wypożyczone":0,
            "dostępne":numer,
            "razem":numer,
        }      
}
    book.dodaj(nowe)
elif(dzial=="3"):
    book.display_info()

for book_info in book_list:
    print()   
    print("Tytuł:",book_info["Tytuł"])
    print("Autor:",book_info["Autor"])
    for attribute, value in book_info["Ilość"].items():
        print(attribute + ":", value)