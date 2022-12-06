from dataclasses import dataclass, field
from htmltree import *


def all_text(tree: HTMLTree) -> list:
    """
    Returns the text of all <text> tags within tree
    """
    # this uses list comprehension to assist the recursion
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
    pass


# PROBLEM 2
def get_longest_ul_length(tree: HTMLTree) -> int:
    """
    Returns the number of entries in the longest (most children) "ul" tag in the tree
    """
    pass


# PROBLEM 3
def strong_to_emph(tree: HTMLTree):
    """
    Changes all <strong> tags in the tree to <emph> tags
    """
    pass
