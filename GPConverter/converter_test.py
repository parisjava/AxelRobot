# this is a test file for gp converter

# To Do
# Make a matrix for each string for when to play
# Deal with rests
# Currently assuming that time signature is 4/4 - add support for time signature
# Discuss time division length in special cases (like triplets)

import guitarpro, numpy as np
song = guitarpro.parse('../test_songs/Twinkle.gp5')

tempo = song.tempo
print('tempo: %r bpm' % tempo)

min_note_length = 100 #arbitrary large number
sum_note_length = 0

for track in song.tracks:
    for measure in track.measures:
        for voice in measure.voices:
            for beat in voice.beats:
                print("beat duration: %r" % beat.duration)
                notelength = float(4/beat.duration.value)*float(1/tempo)*60
                sum_note_length += notelength
                if (notelength < min_note_length):
                    min_note_length = notelength
                print("length of note: %f s" % notelength)
                for note in beat.notes:
                    print("string: %r" % note.string)
                    print("value: %r" % note.value)
                    print("beat: %r" % note.beat)
                    print("duration percent: %r" % note.durationPercent)
                    print("note type: %r" % note.type)

print("min note length: %r" % min_note_length)
print("number of columns: %r" % round(sum_note_length/min_note_length))

# this matrix contains all the notes of the song and will be read by the arduino
matrix = [['\0' for x in range(round(sum_note_length/min_note_length))] for y in range(12)]

i = 0

for track in song.tracks:
    for measure in track.measures:
        for voice in measure.voices:
            for beat in voice.beats:
                print("beat duration: %r" % beat.duration)
                notelength = float(4/beat.duration.value)*float(1/tempo)*60

                print("length of note: %f s" % notelength)
                for note in beat.notes:
                    n = notelength
                    j = i
                    while (notelength > 0): # iterate through
                        matrix[note.string][j] = chr(note.value) # convert fret value to character
                        matrix[note.string+6][j] = chr(1)
                        n -= min_note_length
                        j += 1
                i+=round(notelength/min_note_length)
