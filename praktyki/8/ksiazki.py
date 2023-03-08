"""Napisz program, który będzie przechowywał informacje o książkach w bibliotece.
 Utwórz klasę 'Book', która będzie miała atrybuty 'title', 'author' oraz 'isbn'. 
 Następnie utwórz listę obiektów klasy 'Book', a w programie umożliw użytkownikowi dodawanie, usuwanie i wyświetlanie informacji o książkach z tej listy."""

class Book:
    def __init__(self, book_list):
        self.book_list=book_list
    
    def display_info(self):
        x=1
        for title, author, amount in book_list:
            print(x, "tytuł: ", title, "| autor: ", author, "| Ilość: ", amount)
            x+=1
    def dodaj(self):
        if(tytul==book_list & autor==book_list):
            book_list.append(tytul, autor, numer)
            

dzial=input("Co chcesz zrobić? \n 1)usunąć książke \n 2)dodać książke \n 3)zobaczyć tytuły \n 4)Wyjść \n")


book_list={
        "Książka1":{
            "IT",
            "nie pamiętam",
            "Ilosć":{
                "wypożyczone":4, 
                "dostępne":2, 
                "razem":3
                    }
                    },
        "Książka2":{
            "w pustyni i w puszczy", 
            "nie pamiętam", 
            "Ilosć":{
                "wypożyczone":1, 
                "dostępne":2, 
                "razem":3
            }, 
            "Książka3":{
                "Dziady", 
                "Mickiewicz",
                "Ilosć":{
                    "wypożyczone":1, 
                    "dostępne":2, 
                    "razem":3
                        }
            }

book=Book(book_list)

if(dzial==2):
    tytul=input("Tytuł: ")
    autor=input("Autor: ")
    numer=input("IBSN: ")
    
elif(dzial==3):
    book.display_info()