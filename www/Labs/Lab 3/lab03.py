from dataclasses import dataclass, field
from htmltree import *


def all_text(tree: HTMLTree) -> list:
    """
    Returns the text of all <text> tags within tree
    """
    # Using list comprehension to return the text of all <text> tags within tree
    child_text = [subtext for child in tree.children for subtext in all_text(child)]
    if tree.tag == "text":
        return [tree.text] + child_text
    return child_text


def all_bold_text(tree: HTMLTree) -> list:
    """
    Returns the text of all <text> tags that are descendants of <strong> tags,
    as a list of strings.
    """
    pass


def get_longest_ul_length(tree: HTMLTree) -> int:
    """
    Returns the number of entries in the longest (most children) "ul" tag in the tree.
    """
    pass


def strong_to_emph(tree: HTMLTree):
    """
    Changes all <strong> tags in the tree to <emph> tags.
    """
    pass
