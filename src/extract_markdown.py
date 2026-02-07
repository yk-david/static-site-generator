import re


def extract_markdown_images(text):
    pattern = r'[]'
    # return re.findall(r'\[\]', text)


print(extract_markdown_images(
    "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
)

