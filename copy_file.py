import os

# Открываем исходный файл для чтения
src = os.open("data.txt", os.O_RDONLY)
# Открываем/создаём файл назначения для записи
dst = os.open("copy.txt", os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)

while True:
    # Читаем не более 1024 байт
    block = os.read(src, 1024)
    
    # Если прочитали 0 байт — достигнут конец файла
    if not block:
        break
        
    # Записываем прочитанный блок. 
    # Вдруг os.write() запишет меньше, чем мы ему дали? 
    # Поэтому крутимся в цикле, пока не запишем всё, что прочитали.
    while block:
        n = os.write(dst, block)
        # Отбрасываем ту часть блока, которую уже успешно записали
        block = block[n:]

# Закрываем оба дескриптора
os.close(src)
os.close(dst)
