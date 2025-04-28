import subprocess

def stop_container(container_id_or_name):
    command = ["docker", "stop", container_id_or_name]
    subprocess.run(command, check=True)
