from lecture17 import *

def test_init():
    b = Book("The Nickel Boys", "Colson Whitehead")
    assert b.title == "The Nickel Boys"
    assert b.author == "Colson Whitehead"

def test_matches():
    b = Book("The Nickel Boys", "Colson Whitehead")
    assert b.matches("Nickel")
    assert not b.matches("Parasite")
    assert b.matches("Colson")

    b.library_checkout()
    assert b.matches("Nickel")
    assert not b.matches("Parasite")
    assert b.matches("Colson")


def test_checkout():
    b = Book("The Nickel Boys", "Colson Whitehead")
    b.library_checkout()
    assert b.checked_out

def test_return():
    b = Book("The Nickel Boys", "Colson Whitehead")
    b.library_checkout()
    b.library_return()
    assert not b.checked_out

