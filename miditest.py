import mido

messages = mido.parse_all(open('Beethoven_Minuet_inG.mid', 'rb').read());
for message in messages :
    print(message);

print (5 * 5);
