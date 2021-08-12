"""A video player class."""

from .video_library import VideoLibrary
from random import randrange
from .video_playlist import PlaylistLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._video_playing = None
        self._paused = False
        self._playlists = PlaylistLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        print("Here's a list of all available videos:")
        for video in sorted(self._video_library.get_all_videos(), key=lambda x: x.title):
            print(video.format())

    def play_video(self, video_id):
        v = self._video_library.get_video(video_id)
        if v is None:
            print("Cannot play video: Video does not exist",end='')
            return
        if self._video_playing:
            self.stop_video()
        print(f"Playing video: {v.title}")
        self._video_playing = v
        
            
    def stop_video(self):
        if self._video_playing:
            print(f"Stopping video: {self._video_playing.title}")
            self._video_playing = None
            self._paused = False
        else:
            print("Cannot stop video: No video is currently playing")
            
       

    def play_random_video(self):
        """Plays a random video from the video library."""
        if not self._video_library:
            print("No videos available")
            return
        video_id = "amazing_cats_video_id" #TODO: should be random
        self.play_video(video_id)
        
    def pause_video(self):
        if not self._video_playing:
            print("Cannot pause video: No video is currently playing")
            return
        if self._paused:
            print(f"Video already paused: {self._video_playing.title}")
        else:
            self._paused = True
            print(f"Pausing video: {self._video_playing.title}")

    def continue_video(self):
        if not self._video_playing:
            print("Cannot continue video: No video is currently playing")
            return
        if not self._paused:
            print("Cannot continue video: Video is not paused")
            return
        self._paused = False
        print(f"Continuing video: {self._video_playing.title}")
        
    def show_playing(self):
        if not self._video_playing:
            print("No video is currently playing")
            return
        print(f"Currently playing: {self._video_playing.format()}", "- PAUSED" * self._paused)

    def create_playlist(self, playlist_name):
        if self._playlists.createPlaylist(playlist_name):
            print(f"Successfully created new playlist: {playlist_name}")

    def add_to_playlist(self, playlist_name, video_id):
        playlist = self._playlists.getPlaylist(playlist_name)
        if playlist is None:
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")
            return
        video = self._video_library.get_video(video_id)
        if video is None:
            print(f"Cannot add video to {playlist_name}: Video does not exist")
            return
        if not playlist.addVideo(video):
            print(f"Cannot add video to {playlist_name}: Video already added")
            return
        print(f"Added video to {playlist_name}: {video.title}")

    def show_all_playlists(self):
        self._playlists.getAllPlaylists()

    def show_playlist(self, playlist_name):
        playlist = self._playlists.getPlaylist(playlist_name)
        if not playlist:
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")
            return
        print(f"Showing playlist: {playlist_name}")
        playlist.showVideos()

    def remove_from_playlist(self, playlist_name, video_id):
        playlist = self._playlists.getPlaylist(playlist_name)
        if playlist is None:
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")
            return
        video = self._video_library.get_video(video_id)
        if video is None:
            print(f"Cannot remove video from {playlist_name}: Video does not exist")
            return
        if not playlist.removeVideo(video):
            print(f"Cannot remove video from {playlist_name}: Video is not in playlist")
            return
        print(f"Removed video from {playlist_name}: {video.title}")

    def clear_playlist(self, playlist_name):
        playlist = self._playlists.getPlaylist(playlist_name)
        if playlist is None:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")
            return
        playlist.clear()
        print(f"Successfully removed all videos from {playlist_name}")

    def delete_playlist(self, playlist_name):
        if self._playlists.deletePlaylist(playlist_name):
            print(f"Deleted playlist: {playlist_name}")
        else:
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")
        

    def search_videos(self, search_term):
        result = self._video_library.search_videos_by_term(search_term)
        if len(result)>1:
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            command = input("")
            if command.isdigit() and int(command)<=len(result):
                self.play_video(result[int(command)])

    def search_videos_tag(self, video_tag):
        result = self._video_library.search_videos_by_tag(video_tag)
        if len(result)>1:
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            command = input("")
            if command.isdigit() and int(command)<=len(result):
                self.play_video(result[int(command)])

    def flag_video(self, video_id, flag_reason=""):
        v = self._video_library.get_video(video_id)
        reason =  flag_reason if flag_reason!="" else "Not supplied"
        if v is None:
            print("Cannot flag video: Video does not exist",end='')
            return
        if not v.flag_video(v,reason):
            print("Cannot flag video: Video is already flagged")
        else:
            print(f"Successfully flagged video: {video_id} (reason: {reason})")

        

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
