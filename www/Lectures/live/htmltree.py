from dataclasses import dataclass

# This is the dataclass we'll use for tree nodes in lecture
@dataclass
class HTMLTree:  # this is a node in the overall tree!
    tag: str
    children: list
    text: str = ""

###########################################################
# Everything after this point is helper code we've written
# for an HTML _parser_, to help you work with HTML. Without
# some means of converting a string into HTMLTrees, it would
# be a lot tougher to work with web documents. (Parsing, the 
# conversion of strings to more structured representations 
# of data, is common in computing. Even your Python programs
# get parsed into a tree-shaped data structure before they 
# are compiled and/or run.)

# Define our own error type for parsing errors. This makes it 
# easier to know at a glance that the error is related to parsing.
class ParseError(Exception):
    pass

# "Token" is a technical term related to parsing. In essence, a token
# is akin to a word. E.g., in a Python program, keywords like "for" 
# would be tokens. Here, we're defining a dataclass for tokens corresponding
# to tags like <p> or <html> or <strong>. 
@dataclass
class TagToken:
    tag: str

# Similarly, we have a token class for plain text.
@dataclass
class TextToken:
    text: str

# Every tag needs to be closed: <strong> needs </strong>, etc.
@dataclass
class CloseTagToken:
    tag: str

# "Lexing" is very much like calling split() on a string. However, 
# instead of producing a list of strings, it produces a list of tokens.
# (In general, lexing might be more complex; it's not *always* about
# splitting strings by blank space.)
def lex(s):
    in_tag = False
    in_close_tag = False
    text = ""
    toks = []
    s = s.strip()
    for i in range(len(s)):
        c = s[i]
        if c == "<" and not (in_tag or in_close_tag):
            if s[i + 1] == "/":
                in_close_tag = True
            else:
                in_tag = True
            if text.strip():
                toks.append(TextToken(text))
            text = ""
        elif c == ">":
            if in_tag:
                toks.append(TagToken(text))
                text = ""
                in_tag = False
            elif in_close_tag:
                toks.append(CloseTagToken(text))
                text = ""
                in_close_tag = False
            else:
                text += c
        else:
            text += c
    if in_tag or in_close_tag:
        raise ParseError()
    if text.strip():
        toks.append(TextToken(text))
    return toks

# Parsing turns a stream of tokens into a tree. 
def parse_tag(toks, index):
    tag = toks[index].tag
    index = index + 1
    children = []
    while True:
        if toks[index] == CloseTagToken("/" + tag):
            return (HTMLTree(tag, children), index + 1)
        child, index = parse_at_index(toks, index)
        children.append(child)


def parse_at_index(toks, index):
    if isinstance(toks[index], TagToken):
        return parse_tag(toks, index)
    elif isinstance(toks[index], TextToken):
        return (HTMLTree("text", [], toks[index].text), index + 1)
    else:
        raise ParseError()


def parse(s):
    toks = lex(s)
    return parse_at_index(toks, 0)[0]

# Helper function to print out an HTMLTree as a readable string.
#   (Kind of the reverse of parsing.)
def print_html(tag):
    if tag.tag == "text":
        print(tag.text, end="")
    else:
        print("<{}>".format(tag.tag), end="")
        for c in tag.children:
            print_html(c)
        print("</{}>".format(tag.tag), end="")


def to_html_string(node: HTMLTree) -> str:
    if node.tag == "text":
        # Note: relying on "text" node having no children; should we assert something?
        # Note: I don't like that we're inventing new nodes with a new tag
        return node.text
    else:
        child_strs = "".join([to_html_string(c) for c in node.children])
        return f'<{node.tag}>{child_strs}</{node.tag}>'

        
        
