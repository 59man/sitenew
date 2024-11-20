import unittest

from htmlnode import HtmlNode,LeafNode,ParentNode

class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        node = HtmlNode(
            "a","Visit Google",props = {"href": "https://www.google.com"})
        node2= HtmlNode(
                        "h1",
                        "Welcome",
                        [HtmlNode("p", "This is a paragraph.")],
                        {"id": "main-title"})

        self.assertNotEqual(node, node2)
    def test_to_html_props(self):
        node = HtmlNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

class TestLeafmode(unittest.TestCase):
    def test_eq(self):
        LeafNode1 = LeafNode("p", "This is a paragraph of text.")
        LeafNode2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertNotEqual(LeafNode1, LeafNode2)

class TestParentNode(unittest.TestCase):
    def test_init(self):
        node = ParentNode(tag="p",
            children=[
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "Italic text"),
            LeafNode(None, "Normal text"),
            ],
            props={},
        )
        self.assertEqual(node.tag, 'p')
        self.assertEqual(node.props, {})


if __name__ == "__main__":
    unittest.main()