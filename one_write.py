import os

fd = os.open(
    "once.txt",
    os.O_WRONLY | os.O_CREAT | os.O_TRUNC,
    0o644
)

os.write(fd, b"A" * 1000)

os.close(fd)
