import sys
import time

start=time.perf_counter()
#Zapisuje dane w pamięci
evenNumbers=[element
             for element in range (400)
             if (element % 2 == 0)
             ]

#Generuje dane
evenNumbersGenerator=(element
                      for element in range (400)
                      if (element % 2 == 0)
                      )

print(sys.getsizeof(evenNumbers))
print(sys.getsizeof(evenNumbersGenerator))

end=time.perf_counter()
print(end-start)


names= {"Arkadiusz", "Wioletta", "Karol", "Bartłomiej", "Jakub", "Ania"}

namesLenght = {
    name : len(name)
    for name in names
    if name.startswith("A")
}
print(namesLenght)


numbers=[1, 2, 3, 4, 5, 6]
multipliednumbers = {
    number : number*number
    for number in numbers
}
print(multipliednumbers)

celsius = {"t1":-20, "t2":-15, "t3":0, "t4":12, "t5":24}
fahrenheit={
    key:celsius*1.8 + 32
    for key,celsius in celsius.items()
    if celsius > -5
    if celsius < 20
}
print(fahrenheit)