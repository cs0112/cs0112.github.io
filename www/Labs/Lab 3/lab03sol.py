from dataclasses import dataclass, field
from htmltree import *


def all_text(tree: HTMLTree) -> list:
    child_text = [subtext for child in tree.children for subtext in all_text(child)]
    if tree.tag == "text":
        return [tree.text] + child_text
    return child_text


# PROBLEM 1
def all_bold_text(tree: HTMLTree) -> list:
    """
    Returns the text of all <text> tags that are descendants of <strong> tags,
    as a list of strings
    """
    # non list comprehension method
    lst = []
    
    # base case
    if tree.tag == "strong":
        return all_text(tree)
    
    # recursive case
    for subtree in tree.children:
        lst = lst + all_bold_text(subtree)
        
    return lst

def all_bold_text_v2(tree: HTMLTree) -> list:
    # list comprehension method
    if tree.tag == "strong":
        return all_text(tree)
    return [text for child in tree.children for text in all_bold_text(child)]

# PROBLEM 2
def get_longest_ul_length(tree: HTMLTree) -> int:
    """
    Returns the number of entries in the longest (most children) "ul" tag in the tree
    """
    
    # base case
    if tree.tag == "ul":
        return len(tree.children)
    
    # recursive case
    longest = 0
    for child in tree.children:
        ul_length = get_longest_ul_length(child)
        if ul_length > longest:
            longest = ul_length
    return longest

# PROBLEM 3
def strong_to_emph(tree: HTMLTree):
    """
    Changes all <strong> tags in the tree to <emph> tags
    """
    if tree.tag == "strong":
        tree.tag = "emph"
    for child in tree.children:
        strong_to_emph(child)
