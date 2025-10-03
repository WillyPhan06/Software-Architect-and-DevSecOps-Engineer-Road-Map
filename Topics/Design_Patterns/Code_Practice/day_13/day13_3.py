# Coded Proxy Pattern from scratch using understanding and applied __getattr__ for the proxy class to automatically extend with new methods of the real class

from abc import ABC, abstractmethod
from dataclasses import dataclass

class Video(ABC):
    @abstractmethod
    def load(self, content: str):
        pass

    @abstractmethod
    def play(self):
        pass


@dataclass
class YoutubeVideo(Video):
    content: str = None
    playing: bool = False

    def load(self):
        print(f"Loading content of {self.content} to the video")
        self.content = self.content

    def play(self):
        if not self.playing:
            print("Playing the video")
            self.playing = True
        else:
            print("Video already playing")

    def pause(self):
        if self.playing:
            print("Pausing the video")
            self.playing = False
        else:
            print("Video already paused")

@dataclass
class ProxyYoutubeVideo:
    youtube_video: YoutubeVideo = None
    content: str = None

    def load(self):
        if not self.youtube_video:
            self.youtube_video = YoutubeVideo(content=self.content)
            self.youtube_video.load()

    def __getattr__(self, name: str):
        self.load()
        return getattr(self.youtube_video, name)
    
if __name__ == "__main__":
    video = ProxyYoutubeVideo(content="cat.mp4")
    video.play()
    video.play()
    video.pause()
    video.pause()
    video.play()
    video.pause()





