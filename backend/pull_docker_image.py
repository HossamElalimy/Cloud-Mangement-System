import subprocess

def pull_docker_image(image_name):
    try:
        subprocess.run(["docker", "pull", image_name], check=True)
        return True
    except subprocess.CalledProcessError as e:
        raise Exception(f"Failed to pull image: {str(e)}")
