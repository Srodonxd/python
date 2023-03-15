import os
from enum import IntEnum

components=IntEnum('components',{'CPU':1,'Motherboard':2,'BIOS':3, 'RAM':4, 'Graphics':5})
print(list(components))

wybor=int(input("""Co byś chciał zobaczyć?:
1)Procesor
2)Płyta główna
3)BIOS
4)RAM
5)Karta grafizcna
"""))

if(wybor==components.CPU):
    os.system('wmic cpu get name, family, maxclockspeed, l2cachesize, numberoflogicalprocessors, numberofcores')
elif(wybor==components.Motherboard):
    os.system('')
elif(wybor==components.BIOS):
    os.system('wmic bios get name, version, releasedate')
elif(wybor==components.RAM):
    os.system('')
elif(wybor==components.Graphics):
    os.system('')