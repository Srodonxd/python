#Znajdź liczby od 100 do 470 włącznie, zkóre są podzielne przez 7, ale nie są podzielne przez 5

liczby=(
    element 
    for element in range(100,470)
    if (element % 7 ==0)
    if (element % 5 !=0)
)

print(liczby)