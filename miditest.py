import mido
import json


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

def guitarTrack(track, header, midiFile, noteMapping) :
    time = 0
    currentNote = 0
    notes = {}
    notes["notes"] = [];
    
    for message in track :
        messageInformation = message.dict();
        #print(messageInformation)
        time += messageInformation['time']

        type = messageInformation['type'];
        
        if (type == 'note_on' and currentNote == 0) :
            currentNote = messageInformation['note']
            continue
        
        if (type == 'note_off' and messageInformation['note'] == currentNote) :
            notes["notes"].append({"note" : noteMapping[currentNote][0],
                                   "octive" : noteMapping[currentNote][1],
                                   "duration" : mido.tick2second(time, midiFile.ticks_per_beat, header["tempo"])})
            currentNote = 0
            time = 0
    with open("notes.json", "w") as f :
        json.dump(notes,f);
main()
