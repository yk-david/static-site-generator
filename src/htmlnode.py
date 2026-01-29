class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None or self.props == '':
            return ''
        html = []
        for key, value in self.props.items():
            html.append(f'{key}={value}')
        
        return ' '.join(html)


# test = {
#     "href": "https://www.google.com",
#     "target": "_blank",
# }

# for key, val in test.items():
#     print(key)
#     print(val)