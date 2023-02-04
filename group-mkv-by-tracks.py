import argparse
import glob
import subprocess
import json
from classes.GroupedTrackInfo import GroupedTrackInfo
from classes.TrackInfo import TrackInfo

parser = argparse.ArgumentParser(
    prog='group-mkv-by-tracks.py',
    description='Group MKV files by name')

parser.add_argument('dir')

args = parser.parse_args()

# find all mkv files in the directory and subdirectories
file_names = []
for file_name in glob.glob(args.dir + '/**/*.mkv', recursive=True):
    file_names.append(file_name)

tracksToFileNames = {}

for i, file_name in enumerate(file_names):
    output = subprocess.run(['mkvmerge', '-J', file_name], stdout=subprocess.PIPE).stdout.decode('utf-8')
    output_json = json.loads(output)
    tracks = output_json.get('tracks')
    
    trackKey: GroupedTrackInfo = GroupedTrackInfo(tracks)
    
    if trackKey not in tracksToFileNames:
        tracksToFileNames[trackKey] = []
    tracksToFileNames[trackKey].append(file_name)
    
    print("Processed " + str(i + 1) + " of " + str(len(file_names)) + " files", end='\r')
    
for key in tracksToFileNames.keys():
    if tracksToFileNames[key].__len__() < 1:
        continue
    key.print()
    for file_name in tracksToFileNames[key]:
        print(file_name)
    
    print("--------------------------------------")