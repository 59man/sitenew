from enum import Enum

class TextType(Enum):   
    Text = 'Normal text'
    Bold = 'Bold Text'
    Italic = 'Italic text'
    Code = 'Code text'
    Links = 'links'
    Images = 'Images'
class TextNode:
    def __init__(self,text,text_type,url=None):
        self.text = text
        self.text_type = text_type.value
        self.url = url
    
    def __eq__(self,other):
        if not isinstance(other,TextNode):
            return False
        return vars(self) == vars(other)
    def __repr__(self):
        return f'TextNode({self.text},{self.text_type},{self.url})'