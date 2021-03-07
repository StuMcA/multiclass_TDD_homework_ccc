class Room:
    
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.guests = []
        self.playlist = []

    def add_song_to_playlist(self, song):
        self.playlist.append(song)
