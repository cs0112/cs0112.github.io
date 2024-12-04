from math import log10

def add(x, y):
  return x + y











class Book:
    def __init__(self, title: str, author: str):        
        self.title = title
        self.author = author

    def __str__(self):
        return self.title

    def matches(self, query: str) -> bool:
        return query in self.title or query in self.author
        
class TVSeries:
    def __init__(self, title: str, num_episodes: int, actors: list):
        self.title = title
        self.num_episodes = num_episodes
        self.actors = actors
    
    def __str__(self):
        return self.title
    
    def __repr__(self):
        return self.title

    def matches(self, query: str) -> bool:
        return query in self.title or any([query in actor for actor in self.actors])

library = [
    Book("The Calculating Stars", "Mary Robinette Kowal"),    
    TVSeries("Guardian", 40, ["Bai Yu", "Zhu Yilong"])
]
#print(str(library[0]))



def search(library: list, query: str) -> list:
    return [item for item in library if item.matches(query)]

print(search(library, 'Zhu Yilong'))

# def matches(self, query: str) -> bool:

# from pytest import approx

# # The answer given by Google's calculator:
# print(log10(2))
# assert log10(2) == approx(0.30102999566)
