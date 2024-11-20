import unittest

from textnode import TextNode, TextType
from htmlnode import HtmlNode,LeafNode,ParentNode
from main import text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.Bold)
        node2 = TextNode("This is a text node", TextType.Bold)
        self.assertEqual(node, node2)

    def test_textnode_equality_different_content(self):
        node1 = TextNode('test',  TextType.Links, 'https://www.boot.dev')
        node2 = TextNode('different', TextType.Links, 'https://www.boot.dev')
        self.assertNotEqual(node1, node2)


    def test_textnode_equality_url_none(self):
        # Test case where url is None in one instance
        node1 = TextNode('test', TextType.Italic, None)
        node2 = TextNode('test', TextType.Italic, 'https://www.boot.dev')
        self.assertNotEqual(node1, node2)

    def setUp(self):
        self.text_node = TextNode('Hello World',TextType.Text)
        self.bold_text_node = TextNode('Bold Text', TextType.Bold)
        self.italic_text_node = TextNode('Italic Text', TextType.Italic)
    def test_basic_text(self):
        result = text_node_to_html_node(self.text_node)
        assert result.tag is None, "Invalid tag for basic text"
       
    def test_bold_text(self):
        result = text_node_to_html_node(self.bold_text_node)
        assert result.tag == 'b', "Invalid tag for bold text"
       
    
    def test_italic_text(self):
        result = text_node_to_html_node(self.italic_text_node)
        assert result.tag == 'i', "Invalid tag for italic text"
        

if __name__ == "__main__":
    unittest.main()