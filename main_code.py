import subprocess

# Lance 'autre.py' dans un nouveau processus Python
for loop in range(10):
    subprocess.run(["python", "test_ping.py"])