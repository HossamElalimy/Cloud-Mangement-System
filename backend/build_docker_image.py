import subprocess

def build_docker_image(path, image_name):
    command = ["docker", "build", "-t", image_name, path]
    subprocess.run(command, check=True)
