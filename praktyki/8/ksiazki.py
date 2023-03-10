"""Napisz program, który będzie przechowywał informacje o książkach w bibliotece.
 Utwórz klasę 'Book', która będzie miała atrybuty 'title', 'author' oraz 'isbn'. 
 Następnie utwórz listę obiektów klasy 'Book', a w programie umożliw użytkownikowi dodawanie, usuwanie i wyświetlanie informacji o książkach z tej listy."""

class Book:
    def __init__(self, book_list):
        self.book_list=book_list
    
    def display_info(self):
        for book_info in self.book_list:
            print()    
            print("Tytuł:",book_info["Tytuł"])
            print("Autor:",book_info["Autor"])
            for attribute, value in book_info["Ilość"].items():
                print(attribute + ":", value)
        return f"Ilosc ksiazek wynosi: {len(self.book_list)}"
    
    def dodaj(self, nowe, tytul, autor):
        ilosc=0
        exists = False
        for item in self.book_list:
            if tytul == item['Tytuł'] and autor == item["Autor"]:
                exists = True
                ilosc = item['Ilość']['Dostepne']
                item['ilość']['razem'] += nowe['ilość']['razem']
                item['ilość']['dostepne'] += nowe['ilość']['razem']
                return True
        if not exists:
            self.book_list.append(nowe)
        return False
    
    def usun(self, tytul):
        ilosc=0
        for element in self.book_list:
            for  item in element.values():
                if(tytul in item):
                    print(ilosc)
                    self.book_list.pop(ilosc)
            ilosc+=1

dzial=input("Co chcesz zrobić? \n 1)usunąć książke \n 2)dodać książke \n 3)zobaczyć tytuły \n 4)Wyjść \n")

book_list_pre=[
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
    print(book_list_pre)
    book.dodaj(nowe, tytul, autor)
    print(book_list_pre)
elif(dzial=="3"):
    book.display_info()

# for book_info in book_list_pre:
#     print()   
#     print("Tytuł:",book_info["Tytuł"])
#     print("Autor:",book_info["Autor"])
#     for attribute, value in book_info["Ilość"].items():
#         print(attribute + ":", value)