class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        '''
        Docstring for __init__
        
        :param tag: A string representing the HTML tag name (e.g. 'p', 'a', 'h1', etc.)
        :param value: A string representing the value of the HTML tag (e.g. 'Hello, world!')
        :param children: A list of HTMLNode objects representing the children of this node
        :param props: A dictionary of key-value pairs representing the attributes of the HTML tag (e.g. {'href': 'https://www.google.com'})
        '''
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError('to_html method not implemented')
    
    def props_to_html(self):
        if self.props is None:
            return ''
        html = ''
        for key, value in self.props.items():
            html += f" {key}='{value}'"  
        return html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError('invalid HTML: no value')
        if self.tag is None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f'LeaFNode({self.tag}, {self.value}, {self.props})'
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError('invalid HTML: no tag')
        if self.children is None:
            raise ValueError('invalid HTML: no children')
        
        # join on `''` is important, because with space, test with multiple children would fail
        children_html = ''.join(list(map(lambda child: child.to_html(), self.children)))

        return f'<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>'
    
    def __repr__(self):
        return f'ParentNode({self.tag}, children: {self.children}, {self.props})'