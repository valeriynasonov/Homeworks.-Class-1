class Track:

    def __init__(self, name, long):
        self.name = name
        self.long = long

    def show(self):
        print(self.name, self.long)

track_1 = Track("Pink Floyd", 24)
print(track_1.name)

class Album:

    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.list_of_tracks = [ ]

    def get_tracks(self, list_of_tracks):
        for element in list_of_track:
            print(element)

    def add_track(self, track):
        self.list_of_tracks.append(track)

    def get_duration(self, track):
        sum(track.long for element in list_of_track)

track_2 = Track("Арлекино", 3)
track_3 = Track("Слава", 43)
album_1 = Album("Синий бархат", "Алиса")
album_1.add_track({track_1.name: track_1.long})
album_1.add_track({track_2.name: track_2.long})
album_1.add_track({track_3.name: track_3.long})
sum = 0
for element in album_1.list_of_tracks:
    for value in element.values():
        sum += value
print(sum)
track_4 = Track("Velaskes", 4)
track_5 = Track("Harlem", 6)
track_6 = Track("California in the Dream", 5)
album_2 = Album("Человек-слон", "Т2")
album_2.add_track({track_4.name: track_4.long})
album_2.add_track({track_5.name: track_5.long})
album_2.add_track({track_6.name: track_6.long})
sum = 0
for element in album_2.list_of_tracks:
    for value in element.values():
        sum += value
print(sum)
