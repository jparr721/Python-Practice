import re, argparse
import sys
from matplotlib import pyplot
import plistlib
import numpy as np

"""
Cooking up a little program to go through my track list and tell me which 
artists I like the most. Hope to make this into a type of neural net
"""

def findDuplicates(fileName):
    print('Finding duplicate tracks in %s...' % fileName)
    # read in the playlist
    pList = plistlib.load(fileName)
    # get the tracks
    tracks = pList['Tracks']
    # Create dictionary to store the track names
    trackNames = {}
    # Iterate through the tracks
    for trackID, track in tracks.items():
        try:
            name = track['Name']
            duration = track['Total Time']
            # Checks to see if these entries exist in the library
            if name in trackNames:
                # Check if the name and duration for the song match, then
                # increment the count and round the track length
                if duration//1000 == trackNames[name][0]//1000:
                    count = trackNames[name][1]
                    trackNames[name] = (duration, count+1)
            else:
                # If this is the first time the program sees the track name,
                # creates a new entry for it
                trackNames[name] = (duration, 1)
        except:
            # Gonna ignore the exceptions for now
            pass

    # store duplicates
    dups = []
    for k, v in trackNames.items():
        if v[1] > 1:
            dups.append((v[1], k))
    # save duplicates to a file