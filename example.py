from mingus.containers import Track, Composition
from mingus.containers.instrument import MidiPercussionInstrument
from mingus.midi import midi_file_out
from drummer import Drummer

class SimpleSong:
    def __init__(self):
        self.key = "C"
        self.total_bars = 64
        self.time_signature = (4, 4)
        self.composition = Composition()
        self.song_name = "percussion_example"
        self.author = "Author"
        self.tracks = {}

    def set_percussion(self):
        #init drummer object with key , time signature, and optional initial pattern
        drummer = Drummer(self.key, self.time_signature)
        md = MidiPercussionInstrument()
        t = Track(instrument=md)
       
        
        for bar_num in range(self.total_bars//4):
            drummer.change_pattern("amen_brother_part_1")
            b = drummer.get_bar()
            t.add_bar(b)
            drummer.change_pattern("amen_brother_part_2")
            b = drummer.get_bar(Fill=True)
            t.add_bar(b)
            drummer.change_pattern("amen_brother_part_3")
            b = drummer.get_bar()
            t.add_bar(b)
            drummer.change_pattern("amen_brother_part_4")
            b = drummer.get_bar(Fill=True)
            t.add_bar(b)
        self.tracks["percussion"] = t
        self.composition.add_track(t)
        return t

    def write(self):
        self.set_percussion()
        self.composition.set_title(self.song_name)
        self.composition.set_author(self.author)
        midi_file_out.write_Composition(file=f"{self.song_name}.mid", composition=self.composition, bpm=86)

if __name__ == '__main__':
    song_3 = SimpleSong()
    song_3.write()
