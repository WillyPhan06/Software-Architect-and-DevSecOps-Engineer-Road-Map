from abc import ABC, abstractmethod
from typing import final

class ShortFormVideo(ABC):
    @final
    def run(self, platform: str, vid_path: str):
        self.request_video(platform=platform)
        content = self.retrieving_video(vid_path=vid_path)
        self.displaying_video(content=content)
        self.displaying_comments()
        self.closing_app(platform=platform)
        return "Succeeded"
        

    def request_video(self, platform: str):
        print(f"Sent video request from {platform}")

    def retrieving_video(self, vid_path: str):
        print(f"Retrieving video from: {vid_path}")
        with open(vid_path, "r") as f:
            content = f.read()
        return content
    
    @abstractmethod
    def displaying_video(self, content: str):
        pass

    @abstractmethod
    def displaying_comments(self):
        pass

    def closing_app(self, platform: str):
        print(f"Closing the app {platform}")
