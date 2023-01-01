import time
import fluidsynth

fs = fluidsynth.Synth()
fs.start()

sfid = fs.sfload('Chrono Trigger.sf2')  # replace path as needed
for preset in range(0,100):
    fs.program_select(0, sfid, 0, preset)

    fs.noteon(0, 60, 30)
    fs.noteon(0, 67, 30)
    fs.noteon(0, 76, 30)

    time.sleep(1.0)

    fs.noteoff(0, 60)
    fs.noteoff(0, 67)
    fs.noteoff(0, 76)

time.sleep(1.0)

fs.delete()
"""
000-000 piano
000-001 pianom
000-002 pianol
000-004 rhodes
000-012 marimba
000-017 porg
000-030 dguit
000-033 fbass
000-034 pbass
000-038 synthbass
000-045 pizzicato
000-046 harp
000-047 timpani
000-048 str
000-049 str2
000-052 choir
000-056 trumpet
000-060 horn
000-065 sax
000-069 oboe
000-073 flute
000-075 panflute
000-079 tone1
000-080 tone2
000-081 tone4
000-082 tone3
000-083 tone5
000-116 toms
000-117 osnare
000-118 voice
000-119 tamb
000-120 perc3
000-121 perc2
000-122 perc1
000-123 cymbal
000-124 snare
000-125 bassdrum
000-126 hihatop
000-127 hihatcl
001-033 fbassfd
001-046 harpfd
001-048 at0str
001-081 tone4l
001-123 crashfd1
001-127 lavos
002-127 lavos1
003-127 lavos2

"""