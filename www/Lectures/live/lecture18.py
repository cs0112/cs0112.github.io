class Animal:
    # if habitats are more general, like biomes, maybe hold them in Animal class
    def __init__(self):
        pass

# "is-a"
class Tiger(Animal):
    pass

# "is-a"
class Moose(Animal):
    pass

# if habitats are physical locations RIGHT NOW
class Habitat:
    def __init__(self): 
        self.animals = set()
    def addAnimal(self, a: Animal):
        self.animals.add(a)
    pass

# Car 
# Engine
# Convertable    (this is a car that you can ride without a roof on!)

class Car: 
    def __init__(self, engine_mules): 
        self.engine = Engine(engine_mules) # would be more complicated in reality
        ## ...whatever Vehicle needs to initialize
        # super().__init__()
    pass

# "is-a"
class Convertable(Car): 
    def __init__(self):
        # overridden
        # self.engine = Engine(20)
        # or instead call superclass...
        super().__init__(20) 
    pass

# "has-a"
class Engine:
    def __init__(self, mules: int):
        self.mules = mules
    pass 
miata = Convertable()
print(miata.engine.mules)




























class Library:
    def __init__(self):
        self.items = []

    def add(self, item):
        # maybe does some other stuff
        self.items.append(item)

    def search(self, query: str) -> list:
        return [item for item in self.items if item.matches(query)]

class LibraryItem:
    def __init__(self, library: Library):
        self.checked_out = False
        self.library = library
        # library.items.append(self) # *A* choice
        # ^ changing a field of another object directly!!!! :-(
        library.add(self)

    def checkout(self):
        self.checked_out = True

class Book(LibraryItem):
    def __init__(self, title: str, author: str, library: Library):
        self.title = title
        self.author = author
        super().__init__(library)

    def matches(self, query: str) -> bool:
        return (not self.checked_out) and (query in self.title or query in self.author)

class Movie(LibraryItem):
    def __init__(self, title: str, director: str, actors: list, library: Library):
        self.title = title
        self.director = director
        self.actors = actors
        super().__init__(library)

    def matches(self, query: str) -> bool:
        return (not self.checked_out) and \
            query in self.title or query in self.director or \
            any([query in actor for actor in self.actors])

prov_pub = Library()
cc = Book("Cat's Cradle", "Kurt Vonnegut", prov_pub)