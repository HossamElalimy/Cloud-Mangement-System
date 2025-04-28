import subprocess

def search_local_images(query):
    try:
        output = subprocess.check_output(["docker", "images", "--format", "{{.Repository}}:{{.Tag}}"], text=True)
        images = output.strip().split('\n')
        matches = [img for img in images if query.lower() in img.lower()]
        return matches
    except subprocess.CalledProcessError as e:
        raise Exception(f"Failed to search local images: {str(e)}")
