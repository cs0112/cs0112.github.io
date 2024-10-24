
class Book: 
  def __init__(self, title: str, author: str):
    self.title = title 
    self.author = author 

  def matches(self, query: str) -> bool: 
    return query in self.title or query in self.author
  
  def __str__(self): 
    return f'{self.title} by {self.author}'
  
  def __eq__(self, other): 
    # TODO: other must also be a Book
    return self.title == other.title and self.author == other.author
 
class TVSeries: 
  def __init__(self, title: str, num_episodes: int, actors: list[str]):
    self.title = title 
    self.num_episodes = num_episodes
    self.actors = actors

  def matches(self, query: str) -> bool: 
    return query in self.title or any([query in actor for actor in self.actors])

  # BY CONVENTION: human-facing
  #def __str__(self): 
  #  return f'{self.title} starring {self.actors}'
  # BY CONVENTION: debugging-human facing (or program-facing)
  def __repr__(self):
    return f'TVSeries({self.title}, {self.num_episodes}, {self.actors})'

  def __eq__(self, other): 
    # TODO: other must also be a TVSeries
    return self.title == other.title and\
           self.num_episodes == other.num_episodes and\
           self.actors == other.actors # rely on equality for lists being defined!

tims_library = [
  Book("The Calculating Stars", "Mary Robinette Kowal"),
  TVSeries("Guardian", 40, ["Bai Yu", "Zhu Yilong"])
]

# We want to search, and have a different notion of match for each type of object.
def search(library: list, query: str) -> list:
  # oops
  # return [item for item in library if item.matches(str)]
  return [item for item in library if item.matches(query)]

# for item in library:
#    if item.matches(query):
#       accumulation.add(item)

if __name__ == '__main__':
    results = search(tims_library, "Bai")
    first_item = results[0]
    first_str = str(first_item) # python will add this for a print()
    first_repr = repr(first_item)
    print(first_str)
    print(first_repr)
    print(first_item) # do the str behavior 
    print(results) # ???

class A: 
  def hello(self):
    print('hello')

# Class B inherits from (or "extends") A
class B(A): 
  def goodbye(self):
    print('goodbye')

example = B()
example.hello()
example.goodbye()
