import unittest
from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def extract_title(self):
        md = '''
# Tolkien Fan Club

![JRR Tolkien sitting](/images/tolkien.png)

Here's the deal, **I like Tolkien**.

> "I am in fact a Hobbit in all but size."
>
> -- J.R.R. Tolkien    
'''
        title = extract_title(md)
        self.assertEqual(title, 'Tolkien Fan Club')


    def extract_title_two(self):
        md = '''
# This is an H1 Heading

Markdown is a lightweight markup language with plain text formatting syntax.

## Text Formatting
You can make text **bold** or *italic*.

## Lists
Here is a list of items:
* Item 1
* Item 2
* Item 3

## Code Snippet
```python
print("Hello World")
```
'''
        title = extract_title(md)
        self.assertEqual(title, 'This is an H1 Heading')