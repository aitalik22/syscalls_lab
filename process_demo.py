import os
import subprocess # модуль для запуска других программ

print("PID:", os.getpid(), flush=True) # номер текущего процесса

# запускаем команду echo в дочернем процессе и ждём её завершения
subprocess.run(["echo", "Hello from child"], check=True)

print("Работа завершена")
