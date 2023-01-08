"""
File: drummer.py

This modules defines the Drummer class
"""
from mingus.containers import Track, Bar, Composition, NoteContainer, Note
from mingus.core import progressions, value
from mingus.containers.instrument import MidiPercussionInstrument
from drum_patterns import patterns
import random

class Drummer(object):
    """
    This class represents a drummer that can take instructions, 
    but also be left to improvise the percussion.    
    """
    def __init__(self, key, time_signature,pattern_name=None):
        self._key = key
        self._time_signature = time_signature
        self._num_bars_played = 0
        self._pattern_name = pattern_name
        if self._pattern_name == None:
            self._pattern_name = "the_funky_drummer"
        self.pattern = patterns[self._pattern_name]
        self.md = MidiPercussionInstrument()
        self.kick = self.md.acoustic_bass_drum()
        self.kick.channel = 9
        self.snare = self.md.electric_snare()
        self.snare.channel = 9
        self.open_hi_hat = self.md.open_hi_hat()
        self.open_hi_hat.channel = 9
        self.closed_hi_hat = self.md.closed_hi_hat()
        self.closed_hi_hat.channel = 9
        self.ride = self.md.ride_cymbal_1()
        self.ride.channel = 9
        self.tambourine = self.md.tambourine()
        self.tambourine.channel = 9
        self.hi_bell = self.md.cowbell()
        self.hi_bell.channel =9
        self.lo_bell = self.md.ride_bell()
        self.lo_bell.channel = 9
        self.clap = self.md.electric_snare()
        self.clap.channel = 9
        self.lo_conga = self.md.low_conga()
        self.lo_conga.channel = 9
        self.hi_conga = self.md.mute_hi_conga()
        self.hi_conga.channel = 9
    
    def get_num_bars(self):
        return self._num_bars_played

    def change_pattern(self,pattern_name=None):
        self._pattern_name = pattern_name
        if self._pattern_name == None:
            self._pattern_name = "the_funky_drummer"
        self.pattern = patterns[self._pattern_name]

    def get_bar(self,Mute=False):
        
        b = Bar(self._key, self._time_signature)
        if Mute:
            for beat in range(self.pattern["length"]):
                b.place_notes(None, value.sixteenth)
            self._num_bars_played += 1
            return b
        
        c = 0
        for beat in range(self.pattern["length"]):
            nc = NoteContainer()
            if self.pattern["kick"][c] : 
                nc.add_notes(self.kick)
            if self.pattern["snare"][c] : 
                nc.add_notes(self.snare)
            if self.pattern["open_hi_hat"][c] : 
                nc.add_notes(self.open_hi_hat)
            if self.pattern["closed_hi_hat"][c] : 
                nc.add_notes(self.closed_hi_hat)
            if self.pattern["ride"][c] : 
                nc.add_notes(self.ride)
            if self.pattern["tambourine"][c] : 
                nc.add_notes(self.tambourine)
            if self.pattern["hi_bell"][c] : 
                nc.add_notes(self.hi_bell)
            if self.pattern["lo_bell"][c] : 
                nc.add_notes(self.lo_bell)
            if self.pattern["clap"][c] : 
                nc.add_notes(self.clap)
            if self.pattern["lo_conga"][c] : 
                nc.add_notes(self.lo_conga)
            if self.pattern["hi_conga"][c] : 
                nc.add_notes(self.hi_conga)

            #print(len(nc))
            if len(nc):
                b.place_notes(nc, value.sixteenth)
            else:
                b.place_notes(None, value.sixteenth)  
            c +=1

        self._num_bars_played += 1
        return b

    

