#Napisz program, który poprosi użytkownika o podanie liczby całkowitej 'n' i obliczy sumę liczb od 1 do 'n'.

x=int(input("do ilu cchcesz dodawać: "))
y=0
while 0!=x:
    y=y+x
    x-=1
print(y)