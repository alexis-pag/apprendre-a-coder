import subprocess
from pythonping import ping
# Ouvre un nouveau terminal CMD
for loop in range(1):
        subprocess.run('start cmd /k "ping localhost -n 10000000"', shell=True)
