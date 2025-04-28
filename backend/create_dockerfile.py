import os

def create_dockerfile(path, content):
    full_path = os.path.join(path, "Dockerfile")
    with open(full_path, "w") as f:
        f.write(content)
