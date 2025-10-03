from .template import ShortFormVideo

class FacebookReel(ShortFormVideo):
    def displaying_video(self, content):
        print("Video frame in the middle with black background with Facebook type bar to the right showing author on top")
        print(f"Video frame showing video of: {content}")

    def displaying_comments(self):
        print("Unhinged comments lmao no difference compared to Insta reels")