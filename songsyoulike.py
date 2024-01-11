import os
import random

songsDirectory = os.path.join(os.getcwd(), "songsyoulike")
snippetCriteria = "| D major | Treble clef | Single note | Intervals of 1 | Sixteenth note |"

def pickRandomSong():
    files = [f for f in os.listdir(songsDirectory) if os.path.isfile(os.path.join(songsDirectory, f))]
    random_file = random.choice(files)
    print(random_file)

pickRandomSong()
