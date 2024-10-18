# Picking up where we left off last time: I added the `matches` methods.
from dataclasses import dataclass

class LibraryItem:
  def __init__(self): 
    self.checked_out = False

  def library_checkout(self):
    self.checked_out = True
  def library_return(self): 
    self.checked_out = False


class Book(LibraryItem): 
  matches_count = 0

  def __init__(self, title: str, author: str):
    self.title = title 
    self.author = author 
    super().__init__()

  def __eq__(self, other):
    return self.title == other.title and self.author == other.author

  # human readable
  def __str__(self):   # str(...)
    return f'{self.title} by {self.author}'
  # more complete, for debugging, etc.
  def __repr__(self):  # repl(...)
    return f"Book('{self.title}', '{self.author}')"

  def matches(self, query: str) -> bool:
    self.matches_count = self.matches_count + 1
    print(self.matches_count)
    print(f'in matches for Book: {query} vs {self.title}')
    return query == self.title or query == self.author

class TVSeries(LibraryItem): 
  def __init__(self, title: str, num_episodes: int, actors: list[str]):
    self.title = title 
    self.num_episodes = num_episodes
    self.actors = actors
    super().__init__()

  # human readable
  def __str__(self):   # str(...)
    return f'{self.title} starring {self.actors}'
  # more complete, for debugging, etc.
  def __repr__(self):  # repl(...)
    return f"TVSeries('{self.title}', {self.num_episodes}, {self.actors})"


  def matches(self, query: str) -> bool:
    return query == self.title or any([query == actor for actor in self.actors])

tims_library = [
  Book("The Calculating Stars", "Mary Robinette Kowal"),
  TVSeries("Guardian", 40, ["Bai Yu", "Zhu Yilong"])
]

print(Book("The Calculating Stars", "Mary Robinette Kowal")
   in tims_library) # why did we expect True here???
print(1 in [1,2,3])

b = Book("The Calculating Stars", "Mary Robinette Kowal")
print(b.checked_out)
b.library_checkout()
print(b.checked_out)

# for item in tims_library:
#   print(str(item))
#   print(repr(item))

def search(library: list, query: str) -> list:
  return [item for item in library if item.matches(query)]
#print(search(tims_library, "The Calculating Stars"))
