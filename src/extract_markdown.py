import re

# [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]



# regular links
#r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"

def extract_markdown_images(text):
    img_match = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return img_match
def extract_markdown_links(text): 
    link_match = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return link
