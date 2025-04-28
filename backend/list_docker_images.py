import subprocess

def list_docker_images():
    subprocess.run(["docker", "images"], check=True)
