from math import log10
from pytest import approx

#assert log10(2) == 0.30102999566
#print(log10(2))
#assert log10(2) == approx(0.30102999566)

# Polymorphism
# 






# #########################
# # Motivating polymorphism 
# #########################

# def add(x: int, y: int) -> int:
def add(x, y):
  return 






# # string, string? 
# # int, int 
# # float, float
# # list, list
# # int, float 








# #############################################################
# # Example of polymorphism (add the `match` method in class)
# #############################################################

class Book: 
  def __init__(self, title: str, author: str):
    self.title = title 
    self.author = author 

  def matches(self, query: str) -> bool: 
    return query in self.title or query in self.author
 
class TVSeries: 
  def __init__(self, title: str, num_episodes: int, actors: list[str]):
    self.title = title 
    self.num_episodes = num_episodes
    self.actors = actors
  def matches(self, query: str) -> bool: 
    return query in self.title or any([query in actor for actor in self.actors])

tims_library = [
  Book("The Calculating Stars", "Mary Robinette Kowal"),
  TVSeries("Guardian", 40, ["Bai Yu", "Zhu Yilong"])
]

# We want to search, and have a different notion of match for each type of object.
def search(library: list, query: str) -> list:
  # oops
  return [item for item in library if item.matches(str)]
  # return [item for item in library if item.matches(query)]
print(search(tims_library, "Stars"))


