
class HtmlNode:
    def __init__(self,tag=None,value=None,children = None ,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError('not implemented')

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HtmlNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(value,tag,None,props)
    def to_html(self):
        if self.value == None:
            raise ValueError('All leaf nodes must have a value.')
        if self.tag is None: 
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'      
        
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HtmlNode):
    def __init__(self, tag=None,children = None , props=None):
        super().__init__(tag,None,children,props)
    def to_html(self):   
        if self.tag is None:
            raise ValueError('All ParentNode must have a tag.')
        if self.children is None:
            raise ValueError('All ParentNode must have a Children.')

        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
        
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"