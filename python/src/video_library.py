"""A video library class."""

from .video import Video
from pathlib import Path
import csv


# Helper Wrapper around CSV reader to strip whitespace from around
# each item.
def _csv_reader_with_strip(reader):
    yield from ((item.strip() for item in line) for line in reader)


class VideoLibrary:
    def __init__(self):
        self._videos = {}
        with open(Path(__file__).parent / "videos.txt") as video_file:
            reader = _csv_reader_with_strip(
                csv.reader(video_file, delimiter="|"))
            for video_info in reader:
                title, url, tags = video_info
                self._videos[url] = Video(
                    title,
                    url,
                    [tag.strip() for tag in tags.split(",")] if tags else [],
                )

    def get_all_videos(self):
        return list(self._videos.values())

    def get_video(self, video_id):
        return self._videos.get(video_id, None)
    
    def search_videos_by_term(self, term):
        counter = 1
        result = {}
        for v in self._videos:
            if self._videos[v].title_contains_term(term):
                if counter==1:
                    print(f"Here are the results for {term}:")
                print(f"{counter})",end=' ')
                print(self._videos[v].format())
                result[counter] = self._videos[v].video_id
                counter+=1
        if counter==1:
            print(f"No search results for {term}")
        return result
    
    def search_videos_by_tag(self, tag):
        counter = 1
        result = {}
        for v in self._videos:
            if self._videos[v].title_contains_tag(tag):
                if counter==1:
                    print(f"Here are the results for {tag}:")
                print(f"{counter})",end=' ')
                print(self._videos[v].format())
                result[counter] = self._videos[v].video_id
                counter+=1
        if counter==1:
            print(f"No search results for {tag}")
        return result
        
