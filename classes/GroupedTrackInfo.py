from .TrackInfo import TrackInfo

class GroupedTrackInfo:
    tracks = []

    def __init__(self, tracks = []):
        self.tracks = [] 
        for track in tracks:
            type = track.get('type')
            if type != 'audio' and type != 'subtitles':
                continue
            props = track.get('properties')
            trackInfo: TrackInfo = TrackInfo(track.get('id'), props.get('track_name'), props.get('language'), type)
            self.tracks.append(trackInfo)

    def __hash__(self):
        return hash(tuple(self.tracks))

    def __eq__(self, other):
        if not isinstance(other, GroupedTrackInfo):
            return False
        return self.tracks == other.tracks
    
    def print(self):
        print("Grouped tracks: ")
        for track in self.tracks:
            print("\t" + str(track))
