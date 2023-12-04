# If you _really_ want to return None and use type hints:
from typing import Union

class Station:
    def __init__(self):
         self.queue = []
         self.num_callers = 0

    def __len__(self): 
        return len(self.queue)

    def request(self, caller: str, song: str) -> str:
        '''Request a song of the current radio DJ'''
        self.queue.append(song)
        self.num_callers += 1
        if self.num_callers % 1000 == 0:
            return "Congrats, " + caller + "! You get a prize!"
        else:
            return "Cool, " + caller
    
    # What did Tim forget???
    def play(self) -> str:
        '''Get the name of the next song to play'''
        if len(self.queue) < 1: 
            # send back a better error message than IndexError
            raise Exception('no song remaining in queue; add one first')
            # raise ValueError('no song existed')
            # raise KeyError('no song')
        
        song = self.queue[0] 
        del self.queue[0]
        return song 


# the_dj = Station(0, [])
# request(the_dj, "Tim", "French Fries w/Pepper")
the_station = Station()
the_station.request("Tim", "Whirling-In-Rags 8PM")
print(the_station.play())

# Code to: keep playing songs until there are no more, and then call in,
#   ...repeat...

while True:  # loop forever! (don't use these yet please)
    try:
        next_song = the_station.play()
        print(f'Playing: {next_song}')
    except Exception:  # too broad, really (stay tuned for next week)
        the_station.request('Nim Telson', 'Never gonna give you up')


