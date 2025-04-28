import tkinter as tk
from tkinter import simpledialog, messagebox

from backend.create_virtual_disk import create_virtual_disk
from backend.create_virtual_machine import create_virtual_machine
from backend.create_dockerfile import create_dockerfile
from backend.build_docker_image import build_docker_image
from backend.list_docker_images import list_docker_images
from backend.list_running_containers import list_running_containers
from backend.stop_container import stop_container
from backend.run_container import run_container

from backend.search_local_images import search_local_images
from backend.search_dockerhub_images import search_dockerhub_images
from backend.pull_docker_image import pull_docker_image



import os
import subprocess

import time

def stop_selected_container(container_id):
    try:
        stop_container(container_id)
        messagebox.showinfo("Success", f"Container {container_id} stopped successfully!")
        time.sleep(0.5)  # short pause
    except Exception as e:
        messagebox.showerror("Error", str(e))


# ================= Backend Call Wrappers for GUI ====================

def create_virtual_disk_gui():
    disk_name = simpledialog.askstring("Disk Name", "Enter disk name:")
    disk_size = simpledialog.askstring("Disk Size", "Enter disk size (e.g., 10G):")
    disk_format = simpledialog.askstring("Disk Format", "Enter disk format (qcow2/raw):")
    if disk_name and disk_size and disk_format:
        try:
            create_virtual_disk(disk_name, disk_size, disk_format)
            messagebox.showinfo("Success", f"Disk '{disk_name}.{disk_format}' created!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

def create_virtual_machine_gui():
    vm_name = simpledialog.askstring("VM Name", "Enter VM name:")
    disk_file = simpledialog.askstring("Disk File", "Enter disk file name (e.g., mydisk.qcow2):")
    memory = simpledialog.askstring("Memory", "Enter memory in MB (e.g., 2048):")
    cpu = simpledialog.askstring("CPU", "Enter number of CPUs:")
    if vm_name and disk_file and memory and cpu:
        try:
            create_virtual_machine(vm_name, disk_file, memory, cpu)
            messagebox.showinfo("Success", f"VM '{vm_name}' started!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

def create_dockerfile_gui():
    path = simpledialog.askstring("Folder Path", "Enter folder path to save Dockerfile:")
    content = simpledialog.askstring("Dockerfile Content", "Enter Dockerfile content (e.g., FROM ubuntu):")
    if path and content:
        try:
            create_dockerfile(path, content)
            messagebox.showinfo("Success", "Dockerfile created!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

def build_docker_image_gui():
    path = simpledialog.askstring("Dockerfile Path", "Enter folder path where Dockerfile is saved:")
    image_name = simpledialog.askstring("Image Name", "Enter Docker image name (e.g., myubuntuimage):")
    if path and image_name:
        try:
            build_docker_image(path, image_name)
            messagebox.showinfo("Success", f"Docker image '{image_name}' built!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

def list_docker_images_gui():
    try:
        list_docker_images()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def list_running_containers_gui():
    try:
        list_running_containers()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def stop_container_gui():
    container_id = simpledialog.askstring("Container ID/Name", "Enter container ID or name to stop:")
    if container_id:
        try:
            stop_container(container_id)
            messagebox.showinfo("Success", f"Container '{container_id}' stopped!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

def run_container_gui():
    image_name = simpledialog.askstring("Image Name", "Enter image name to run:")
    container_name = simpledialog.askstring("Container Name", "Enter container name (optional):")
    if image_name:
        try:
            run_container(image_name, container_name)
            messagebox.showinfo("Success", f"Container started from '{image_name}'!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            
            
  


# ================= Welcome Window ====================

def open_main_window():
    welcome_window.withdraw()

    main_window = tk.Toplevel()
    main_window.title("Cloud Management System 🚀")
    main_window.geometry("950x750")
    main_window.configure(bg="#f0f8ff")

    title = tk.Label(main_window, text="Select a Service", font=("Poppins", 20, "bold"), bg="#f0f8ff")
    title.pack(pady=20)

    # Main Menu Frame
    menu_frame = tk.Frame(main_window, bg="#f0f8ff")
    menu_frame.pack()
    
    left_frame = tk.Frame(menu_frame, bg="#f0f8ff")
    center_frame = tk.Frame(menu_frame, bg="#f0f8ff")
    right_frame = tk.Frame(menu_frame, bg="#f0f8ff")

    left_frame.grid(row=0, column=0, padx=10, pady=5)
    center_frame.grid(row=0, column=1, padx=10, pady=5)
    right_frame.grid(row=0, column=2, padx=10, pady=5)
    
  
    
    def search_local_images_gui():
        show_search_local_form()

    def search_dockerhub_images_gui():
        show_search_dockerhub_form()

    def pull_docker_image_gui():
        show_pull_image_form()

    
   

    button_style = {
        "font": ("Segoe UI", 12),
        "width": 30,
        "bg": "#e6f2ff",
        "activebackground": "#cce6ff",
        "bd": 2,
        "relief": "raised"
    }

    # Define Switch Functions
    def show_create_disk_form():
        menu_frame.pack_forget()
        create_disk_frame.pack(pady=20)

    def show_create_vm_form():
        menu_frame.pack_forget()
        create_vm_frame.pack(pady=20)

    def show_create_dockerfile_form():
        menu_frame.pack_forget()
        create_dockerfile_frame.pack(pady=20)

    def show_build_docker_image_form():
        menu_frame.pack_forget()
        build_docker_image_frame.pack(pady=20)
        
    def show_search_local_form():
        menu_frame.pack_forget()
        search_local_frame.pack(pady=20)

    def show_search_dockerhub_form():
        menu_frame.pack_forget()
        search_dockerhub_frame.pack(pady=20)

    def show_pull_image_form():
        menu_frame.pack_forget()
        pull_image_frame.pack(pady=20)



    def list_images_action():
        try:
            # Get list of images
            output = subprocess.check_output(["docker", "images", "--format", "{{.Repository}}:{{.Tag}}"], text=True)
            images = output.strip().split('\n')

            # Create popup window
            popup = tk.Toplevel()
            popup.title("Docker Images")
            popup.geometry("400x400")
            popup.configure(bg="#f0f8ff")

            tk.Label(popup, text="Docker Images:", font=("Poppins", 16), bg="#f0f8ff").pack(pady=10)

            for img in images:
                if img:  # avoid empty lines
                    tk.Label(popup, text=img, font=("Segoe UI", 12), bg="#f0f8ff").pack()

            tk.Button(popup, text="Close", command=popup.destroy, font=("Segoe UI", 12)).pack(pady=20)

        except Exception as e:
            messagebox.showerror("Error", str(e))


    def list_running_containers_action():
        try:
            output = subprocess.check_output(["docker", "ps", "--format", "{{.ID}}: {{.Image}}"], text=True)
            containers = output.strip().split('\n')

            popup = tk.Toplevel()
            popup.title("Running Containers")
            popup.geometry("400x400")
            popup.configure(bg="#f0f8ff")

            tk.Label(popup, text="Running Containers:", font=("Poppins", 16), bg="#f0f8ff").pack(pady=10)

            for cont in containers:
                if cont:
                    tk.Label(popup, text=cont, font=("Segoe UI", 12), bg="#f0f8ff").pack()

            tk.Button(popup, text="Close", command=popup.destroy, font=("Segoe UI", 12)).pack(pady=20)

        except Exception as e:
            messagebox.showerror("Error", str(e))


    def show_stop_container_form():
        menu_frame.pack_forget()

        try:
            output = subprocess.check_output(["docker", "ps", "--format", "{{.ID}}: {{.Image}}"], text=True)
            containers = output.strip().split('\n')

            stop_popup = tk.Toplevel()
            stop_popup.title("Stop a Container")
            stop_popup.geometry("500x500")
            stop_popup.configure(bg="#f0f8ff")

            tk.Label(stop_popup, text="Click 'Stop' to stop a container:", font=("Poppins", 16), bg="#f0f8ff").pack(pady=10)

            for cont in containers:
                if cont:
                    parts = cont.split(':')
                    container_id = parts[0].strip()

                    frame = tk.Frame(stop_popup, bg="#f0f8ff")
                    frame.pack(pady=2)

                    tk.Label(frame, text=cont, font=("Segoe UI", 12), bg="#f0f8ff").pack(side="left")
                    tk.Button(frame, text="Stop", font=("Segoe UI", 10), command=lambda c=container_id: stop_selected_container(c)).pack(side="right")

            tk.Button(stop_popup, text="Close", font=("Segoe UI", 12), command=lambda: (stop_popup.destroy(), menu_frame.pack())).pack(pady=20)

        except Exception as e:
            messagebox.showerror("Error", str(e))
            menu_frame.pack()

 


    def show_run_container_form():
        menu_frame.pack_forget()

        try:
            output = subprocess.check_output(["docker", "images", "--format", "{{.Repository}}:{{.Tag}}"], text=True)
            images = output.strip().split('\n')

            run_popup = tk.Toplevel()
            run_popup.title("Run a Container")
            run_popup.geometry("400x400")
            run_popup.configure(bg="#f0f8ff")

            tk.Label(run_popup, text="Click 'Run' to start a container from image:", font=("Poppins", 16), bg="#f0f8ff").pack(pady=10)

            for img in images:
                if img:
                    frame = tk.Frame(run_popup, bg="#f0f8ff")
                    frame.pack(pady=2)

                    tk.Label(frame, text=img, font=("Segoe UI", 12), bg="#f0f8ff").pack(side="left")
                    tk.Button(frame, text="Run", font=("Segoe UI", 10), command=lambda i=img: run_selected_image(i)).pack(side="right")

            tk.Button(run_popup, text="Close", font=("Segoe UI", 12), command=lambda: (run_popup.destroy(), menu_frame.pack())).pack(pady=20)

        except Exception as e:
            messagebox.showerror("Error", str(e))
            menu_frame.pack()

    def run_selected_image(image_name):
        try:
            run_container(image_name)
            messagebox.showinfo("Success", f"Container started from {image_name} successfully!")
            time.sleep(0.5)  # short pause
        except Exception as e:
            messagebox.showerror("Error", str(e))


    # --- Main Menu Buttons ---
    menu_buttons = [
        ("💽 Create Virtual Disk", show_create_disk_form),
        ("💻 Create Virtual Machine", show_create_vm_form),
        ("📝 Create Dockerfile", show_create_dockerfile_form),
        ("🏗️ Build Docker Image", show_build_docker_image_form),
        ("🖼️ List Docker Images", list_images_action),
        ("📦 List Running Containers", list_running_containers_action),
        ("⛔ Stop a Container", show_stop_container_form),
        ("🏃 Run a Container", show_run_container_form),
        ("🔍 Search Local Images", show_search_local_form),
        ("🌐 Search DockerHub Images", show_search_dockerhub_form),
        ("⬇️ Pull Docker Image", show_pull_image_form),
        ("🚪 Exit", lambda: (main_window.destroy(), welcome_window.destroy()))
    ]
    
    # Put them in a 3-column grid
    for index, (text, command) in enumerate(menu_buttons):
        row = index % 4
        column = index // 4
        tk.Button(menu_frame, text=text, command=command, **button_style).grid(row=row, column=column, padx=10, pady=10, ipady=5)

    # ----------------- Individual Frames -----------------

    # Create Disk Frame
    create_disk_frame = tk.Frame(main_window, bg="#f0f8ff")
    tk.Label(create_disk_frame, text="Create Virtual Disk", font=("Poppins", 18), bg="#f0f8ff").pack(pady=10)

    tk.Label(create_disk_frame, text="Disk Name:", font=("Segoe UI", 12), bg="#f0f8ff").pack()
    disk_name_entry = tk.Entry(create_disk_frame, font=("Segoe UI", 12))
    disk_name_entry.pack(pady=5)

    tk.Label(create_disk_frame, text="Disk Size (e.g., 5G):", font=("Segoe UI", 12), bg="#f0f8ff").pack()
    disk_size_entry = tk.Entry(create_disk_frame, font=("Segoe UI", 12))
    disk_size_entry.pack(pady=5)

    tk.Label(create_disk_frame, text="Disk Format (qcow2/raw):", font=("Segoe UI", 12), bg="#f0f8ff").pack()
    disk_format_entry = tk.Entry(create_disk_frame, font=("Segoe UI", 12))
    disk_format_entry.pack(pady=5)

    def submit_create_disk():
        disk_name = disk_name_entry.get()
        disk_size = disk_size_entry.get()
        disk_format = disk_format_entry.get()
        if disk_name and disk_size and disk_format:
            try:
                create_virtual_disk(disk_name, disk_size, disk_format)
                messagebox.showinfo("Success", "Virtual Disk Created Successfully!")
                create_disk_frame.pack_forget()
                menu_frame.pack()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    tk.Button(create_disk_frame, text="Create", command=submit_create_disk, **button_style).pack(pady=10)
    tk.Button(create_disk_frame, text="Back to Menu", command=lambda: (create_disk_frame.pack_forget(), menu_frame.pack()), **button_style).pack()

    # --- Create VM Frame ---
    create_vm_frame = tk.Frame(main_window, bg="#f0f8ff")
    tk.Label(create_vm_frame, text="Create Virtual Machine", font=("Poppins", 18), bg="#f0f8ff").pack(pady=10)

    tk.Label(create_vm_frame, text="VM Name:", font=("Segoe UI", 12), bg="#f0f8ff").pack()
    vm_name_entry = tk.Entry(create_vm_frame, font=("Segoe UI", 12))
    vm_name_entry.pack(pady=5)

    tk.Label(create_vm_frame, text="Disk File (e.g., mydisk.qcow2):", font=("Segoe UI", 12), bg="#f0f8ff").pack()
    disk_file_entry = tk.Entry(create_vm_frame, font=("Segoe UI", 12))
    disk_file_entry.pack(pady=5)

    tk.Label(create_vm_frame, text="Memory (MB):", font=("Segoe UI", 12), bg="#f0f8ff").pack()
    memory_entry = tk.Entry(create_vm_frame, font=("Segoe UI", 12))
    memory_entry.pack(pady=5)

    tk.Label(create_vm_frame, text="Number of CPUs:", font=("Segoe UI", 12), bg="#f0f8ff").pack()
    cpu_entry = tk.Entry(create_vm_frame, font=("Segoe UI", 12))
    cpu_entry.pack(pady=5)

    def submit_create_vm():
        vm_name = vm_name_entry.get()
        disk_file = disk_file_entry.get()
        memory = memory_entry.get()
        cpu = cpu_entry.get()
        if vm_name and disk_file and memory and cpu:
            try:
                create_virtual_machine(vm_name, disk_file, memory, cpu)
                messagebox.showinfo("Success", "Virtual Machine Started Successfully!")
                create_vm_frame.pack_forget()
                menu_frame.pack()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    tk.Button(create_vm_frame, text="Create", command=submit_create_vm, **button_style).pack(pady=10)
    tk.Button(create_vm_frame, text="Back to Menu", command=lambda: (create_vm_frame.pack_forget(), menu_frame.pack()), **button_style).pack()

    # --- Create Dockerfile Frame ---
    create_dockerfile_frame = tk.Frame(main_window, bg="#f0f8ff")
    tk.Label(create_dockerfile_frame, text="Create Dockerfile", font=("Poppins", 18), bg="#f0f8ff").pack(pady=10)

    tk.Label(create_dockerfile_frame, text="Folder Path:", font=("Segoe UI", 12), bg="#f0f8ff").pack()
    dockerfile_path_entry = tk.Entry(create_dockerfile_frame, font=("Segoe UI", 12))
    dockerfile_path_entry.pack(pady=5)

    tk.Label(create_dockerfile_frame, text="Dockerfile Content (e.g., FROM ubuntu):", font=("Segoe UI", 12), bg="#f0f8ff").pack()
    dockerfile_content_entry = tk.Entry(create_dockerfile_frame, font=("Segoe UI", 12))
    dockerfile_content_entry.pack(pady=5)

    def submit_create_dockerfile():
        path = dockerfile_path_entry.get()
        content = dockerfile_content_entry.get()
        if path and content:
            try:
                create_dockerfile(path, content)
                messagebox.showinfo("Success", "Dockerfile Created Successfully!")
                create_dockerfile_frame.pack_forget()
                menu_frame.pack()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    tk.Button(create_dockerfile_frame, text="Create", command=submit_create_dockerfile, **button_style).pack(pady=10)
    tk.Button(create_dockerfile_frame, text="Back to Menu", command=lambda: (create_dockerfile_frame.pack_forget(), menu_frame.pack()), **button_style).pack()


   
    
    # --- Build Docker Image Frame ---
    build_docker_image_frame = tk.Frame(main_window, bg="#f0f8ff")
    tk.Label(build_docker_image_frame, text="Build Docker Image", font=("Poppins", 18), bg="#f0f8ff").pack(pady=10)

    tk.Label(build_docker_image_frame, text="Folder Path (where Dockerfile is):", font=("Segoe UI", 12), bg="#f0f8ff").pack()
    build_path_entry = tk.Entry(build_docker_image_frame, font=("Segoe UI", 12))
    build_path_entry.pack(pady=5)

    tk.Label(build_docker_image_frame, text="Image Name:", font=("Segoe UI", 12), bg="#f0f8ff").pack()
    image_name_entry = tk.Entry(build_docker_image_frame, font=("Segoe UI", 12))
    image_name_entry.pack(pady=5)

    def submit_build_docker_image():
        path = build_path_entry.get()
        image_name = image_name_entry.get()
        if path and image_name:
            try:
                build_docker_image(path, image_name)
                messagebox.showinfo("Success", "Docker Image Built Successfully!")
                build_docker_image_frame.pack_forget()
                menu_frame.pack()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    tk.Button(build_docker_image_frame, text="Build", command=submit_build_docker_image, **button_style).pack(pady=10)
    tk.Button(build_docker_image_frame, text="Back to Menu", command=lambda: (build_docker_image_frame.pack_forget(), menu_frame.pack()), **button_style).pack()

    # --- Search Local Images Frame ---
    search_local_frame = tk.Frame(main_window, bg="#f0f8ff")
    tk.Label(search_local_frame, text="Search Local Docker Images", font=("Poppins", 18), bg="#f0f8ff").pack(pady=10)

    tk.Label(search_local_frame, text="Enter local image name:", font=("Segoe UI", 12), bg="#f0f8ff").pack()
    local_query_entry = tk.Entry(search_local_frame, font=("Segoe UI", 12))
    local_query_entry.pack(pady=5)

    
    

    def submit_search_local():
        query = local_query_entry.get()
        if query:
            try:
                results = search_local_images(query)
                result_text = "\n".join(results) if results else "No matching images found."
                messagebox.showinfo("Search Results", result_text)
                search_local_frame.pack_forget()
                menu_frame.pack()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    tk.Button(search_local_frame, text="Search", command=submit_search_local, **button_style).pack(pady=10)
    tk.Button(search_local_frame, text="Back to Menu", command=lambda: (search_local_frame.pack_forget(), menu_frame.pack()), **button_style).pack()


# --- Search DockerHub Images Frame ---
    search_dockerhub_frame = tk.Frame(main_window, bg="#f0f8ff")
    tk.Label(search_dockerhub_frame, text="Search DockerHub Images", font=("Poppins", 18), bg="#f0f8ff").pack(pady=10)

    tk.Label(search_dockerhub_frame, text="Enter DockerHub Search Query (e.g., nginx):", font=("Segoe UI", 12), bg="#f0f8ff").pack()

    dockerhub_query_entry = tk.Entry(search_dockerhub_frame, font=("Segoe UI", 12))
    dockerhub_query_entry.pack(pady=5)

    def submit_search_dockerhub():
        query = dockerhub_query_entry.get()
        if query:
            try:
                output = search_dockerhub_images(query)
                messagebox.showinfo("Search Results", output)
                search_dockerhub_frame.pack_forget()
                menu_frame.pack()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    tk.Button(search_dockerhub_frame, text="Search", command=submit_search_dockerhub, **button_style).pack(pady=10)
    tk.Button(search_dockerhub_frame, text="Back to Menu", command=lambda: (search_dockerhub_frame.pack_forget(), menu_frame.pack()), **button_style).pack()

    # --- Pull Docker Image Frame ---
    pull_image_frame = tk.Frame(main_window, bg="#f0f8ff")
    tk.Label(pull_image_frame, text="Pull Docker Image", font=("Poppins", 18), bg="#f0f8ff").pack(pady=10)

    tk.Label(pull_image_frame, text="Enter Image Name to Pull (e.g., nginx:latest):", font=("Segoe UI", 12), bg="#f0f8ff").pack()

    pull_query_entry = tk.Entry(pull_image_frame, font=("Segoe UI", 12))
    pull_query_entry.pack(pady=5)

    def submit_pull_image():
        image_name = pull_query_entry.get()
        if image_name:
            loading_popup = tk.Toplevel()
            loading_popup.title("Downloading...")
            loading_popup.geometry("300x100")
            tk.Label(loading_popup, text="Downloading image, please wait...").pack(pady=20)
            loading_popup.update()
            try:
                pull_docker_image(image_name)
                loading_popup.destroy()
                messagebox.showinfo("Success", "Docker Image Pulled Successfully!")
            except subprocess.CalledProcessError:
                loading_popup.destroy()
                messagebox.showerror("Error", "Docker Engine not running. Please start Docker.")
            except Exception as e:
                loading_popup.destroy()
                messagebox.showerror("Error", str(e))


    tk.Button(pull_image_frame, text="Pull", command=submit_pull_image, **button_style).pack(pady=10)
    tk.Button(pull_image_frame, text="Back to Menu", command=lambda: (pull_image_frame.pack_forget(), menu_frame.pack()), **button_style).pack()

 
    main_window.mainloop()

# --- Welcome Window ---
welcome_window = tk.Tk()
welcome_window.title("Welcome 🚀")
welcome_window.geometry("400x300")
welcome_window.configure(bg="#e0ffff")

welcome_label = tk.Label(welcome_window, text="Welcome to\nCloud Management System!", font=("Helvetica", 18, "bold"), bg="#e0ffff")
welcome_label.pack(pady=50)

tk.Button(welcome_window, text="Dive In", font=("Helvetica", 12), command=open_main_window, padx=20, pady=10).pack(pady=10)
tk.Button(welcome_window, text="Exit", font=("Helvetica", 12), command=welcome_window.destroy, padx=20, pady=10).pack()

welcome_window.mainloop()
