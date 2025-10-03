from scratch_code.template import ShortFormVideo
from scratch_code.facebook import FacebookReel
from scratch_code.youtube import YoutubeShorts

def test_youtube_shorts():
    youtube_shorts = YoutubeShorts().run(platform="Youtube", vid_path=r"D:\GitHub_Repos\Personal_Repos\Software-Architect-and-DevSecOps-Engineer-Road-Map\Topics\Design_Patterns\Code_Practice\day_14\scratch_code\cat_vid.txt")
    assert youtube_shorts == "Succeeded"

def test_facebook_reel():
    facebook_reel = FacebookReel().run(platform="Facebook", vid_path=r"D:\GitHub_Repos\Personal_Repos\Software-Architect-and-DevSecOps-Engineer-Road-Map\Topics\Design_Patterns\Code_Practice\day_14\scratch_code\cat_vid.txt")
    assert facebook_reel == "Succeeded"