import os
fd = os.open("data.txt", os.O_RDONLY) # открываем только для чтения
data = os.read(fd, 100) # читаем не более 100 байтов
print(data.decode("utf-8")) # превращаем байты в текст
os.close(fd)

