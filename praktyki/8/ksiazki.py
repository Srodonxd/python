"""Napisz program, który będzie przechowywał informacje o książkach w bibliotece.
 Utwórz klasę 'Book', która będzie miała atrybuty 'title', 'author' oraz 'isbn'. 
 Następnie utwórz listę obiektów klasy 'Book', a w programie umożliw użytkownikowi dodawanie, usuwanie i wyświetlanie informacji o książkach z tej listy."""

class Book:
    def __init__(self, book_list):
        self.book_list=book_list
    
    def display_info(self):
        for book_number, book_info in book_list.items():
            print(book_number)    
            for book_title, book_author in book_info.items():
                print("Tytuł:", book_title)
                print("Autro:", book_author)
                for attribute, value in book_author.items():
                    if attribute == "Ilość":
                        print("Ilość:")
                        for amount_type, amount in value.items():
                            print(amount_type + ":", amount)
                    else:
                        print(attribute + ":", value)

    def dodaj(self):
        if(tytul==book_list & autor==book_list):
            book_list.append(tytul, autor, numer)
            

dzial=input("Co chcesz zrobić? \n 1)usunąć książke \n 2)dodać książke \n 3)zobaczyć tytuły \n 4)Wyjść \n")


book_list={
        "Numer 1":{
            "Tytuł":"IT",
            "autor":"nie pamiętam",
            "Ilość":{
                "wypożyczone":4, 
                "dostępne":2, 
                "razem":3
                    }
                    },
        "Numer 2":{
            "Tytuł":"w pustyni i w puszczy", 
            "autor":"nie pamiętam", 
            "Ilość":{
                "wypożyczone":1, 
                "dostępne":2, 
                "razem":3
                    }
                    }, 
        "Numer 3":{
            "Tytuł":"Dziady", 
            "autor":"Mickiewicz",
            "Ilość":{
                "wypożyczone":1, 
                "dostępne":2, 
                "razem":3
                    }
                    }
}

book=Book(book_list)

if(dzial=="2"):
    tytul=input("Tytuł: ")
    autor=input("Autor: ")
    numer=input("IBSN: ")
    
elif(dzial=="3"):
    book.display_info()