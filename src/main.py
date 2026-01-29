from textnode import TextType, TextNode

def main():
    text_node = TextNode('My webpage', TextType.LINK, 'https://www.fredu.net')
    print(text_node)


main()