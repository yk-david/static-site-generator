import os
from markdown_to_html_node import *
from extract_title import extract_title


def generate_page(from_path, template_path, dest_path, base_path):    
    print(f"Generating page from '{from_path}' to '{dest_path}' using '{template_path}'")
    with open(from_path, 'r') as f:
        markdown = f.read() # In Python, `markdown` is accessible outside of `with open` statement
    with open(template_path, 'r') as f:
        template = f.read()
    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace('{{ Title }}', title).replace('{{ Content }}', content).replace('href="/', f'href="{base_path}').replace('src="/', f'src="{base_path}')

    dest_folder_path = os.path.join(*dest_path.split('/')[:-1])

    if not os.path.exists(dest_folder_path):
        os.makedirs(dest_folder_path)

    with open(dest_path, 'w') as f:
        f.write(template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path):
    contents = os.listdir(dir_path_content)

    for item in contents:
        current_item_path = os.path.join(dir_path_content, item)
        if os.path.isfile(current_item_path) and current_item_path.endswith('.md'):
            generate_page(current_item_path, template_path, os.path.join(dest_dir_path, item.replace('md', 'html')), base_path)
        else:
            os.makedirs(os.path.join(dest_dir_path, item))
            generate_pages_recursive(current_item_path, template_path, os.path.join(dest_dir_path, item), base_path)