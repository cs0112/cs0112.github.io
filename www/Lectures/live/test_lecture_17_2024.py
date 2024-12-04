from lecture17_2024 import *

def test_init(): 
    b = Book("Book Title", "A Person")
    assert b.title == "Book Title"
    assert b.author == "A Person"

def test_matches():
    b = Book("Book Title", "A Person")
    assert b.matches("Title")
    assert b.matches("Person")
    assert not b.matches("The Lord of the Rings")

def test_id():
    tims_library = [
      Book("The Calculating Stars", "Mary Robinette Kowal"),
      TVSeries("Guardian", 40, ["Bai Yu", "Zhu Yilong"])
    ]

    a_book = Book("The Calculating Stars", "Mary Robinette Kowal")
    assert a_book in tims_library

