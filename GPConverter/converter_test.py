# this is a test file for gp converter 
import guitarpro 
song = guitarpro.parse('../test_songs/greensleeves.gp3') 


for track in song.tracks:
    for measure in track.measures:
        for voice in measure.voices:
            for beat in voice.beats:
                for note in beat.notes:
                    print("value: %r" % note.value)
                    print("beat: %r" % note.beat)
                    print("duration percent: %r" % note.durationPercent)
