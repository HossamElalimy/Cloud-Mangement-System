import subprocess

def search_dockerhub_images(query):
    try:
        output = subprocess.check_output(["docker", "search", query], text=True)
        return output
    except subprocess.CalledProcessError as e:
        raise Exception(f"Failed to search DockerHub: {str(e)}")
