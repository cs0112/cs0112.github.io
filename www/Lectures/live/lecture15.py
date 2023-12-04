from math import log10 # used later


#########################
# Motivating polymorphism 
#########################

def add(x, y):
  return x + y
# string, string? 
# int, int 
# float, float
# list, list
# int, float 








#########################
# Example of polymorphism
#########################

class Book: 
  def __init__(self, title: str, author: str):
    self.title = title 
    self.author = author 
 
class TVSeries: 
  def __init__(self, title: str, num_episodes: int, actors: list[str]):
    self.title = title 
    self.num_episodes = num_episodes
    self.actors = actors

tims_library = [
  Book("The Calculating Stars", "Mary Robinette Kowal"),
  TVSeries("Guardian", 40, ["Bai Yu", "Zhu Yilong"])
]

def search(library: list, query: str) -> list:
  return [item for item in library if item.matches(str)]
search(tims_library, "Stars")


