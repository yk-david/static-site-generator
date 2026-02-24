from textnode import TextType, TextNode
import os
from copy_static import initialize_public, copy_static
from generate_page import generate_page


def main():
    initialize_public() # Clean initialization of `public`
    copy_static(os.path.join('static'), os.path.join('public'))
    generate_page('content/index.md', 'template.html', 'public/index.html')


main()
