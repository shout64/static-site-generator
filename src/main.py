from block_markdown import *
from textnode       import *
from htmlnode       import *
import shutil
import os


def main():
    copy_static_to_public("static", "public")
    generate_pages_recursive("content", "template.html", "public")

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
    cwd       = os.getcwd()
    file_path = os.path.join(cwd, markdown)   
    if os.path.isfile(file_path):
        with open(file_path, "r") as file:
            content = file.read()
            if content.startswith("# "):
                header = content.split("\n", 1)
                header = header[0][1:].strip()
                return header
            else:
                raise ValueError(f"File doesn't contain title header\n{file_path}")
    else:
        raise FileNotFoundError(f"THIS AINT A FILE:\n{file_path}")
    
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as file:
        from_content = file.read()

    with open(template_path, "r") as file:
        template_content = file.read()

    md    = markdown_to_html_node(from_content)
    html  = md.to_html()
    title = extract_title(from_path)

    new_html = template_content.replace("{{ Title }}", title)
    new_html = new_html.replace("{{ Content }}", html)

    directory = os.path.dirname(dest_path)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(dest_path, "w") as file:
        file.write(new_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    content = os.listdir(dir_path_content)
    
    for item in content:
        original_path = os.path.join(dir_path_content, item)
        if os.path.isfile(original_path):
            new_path      = os.path.join(dest_dir_path, item.replace(".md", ".html"))
            generate_page(original_path, template_path, new_path)
        else:
            content_path = os.path.join(dir_path_content, item)
            dest_path    = os.path.join(dest_dir_path, item)
            generate_pages_recursive(content_path, template_path, dest_path)

main()
