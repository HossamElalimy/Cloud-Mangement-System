import subprocess

def create_virtual_disk(disk_name, disk_size, disk_format):
    command = ["qemu-img", "create", "-f", disk_format, f"{disk_name}.{disk_format}", disk_size]
    subprocess.run(command, check=True)
