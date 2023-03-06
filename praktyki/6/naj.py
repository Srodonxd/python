#napisz funkcję, która przyjmuje listę liczb i zwraca największą liczbę w tej liście
i=0
x=[]
while i != 5:
    y=float(input())
    x.append(y)
    i+=1
x.sort(reverse=True)
print(x[0])