from textnode import *
from htmlnode import *
def text_node_to_html_node(text_node):
        if text_node.text_type not in [t.value for t in TextType]:
            raise exception('Invalid text type')   
        html_node = LeafNode()
        if text_node.text_type == 'Normal text':
            html_node.tag = None
            html_node.value = text_node.text
        elif text_node.text_type == 'Bold Text':
            html_node.tag = "b"
            html_node.value = text_node.text
        elif text_node.text_type == 'Italic text':
            html_node.tag = "i"
            html_node.value = text_node.text
        elif text_node.text_type == 'Code text':
            html_node.tag = "code"
            html_node.value = text
        elif text_node.text_type == 'links':
            html_node.tag = "a"
            html_node.props['href'] = text_node.text
        elif text_node.text_type == 'Images':
            html_node.tag = "img"
            html_node.value = ''
            html_node.props['src'] = text_node.url  # Assuming image URL is empty string
            html_node.props['alt'] = text_node.text  # Assuming alt text is same as text_node
        return html_node

test = TextNode("This is a text node", TextType.Bold)
po = text_node_to_html_node(test)
print(po)
print(test)

def main():
    pass
main()