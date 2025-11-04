from textnode import *
from htmlnode import *
import shutil
import os


def main():
    copy_static_to_public("static", "public")
    extract_title("content/index.md")


def copy_static_to_public(src, dst):
    cwd         = os.getcwd()
    source_path = os.path.join(cwd, src)
    dest_path   = os.path.join(cwd, dst)
    
    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)
    
    os.mkdir(dst)

    files_to_copy = os.listdir(source_path)
    for item in files_to_copy:
        original_file_path = os.path.join(source_path, item)
        copied_file_path = os.path.join(dest_path, item)

        if os.path.isfile(original_file_path):
            shutil.copy(original_file_path, copied_file_path)
        else:
            copy_static_to_public(os.path.join(src, item), os.path.join(dst, item))

def extract_title(markdown):
    cwd         = os.getcwd()
    file_path = os.path.join(cwd, markdown)   
    if os.path.isfile(file_path):
        with open(file_path, "r") as file:
            content = file.read()
            if content.startswith("# "):
                header = content.split("\n", 1)
                header = header[0][1:].strip()
                print(header)
                return header
            else:
                raise ValueError(f"File doesn't contain title header\n{file_path}")
    else:
        raise FileNotFoundError(f"THIS AINT A FILE:\n{file_path}")
    
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

main()
