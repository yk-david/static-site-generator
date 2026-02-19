from textnode import TextType, TextNode
import os


def main():
    node = TextNode('My webpage', TextType.LINK, 'https://www.fredu.net')
    print(node)

def copy_static():
    print(os.listdir)

copy_static()
# main()