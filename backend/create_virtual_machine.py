import subprocess

def create_virtual_machine(vm_name, disk_file, memory, cpu):
    command = [
        "qemu-system-x86_64",
        "-m", memory,
        "-smp", cpu,
        "-hda", disk_file,
        "-boot", "order=c",
        "-name", vm_name
    ]
    subprocess.Popen(command)
