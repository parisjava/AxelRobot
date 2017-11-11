import mido

messages = mido.parse_all(open('Beethoven_Minuet_inG.mid', 'rb').read());
currentNote = 0
notes = []
time = 0
for message in messages :
    messageInformation = message.dict();
    time += messageInformation['time']

    type = messageInformation['type'];

    if (type == 'note_on' and currentNote == 0) :
        currentNote = messageInformation['note']
        continue
    
    if (type == 'note_off' and messageInformation['note'] == currentNote) :
        notes.append({currentNote : time})
        currentNote = 0
        time = 0
        
print(notes)
