# python3
# jukebox.py - Jukebox class implementation that holds a list of songs
# and allows users to choose from those songs with a variety of methods

from random import randint


class SongNode:

    def __init__(self, song, next=None, prev=None):
        self.song = song
        self.prev = prev
        self.next = next


class JukeBox:
    """
    Jukebox class implementation that holds a list of songs
    and allows users to choose from those songs with a variety of methods
    """
    all_songs = []

    def __init__(self):
        self._curr = None
        self._first = None
        self._last = None

    def __iter__(self):
        current = self._first
        while current:
            yield current
            current = current.next

    def __str__(self):
        values = [str(x) for x in self.all_songs]
        return " <--> ".join(values)

    def __len__(self):
        result = 0
        node = self._first
        while node:
            result += 1
            node = node.next
        return result

    def add_song(self, song):
        """
        Adds new song into the playlist 
        using a double linked Node.
        """
        if self._first == None:
            new_song = SongNode(song)
            self._curr = self._first = self._last = new_song
        else:
            self._last.next = SongNode(song, None, self._last)
            self._last = self._last.next
            new_song = self._last
        self.all_songs.append(new_song)
        self._curr = new_song
        return self._curr
        
    def playlist_empty(self):
        """
        Checks to see if there are any songs in the playlist.
        """
        return len(self.all_songs) == 0

    def play_first_song(self):
        if self.playlist_empty() == True:
            return print("There are no songs in this jukebox! Please add songs to enjoy.")
        else:
            self._curr = self._first
            return print(f"Playing {self._curr.song}")
    
    def play_last_song(self):
        if self.playlist_empty() == True:
            return print("There are no songs in this jukebox! Please add songs to enjoy.")
        else:
            self._curr = self._last
            return print(f"Playing {self._curr.song}")

    def play_song(self, specific_song):
        """
        Plays the song that the user inputs.
        If that song is not in the playlist, the song is added to the playlist.
        """
        if self.playlist_empty == True:
            self._curr = self.add_song(specific_song)
            return print(f"Playing {self._curr.song}")
        
        for song in self.all_songs:
            if song.song == specific_song:
                self._curr = song
                return print(f"Playing {self._curr.song}")

        self._curr = self.add_song(specific_song)
        return print(f"Playing {self._curr.song}")

    def play_random_song(self):
        """
        Plays a random song out of the playlist
        but keeps the order of the playlist intact.
        """
        if self.playlist_empty() == True:
            return print("There are no songs in this jukebox! Please add songs to enjoy.")
        
        random_indx = randint(0, len(self.all_songs) - 1)
        self._curr = self.all_songs[random_indx]
        return print(f"Playing {self._curr.song}")

    def play_prev(self):
        if self.playlist_empty() == True:
            return print("There are no songs in this jukebox! Please add songs to enjoy.")
        
        if self._curr == self._first:
            self._curr = self._last
            return print(f"Playing {self._curr.song}")
        else:
            self._curr = self._curr.prev
            return print(f"Playing {self._curr.song}")


    def play_next(self):
        if self.playlist_empty() == True:
            return print("There are no songs in this jukebox! Please add songs to enjoy.")
        
        if self._curr == self._last:
            self._curr = self._first
            return print(f"Playing {self._curr.song}")
        else:
            self._curr = self._curr.next
            return print(f"Playing {self._curr.song}")

    def shuffle_songs(self):
        # TODO: Implement a method that shuffles the songs into a different order
        # Either random or semi-random
        pass


def example():
    """
    Tests the jukebox class.
    """
    jukebox = JukeBox()

    jukebox.playlist_empty()

    songs = [f'song {x}' for x in range(1, 11)]
    for song in songs:
        jukebox.add_song(song)

    jukebox.playlist_empty()

    jukebox.play_first_song()
    jukebox.play_last_song()
    jukebox.play_song('song 5')
    jukebox.play_song('song 11')
    jukebox.play_song('song 22')
    jukebox.play_random_song()
    

    for x in range(20):
        jukebox.play_next()

    for x in range(20):
        jukebox.play_prev()

    for x in range(100):
        jukebox.play_next()
        jukebox.play_random_song()
        jukebox.play_prev()
        jukebox.play_random_song()


if __name__ == "__main__":
    example()