import MIDI

notes = []
with open("s.ms", "r") as song_file:
    chrs = song_file.read()
    for chr in chrs:
        if ord(chr) >= 35:
            notes.append(ord(chr) - 35)

song_score = [480, [['track_name', 0, b'Sonate Opus 10 No. 1 3. Satz'], ['set_tempo', 0, 294840]]]
# ['note', start_time, duration, channel, note, velocity]


song_score.append([['track_name', 0, b'Piano Right'], ['patch_change', 0, 0, 0]])
time = 1000
for note in notes:
    song_score[-1].append(['note', time, 240, 0, note, 50])
    time += 360


midi_data = MIDI.score2midi(song_score)
with open('test2.mid', 'wb') as midi_file:
    midi_file.write(midi_data)