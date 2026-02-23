from textnode import TextType, TextNode
import os
from copy_static import initialize_public, copy_static


def main():
    initialize_public() # Clean initialization of `public`
    copy_static(os.path.join('static'), os.path.join('public'))


main()
