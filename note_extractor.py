import MIDI
import os


def write_notes(file_address):
    midi_file = open(file_address, 'rb')
    score = MIDI.midi2score(midi_file.read())
    midi_file.close()
    # ['note', start_time, duration, channel, note, velocity]

    itrack = 1
    notes = []
    this_channel_has_note = False
    while itrack < len(score):
        for event in score[itrack]:
            if event[0] == 'note':  # for example,
                this_channel_has_note = True
                notes.append(event[4])

        itrack += 1
        if this_channel_has_note and len(notes) > 20:
            break

    with open('songs.ms', 'a') as song_file:  # append
        song_file.write('\n')
        for note in notes:
            song_file.write(chr(note + 35))
        song_file.write('\t')

dataset_addr = "Dataset/mozart"
files = os.listdir(dataset_addr)
for file in files:
    path = os.path.join(dataset_addr, file)
    write_notes(path)