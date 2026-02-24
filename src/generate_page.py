import os
from markdown_to_html_node import *
from extract_title import extract_title


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from '{from_path}' to '{dest_path}' using '{template_path}'")
    with open(from_path, 'r') as f:
        markdown = f.read() # In Python, `markdown` is accessible outside of `with open` statement
    with open(template_path, 'r') as f:
        template = f.read()
    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace('{{ Title }}', title).replace('{{ Content }}', content)

    dest_folder_path = os.path.join(*dest_path.split('/')[:-1])

    if not os.path.exists(dest_folder_path):
        os.makedirs(dest_folder_path)

    with open(dest_path, 'w') as f:
        f.write(template)

