from .template import ShortFormVideo

class YoutubeShorts(ShortFormVideo):
    def displaying_video(self, content):
        print("Video frame in the middle with gray background with sometimes buggy ah comment section with details about views and stuff with author on the bottom left of the video frame")
        print(f"Frame of shorts showing video of: {content}")

    def displaying_comments(self):
        print("Pretty much normal comments")