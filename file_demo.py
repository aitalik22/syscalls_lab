import os

fd = os.open(
    "data.txt",
    os.O_WRONLY | os.O_CREAT | os.O_TRUNC,
    0o644
)
print("Дескриптор файла:", fd)

os.write(fd, b"Hello, Linux!\n")
os.close(fd)
print("Файл закрыт")

