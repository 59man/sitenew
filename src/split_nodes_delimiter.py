from textnode import *
from enum import Enum
import re


#This is text with a **bolded phrase** in the middle
#node = TextNode("This is text with a `code block` word", TextType.Text)
#new_node = []
#delimiter = '`'
#split_text = node.text.split('`')
#index = (node.text.find("`"))
#matches = [match.start() for match in re.finditer(re.escape(delimiter),node.text)]
#substring = node.text[matches[0]+1:matches[1]]
#print(substring)
#for word in split_text:
#    print(word == substring)
#    new_node.append([TextNode(word,TextType.Text)])
#print(new_node)
#new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

    
#new_nodes = split_nodes_delimiter([node], "`", TextType.Code)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_node = []
    for old_node in old_nodes:
        if old_node.text_type == TextType.Text:            
           new_node.append(old_node)
           continue
        split_text = old_node.text.split(delimiter)
        splt_nodes = []
        if len(split_text) % 2 == 0:
                raise Exception('unmatched delimiters in text')

        for i,part in enumerate(split_text):
                if i % 2 == 1:
                    splt_nodes.append(TextNode(part,text_type))
                else:
                    splt_nodes.append(TextNode(part,TextType.Text))
        new_node.extend(splt_nodes)
    return new_node
           # matches = [match.start() for match in re.finditer(re.escape(delimiter),old_node.text)]
           # substring = old_node.text[matches[0]+1:matches[1]]
           # for words in split_text: 
               # if words == substring:
               #     new_node.append([TextNode(words,text_type)])
               # else:
            #        new_node.append([TextNode(words,m)])
    #return new_node
    


