from mingus.midi import fluidsynth
from mingus.containers import Note
import time

fluidsynth.init("Chrono Trigger.sf2")

#This should have the same results as ./fluidsynth-examples/example1.py but it does not :(
for preset in range(0,5):
    fluidsynth.set_instrument(0, preset,0)
    fluidsynth.play_Note(Note("C-5"))
    time.sleep(1)
    fluidsynth.stop_Note(Note("C-5"))