import os

fd = os.open(
    "many.txt",
    os.O_WRONLY | os.O_CREAT | os.O_TRUNC,
    0o644
)

for i in range(1000):
    os.write(fd, b"A")

os.close(fd)
