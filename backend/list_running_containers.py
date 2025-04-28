import subprocess

def list_running_containers():
    subprocess.run(["docker", "ps"], check=True)
