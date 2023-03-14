from enum import IntEnum

Menu_dni=IntEnum("Menu_dni",{"Poniedziałek":1, "Wtorek":2, "Środa":3, "Czwartek":4, "Piątek":5, "Sobota":6, "Niedziela":7})

print(list(Menu_dni))
wybor=int(input("""Ciekawostka o:
1.Poniedziałek
2.Wtorek
3.Środa
4.Czwartek
5.Piątek
6.Sobota
7.Niedziela
"""))

if(wybor==Menu_dni.Poniedziałek):
    print('W języku angielskim "blue Monday" to idiomatyczny termin oznaczający najbardziej przygnębiający dzień tygodnia.')
if(wybor==Menu_dni.Wtorek):
    print('W wielu krajach, takich jak Hiszpania i Grecja, wtorek jest tradycyjnym dniem, w którym ludzie jedzą tacos lub gyros.')
if(wybor==Menu_dni.Środa):
    print('W języku angielskim "hump day" to termin slangowy oznaczający środę, która jest połową tygodnia.')
if(wybor==Menu_dni.Czwartek):
    print('W hinduizmie, czwartek jest zwykle poświęcony czci boga Guru.')
if(wybor==Menu_dni.Piątek):
    print('W islamie, piątek jest dniem modlitwy, a modlitwa po południu nazywana jest ' "salat al-jumu'ah.")
if(wybor==Menu_dni.Sobota):
    print('W języku angielskim "Saturday" pochodzi od łacińskiego słowa "Saturni dies", co oznacza dzień Saturna, boga rolnictwa w mitologii rzymskiej.')
if(wybor==Menu_dni.Niedziela):
    print('W języku angielskim "Sunday" pochodzi od łacińskiego słowa "Dies Solis", co oznacza dzień słońca, co odzwierciedla wcześniejsze pochodzenie niedzieli jako dnia kultu słonecznego w starożytnych religiach.')