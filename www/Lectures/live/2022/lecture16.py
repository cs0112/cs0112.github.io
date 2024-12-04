from typing import Union 

class DJData:
    def __init__(self):
        self.queue = []
        self.num_callers = 0        

    def request(self, caller: str, song: str) -> str:
        self.queue.append(song)
        self.num_callers += 1
        if self.num_callers % 1000 == 0:
            return "Congrats, " + caller + "! You get a prize!"
        else:
            return "Cool, " + caller 

    # Here's how to provide the length of the object, as if it were a list...
    def __len__(self):
        return len(self.queue)

    def play(self) -> str:
        if len(self.queue) == 0:
            raise Exception('didnt have a song')
        song = self.queue[0]
        del self.queue[0]
        return song

dj = DJData()
dj.request('tim', 'The Night')

print('getting song...')
song1 = dj.play()
print(song1)

print('getting song...')
try: 
    song2 = dj.play()
    print(song2)
except Exception:
    print('no song in queue')

print('moving on...')