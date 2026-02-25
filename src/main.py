import os
import sys
from textnode import TextType, TextNode
from copy_static import initialize_public, copy_static
from generate_page import *


def main():   
    basepath = sys.argv[1] if len(sys.argv) > 1 else '/'
    initialize_public() # Clean initialization of `public`
    copy_static(os.path.join('static'), os.path.join('docs'))
    generate_pages_recursive('content', 'template.html', 'docs', basepath)

main()