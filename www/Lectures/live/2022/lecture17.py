class LibraryItem:
    def __init__(self):
        self.checked_out = False

    def library_checkout(self):
        self.checked_out = True
    def library_return(self):
        self.checked_out = False


class Book(LibraryItem):
    def __init__(self, title: str, author: str):        
        self.title = title
        self.author = author      
        super().__init__() # call init of whatever the immediate parent class is  

    # "human readable" string representation
    def __str__(self):
        return self.title + " by " + self.author
    # "unambiguous" string representation
    def __repr__(self):
        return f'Book("{self.title}", "{self.author}", "{self.checked_out}")'

    # def __eq__(self, other):
    #     return self.title == other.title and self.author == other.author

    def matches(self, query: str) -> bool:
        return query in self.title or query in self.author

class TVSeries(LibraryItem):
    def __init__(self, title: str, num_episodes: int, actors: list):
        self.title = title
        self.num_episodes = num_episodes
        self.actors = actors  
        super().__init__()      
    
    # "human readable" string representation
    def __str__(self):
        return self.title + " starring " + str(self.actors)
    # "unambiguous" string representation
    def __repr__(self):
        return f'TVSeries("{self.title}", {self.num_episodes}, "{self.actors}", "{self.checked_out}")'

    def matches(self, query: str) -> bool:
        return query in self.title or any([query in actor for actor in self.actors])

library = [
    Book("The Calculating Stars", "Mary Robinette Kowal"),    
    TVSeries("Guardian", 40, ["Bai Yu", "Zhu Yilong"])
]

print(str(library[1]))
print(repr(library[1]))

cstars = Book("The Calculating Stars", "Mary Robinette Kowal")
print(cstars in library)










def search(library: list, query: str) -> list:
    return [item for item in library if item.matches(query)]

print(search(library, 'Zhu Yilong'))
