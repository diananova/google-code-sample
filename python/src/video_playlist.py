class Playlist:
    def __init__(self,name):
        self._name = name
        self._videos = {}
    
    @property
    def name(self) -> str:
        return self._name
    
    def addVideo(self, video):
        if video.video_id in self._videos:
            return False
        self._videos[video.video_id] = video
        return True
    
    def removeVideo(self,video):
        if video.video_id not in self._videos:
            return False
        self._videos.pop(video.video_id)
        return True
    
    def showVideos(self):
        if not self._videos:
            print("No videos here yet")
        for v in self._videos:
            print(self._videos[v].format())
            
    def clear(self):
        self._videos = {}
    
class PlaylistLibrary:
    def __init__(self):
        self._playlists = {}
        
    def createPlaylist(self, name):
        if name.lower() in self._playlists:
            print("Cannot create playlist: A playlist with the same name already exists")
            return False
        self._playlists[name.lower()] = Playlist(name)
        return True
    
    def getPlaylist(self, name):
        return self._playlists.get(name.lower(), None)
    
    def getAllPlaylists(self):
        if not self._playlists:
            print("No playlists exist yet")
            return
        print("Showing all playlists:")
        for p in sorted(self._playlists):
            print(self._playlists[p].name)
            
    def deletePlaylist(self, name):
        if name.lower() not in self._playlists:
            return False
        self._playlists.pop(name.lower())
        return True
