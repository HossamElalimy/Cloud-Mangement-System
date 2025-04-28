import subprocess

def run_container(image_name, container_name=None):
    command = ["docker", "run", "-d"]
    if container_name:
        command += ["--name", container_name]
    command.append(image_name)
    subprocess.run(command, check=True)
