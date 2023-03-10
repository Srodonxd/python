# Napisz program, który będzie służył do zliczania ilości wystąpień poszczególnych słów w podanym 
# przez użytkownika tekście. Program powinien składać się z dwóch funkcji:

# Funkcja count_words(text: str) -> dict, która przyjmie jako argument tekst i zwróci słownik, 
# w którym kluczami będą poszczególne słowa występujące w tekście, a wartościami ilość ich wystąpień.

# Funkcja print_word_counts(word_counts: dict) -> None, która przyjmie jako argument słownik z ilością 
# wystąpień słów i wypisze na ekranie listę słów wraz z ich ilością wystąpień, posortowaną alfabetycznie.

count={}
class Text:
    def count_words(self, text_input):
        split_text=str(text_input.split(" "))
        print(split_text)
        return

    def print_words_counts(self, text_input):
        for word in text_input():
            if word in count:
                count[word]+=1
            else:
                count[word]=1
            

for element, ilosc in count.items():
    print(f"słowo {element} występuje {ilosc} razy")        


text=Text()
text_input=input("Wpisz tekst: ")

text.count_words(text_input)
text.print_words_counts(text_input)
