"""A video class."""

from typing import Sequence


class Video:
    """A class used to represent a Video."""

    def __init__(self, video_title: str, video_id: str, video_tags: Sequence[str]):
        """Video constructor."""
        self._title = video_title
        self._video_id = video_id
        self._flag = None

        # Turn the tags into a tuple here so it's unmodifiable,
        # in case the caller changes the 'video_tags' they passed to us
        self._tags = tuple(video_tags)

    @property
    def title(self) -> str:
        """Returns the title of a video."""
        return self._title

    @property
    def video_id(self) -> str:
        """Returns the video id of a video."""
        return self._video_id

    @property
    def tags(self) -> Sequence[str]:
        """Returns the list of tags of a video."""
        return self._tags
    
    def format(self):
        return (
            f"{self.title} ({self.video_id})" +
            (f" [{' '.join(self.tags)}]")
        )
        
    def title_contains_term(self,term):
        return term.lower() in self._title.lower()
    
    def title_contains_tag(self,tag):
        return tag.lower() in self._tags
    
    def flag_video(self,reason):
        if self._flag is not None:
            return False
        else:
            self._flag = reason
            return True
            