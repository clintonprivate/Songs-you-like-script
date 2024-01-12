import os
import random
from music21 import *

songsDirectory = os.path.join(os.getcwd(), "songsyoulike")
snippetCriteria = "| D major | Treble clef | Single note | Intervals of 1 | Sixteenth note |"

def pickRandomSong():
    files = [f for f in os.listdir(songsDirectory) if os.path.isfile(os.path.join(songsDirectory, f))]
    randomFile = random.choice(files)
    filePath = "songsyoulike/" + randomFile
    return filePath

def omitBassClef(inputFile):
    score = converter.parse(inputFile)
    score.parts[1].activeSite.remove(score.parts[1])
    score.write('musicxml', fp="output.xml", xml_declaration=True, omit_encoding=False)

omitBassClef("songsyoulike/Shining Star.mid")
