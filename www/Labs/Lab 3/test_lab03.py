from lab03sol import *
from htmltree import parse, HTMLTree

DOC = """
  <html>
    <body>
      <p>This is a <strong>test</strong></p>
      <ul>
        <li>List 1:1</li>
        <li>List 1:2</li>
      </ul>
      Text
      <ul>
        <li>List 2:1</li>
        <li>List 2:2</li>
        <li>List 2:3</li>
      </ul>
      <strong>
        <span>Bold</span> text
      </strong>
    </body>
  </html>
"""

def test_all_text():
  assert([s.strip() for s in all_text(parse(DOC))] == [
    "This is a", "test",
    "List 1:1", "List 1:2",
    "Text",
    "List 2:1", "List 2:2", "List 2:3",
    "Bold", "text"
  ])

def test_all_bold_text():
  assert([s.strip() for s in all_bold_text(parse(DOC))] == [
    "test",
    "Bold", "text"
  ])

def test_all_bold_text_v2():
  assert([s.strip() for s in all_bold_text_v2(parse(DOC))] == [
    "test",
    "Bold", "text"
  ])

def test_get_longest_ul_length():
  assert(get_longest_ul_length(parse(DOC)) == 3)

def test_strong_to_emph():
  doc = parse(DOC)
  strong_to_emph(doc)

  body = doc.children[0]
  p = body.children[0]
  
  strong1 = p.children[1]
  assert(strong1.tag == "emph")
  strong2 = body.children[4]
  assert(strong2.tag == "emph")

  def check_tag(t: HTMLTree):
    if t != strong1 and t != strong2:
      assert(t.tag != "strong" and t.tag != "emph")
    for child in t.children:
      check_tag(child)
  check_tag(doc)
