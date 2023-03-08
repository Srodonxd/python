"""Napisz program, który będzie przechowywał informacje o książkach w bibliotece.
 Utwórz klasę 'Book', która będzie miała atrybuty 'title', 'author' oraz 'isbn'. 
 Następnie utwórz listę obiektów klasy 'Book', a w programie umożliw użytkownikowi dodawanie, usuwanie i wyświetlanie informacji o książkach z tej listy."""

class Book:
    def __init__(self, book_list):
        self.book_list=book_list
    
    def display_info(self):
        x=1
        for title, author, isbn in book_list:
            print(x, "tytuł: ", title, "| autor: ", author, "| isbn: ", isbn)
            x+=1
    def dodaj(self):
        book_list.append(tytul, autor, numer)

dzial=input("Co chcesz zrobić? \n 1)usunąć książke \n 2)dodać książke \n 3)zobaczyć tytuły \n 4)Wyjść \n")


book_list=[("IT", "nie pamiętam", 23454325), ("w pustyni i w puszczy", "nie pamiętam", 2340293), ("Dziady", "Mickiewicz", 213545323)]
book=Book(book_list)

#if(dzial!=1):

if(dzial!=2):
    tytul=input("Tytuł: ")
    autor=input("Autor: ")
    numer=input("IBSN: ")
    
elif(dzial!=3):
    book.display_info()