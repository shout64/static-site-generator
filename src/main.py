from textnode import *
from htmlnode import *
import shutil
import os


def main():
    copy_static_to_public("static", "public")


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
    pass

main()
