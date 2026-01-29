from textnode import TextType, TextNode

def main():
    node = TextNode('My webpage', TextType.LINK, 'https://www.fredu.net')
    print(node)


main()