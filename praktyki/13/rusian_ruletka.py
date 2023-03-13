import random 
x=money_totality=0
b=1
list=[]

group=int(input("Ile osób bierze udział?(MAKS 6 OSÓB): "))

print("Podaj imiona oraz ich zakład")
while x!=group:
    new=input(f"{x+1}: ")
    money=int(input("Ile PLN?: "))
    list.append(new)
    money_totality+=money
    x+=1

while group!=1:
    death=random.randint(1,group)
    while x!=7:
        if x!=death:
            print(f"Runda {b}: {list[death-1]} Odpadł/a :(")
            list.pop(death-1)
            break
        else:
            x+=1
    group-=1
    b+=1
print(f"Brawo! Zwycięscą jest {list[0]} i wygrywa {money_totality} PLN!!")