import os
import random
from music21 import *

songsDirectory = os.path.join(os.getcwd(), "songsyoulike")
snippetCriteria = "| D major | Treble clef | Single note | Intervals of 1 | Sixteenth note |"
d_major_scale = ["B3",
                 "C4", "C#4", "D4", "E4", "F#4", "G4", "A4", "B4",
                 "C5", "C#5", "D5", "E5", "F#5", "G5", "A5", "B5",]

def pickRandomSong():
    files = [f for f in os.listdir(songsDirectory) if os.path.isfile(os.path.join(songsDirectory, f))]
    randomFile = random.choice(files)
    filePath = "songsyoulike/" + randomFile
    return filePath

def omitBassClef(score):
    score.parts[1].activeSite.remove(score.parts[1])
    return score

def find_longest_matching_interval(maxInterval, score):
    allPortions = []
    currentPortion = []
    previousPitch = -1
    # Loop through the notes in treble clef
    for index, measure in enumerate(score.parts[0].getElementsByClass('Measure')):
        for note in measure.notes:
            noteName = str(note.pitch)
            pitch = d_major_scale.index(noteName)
            interval = abs(pitch - previousPitch)
            if (interval > maxInterval and previousPitch > -1):
                allPortions.append(currentPortion)
                currentPortion = []
            currentPortion.append(note)
            previousPitch = pitch
        if index == len(score.parts[0].getElementsByClass('Measure')) - 1:
            allPortions.append(currentPortion)
    longestMatchingPortion = max(allPortions, key=len)
    return longestMatchingPortion

def extractPlayableSnippet(inputFile):
    score = converter.parse(inputFile)

    # Remove bass clef if necessary for simplicity
    if "| Treble and bass clef |" in snippetCriteria == False:
        score = omitBassClef(score)

    # Find longest portion of the song with max intervals of 1
    print(find_longest_matching_interval(1, score))
    
    score.write('musicxml', fp="output.xml", xml_declaration=True, omit_encoding=False)

extractPlayableSnippet("songsyoulike/Shining Star.mid")
