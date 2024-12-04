
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
    
    # TODO in class
    def play(self) -> str:
        '''Get the name of the next song to play'''
        if len(self.queue) < 1:
            # return '' # NO! USING '' FOR POSSIBLY 2 DIFFERENT MEANINGS
            # return 'ERROR OMG!' # same problem
            # return None # doable, if we add | None to the type
            raise Exception('no song in the queue')
        else:
            song = self.queue[0]
            del self.queue[0]   # lots of ways to remove first element, here's one
            # self.queue = self.queue[1:]
            return song

def demo(): 
    the_station = Station()
    the_station.request("Tim", "Whirling-In-Rags 8PM")
    # print(f'before: {len(the_station)}')
    print(the_station.play())
    # print(f'after: {len(the_station)}')
    try:
        print(the_station.play())
    except: 
        print('oh no')
    print('(in demo) after the exception is thrown...')

demo()
print('(top level) after the exception is thrown...')
