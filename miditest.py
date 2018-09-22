import mido
import json
import math


timeSlice = 100; #slice in miliseconds

def readNotes() :
    name = "MidiNotes.txt"
    noteMapping = {}
    with open(name) as f :
        notes = []
        count = 0
        for word in f.readline().split() :
            notes.append(word)

        line = f.readline()
        while line != '' :
            for i, value in enumerate(line.split()) :
                if (i == 0) :
                    continue
                noteMapping[int(value)] = [notes[i - 1], count]
            count += 1
            line = f.readline()
    return noteMapping


def main() :

    midi = mido.MidiFile('song.mid')
    noteMapping = readNotes()
    headerInformation = {}
    for i, track in enumerate(midi.tracks) :
        if (i == 0) :
            headerInformation = getHeaderInformation(track)
        if (track.name == "Acoustic Guitar") :
            guitarTrack(track, headerInformation, midi, noteMapping)
        
        


def getHeaderInformation(track) :
    headerInformation = {}
    for message in track :
        messageInformation = message.dict();
        if (messageInformation["type"] == "set_tempo") :
            headerInformation["tempo"] = messageInformation["tempo"]
    return headerInformation       

def insertNote(notes, note, duration) :
    for x in range(duration) :
        notes.append({"note" : note})
        
        
def addToNotes(notes, note, time, duration, slice) :
    print(time)
    print(duration)
    time = math.ceil(time/slice)
    insertNote(notes, "rest", time - len(notes))
    duration = math.ceil((time + duration)/slice) - time
    insertNote(notes, note, duration)
    return (time + duration) * 10

def guitarTrack(track, header, midiFile, noteMapping) :
    time = 0
    startTime = 0;
    currentNote = 0
    notes = []
    
    for message in track :
        messageInformation = message.dict();
        time += messageInformation['time']
        
        type = messageInformation['type'];
        
        if (type == 'note_on' and currentNote == 0) :
            currentNote = messageInformation['note']
            startTime = time
            continue
        
        if (type == 'note_off' and messageInformation['note'] == currentNote) :
            duration = mido.tick2second(time - startTime,
                midiFile.ticks_per_beat, header["tempo"]) * 1000;
            time = mido.tick
            time = addToNotes(notes, noteMapping[currentNote][0],
                startTime, duration, timeSlice)
            currentNote = 0
    with open("notes.json", "w") as f :
        json.dump(notes,f);
main()
