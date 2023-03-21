import wmi

w = wmi.WMI()

for processor in w.Win32_Processor():
    print("Procesor:")
    print(f"- Nazwa: {processor.Name}")
    print(f"- Ilość rdzeni: {processor.NumberOfCores}")
    print(f"- Maksymalna częstotliwość: {processor.MaxClockSpeed} MHz")

for gpu in w.Win32_VideoController():
    print("Karta graficzna:")
    print(f"- Nazwa: {gpu.Name}")
    print(f"- Pamięć wideo: {gpu.AdapterRAM / 1024 / 1024:.2f} MB")

for mem in w.Win32_PhysicalMemory():
    print("Pamięć RAM:")
    capacity_mb = int(mem.Capacity) / 1024 / 1024
    print(f"- Producent: {mem.Manufacturer}")
    print(f"- Pojemność: {capacity_mb:.2f} MB")

for disk in w.Win32_DiskDrive():
    print("Dysk twardy:")
    print(f"- Model: {disk.Model}")
    print(f"- Pojemność: {disk.Size / 1024 / 1024 / 1024:.2f} GB")
