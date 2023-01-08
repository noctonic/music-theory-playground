from mingus.containers import Composition
from mingus.containers import Track
from mingus.containers import Bar
from mingus.containers import Note
from mingus.containers import NoteContainer
from mingus.containers import MidiInstrument
from mingus.midi import midi_file_out

c = Composition()
c.set_author('Author', 'author@email.com')
c.set_title('First Mingus Composition')

#Create an empty list of instruments
instrument_list = [None] * 10
#Create them
for x in range(len(instrument_list))
    instrument_list[x] = MidiInstrument()
    instrument_list[x] = x


#Create an empty list of Tracks
track_list = [None] * 10
#Create them and use instruments
for x in range(len(track_list)):
    track_list[x] = Track(instrument_list[x])

#Create an empty list of Tracks
bar_list = [None] * 10

for x in range(len(bar_list)):
    bar_list[x] = Bar()
    bar_list[x].place_notes("C-5", 1)
    bar_list[x].place_notes("G-5", 1)
    track_list[x].add_bar(bar_list[x])
    c.add_track(track_list[x])

midi_file_out.write_Composition("test.mid",c)