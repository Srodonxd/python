"""Napisz program, który będzie przechowywał informacje o książkach w bibliotece.
 Utwórz klasę 'Book', która będzie miała atrybuty 'title', 'author' oraz 'isbn'. 
 Następnie utwórz listę obiektów klasy 'Book', a w programie umożliw użytkownikowi dodawanie, usuwanie i wyświetlanie informacji o książkach z tej listy."""
ilosc=0
class Book:
    def __init__(self, book_list):
        self.book_list=book_list
    
    def display_info(self):
        for book_number, book_info in book_list.items():
            print()
            print(book_number)    
            print("Tytuł:",book_info["Tytuł"])
            print("Autor:",book_info["Autor"])
            for attribute, value in book_info["Ilość"].items():
                print(attribute + ":", value)
    
    def dodaj(self):
        if(tytul==book_list["Tytuł"] & autor==book_list["Autor"]):
            book_list.update ({"Numer":{"Tytuł":tytul, "Autor":autor, "Ilość":numer}})
        else:
            ilosc+=1
            

dzial=input("Co chcesz zrobić? \n 1)usunąć książke \n 2)dodać książke \n 3)zobaczyć tytuły \n 4)Wyjść \n")


book_list={
        "Numer 1":{
            "Tytuł":"IT",
            "Autor":"nie pamiętam",
            "Ilość":{
                "wypożyczone":2, 
                "dostępne":3, 
                "razem":ilosc
                    }
                    },
        "Numer 2":{
            "Tytuł":"w pustyni i w puszczy", 
            "Autor":"nie pamiętam", 
            "Ilość":{
                "wypożyczone":1, 
                "dostępne":2, 
                "razem":3
                    }
                    }, 
        "Numer 3":{
            "Tytuł":"Dziady", 
            "Autor":"Mickiewicz",
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
    numer=input("Ile: ")
    
elif(dzial=="3"):
    book.display_info()

for book_number, book_info in book_list.items():
            print()
            print(book_number)    
            print("Tytuł:",book_info["Tytuł"])
            print("Autor:",book_info["Autor"])
            for attribute, value in book_info["Ilość"].items():
                print(attribute + ":", value)