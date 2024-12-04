
# Animal (has-a Habitat)
# Tiger (is-a Animal)
# Moose (is-a Animal)
# -------
# Habitat 

class Animal:
    pass
    #def __init__(self): 
    #    self.habitat = []

class Tiger(Animal):
    pass 
class Moose(Animal):
    pass

class Habitat:
    def __init__(self):
        self.animals = []
    pass

### is-a, has-a? 



class Engine: 
    pass
class Car:
    # This is a "class field"; it belongs to the class, not a specific object. 
    number_built = 0

    #def __init__(self):
    #    self.engine = Engine() # automatic option (engine auto-created)
    def __init__(self, engine):
        self.engine = engine    # argument option (caller provides engine)
        # ... super complicated setup code ... 
        print('vroom!')
        # Refer to a class field using the class name, not "self"
        Car.number_built = Car.number_built + 1

class Convertable(Car):
    def __init__(self, engine, roof_material):
        self.roof_material = roof_material # specific to convertable, handle it here
        super().__init__(engine)  # remember I'm a car, here's my engine
        #self.engine = engine # why not do this? (avoiding having to THINK about Car responsibilities)


# passing Engine gives more configurability (but more work to create Car)
the_engine = Engine()
miata = Convertable(the_engine, 'canvas')
print(miata.engine)
print(Car.number_built)

##########


class Library:
    def __init__(self):
        self.items = []
        self.item_count = 0

    def add(self, item):
        # maybe does some other stuff
        self.items.append(item)
        self.item_count = self.item_count + 1

    def search(self, query: str) -> list:
        return [item for item in self.items if item.matches(query)]

class LibraryItem:
    def __init__(self, library: Library):
        self.checked_out = False
        # CRITIQUE: if I want to create an item that is checked out 
        #  (maybe there's a catalogue error and i need to add something in transit)
        #  i need to remember to call checkout -- but what if there are extra side 
        #  effects? (e.g., what if i need to know who checked it out?)
        
        self.library = library # this item remembers what library it belongs to
        # library.items.append(self) # *A* choice (but skips the library's special add code)
        library.add(self) # better choice: let the library say what needs to happen

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