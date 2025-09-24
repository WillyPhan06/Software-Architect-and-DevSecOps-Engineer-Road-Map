# Instantiate the classes and use the facade to watch a movie called "Inception"
# facade/home_theater.py

class Amplifier:
    def on(self): print("Amplifier on")
    def off(self): print("Amplifier off")
    def set_volume(self, level): print(f"Volume set to {level}")

class DVDPlayer:
    def on(self): print("DVD Player on")
    def off(self): print("DVD Player off")
    def play(self, movie): print(f"Playing {movie}")
    def stop(self): print("Stopping DVD")

class Projector:
    def on(self): print("Projector on")
    def off(self): print("Projector off")
    def wide_screen_mode(self): print("Projector in widescreen mode")

# Facade
class HomeTheaterFacade:
    def __init__(self, amp: Amplifier, dvd: DVDPlayer, proj: Projector):
        self.amp = amp
        self.dvd = dvd
        self.proj = proj

    def watch_movie(self, movie: str):
        print("\nGet ready to watch a movie...")
        self.amp.on()
        self.amp.set_volume(5)
        self.proj.on()
        self.proj.wide_screen_mode()
        self.dvd.on()
        self.dvd.play(movie)

    def end_movie(self):
        print("\nShutting movie theater down...")
        self.dvd.stop()
        self.dvd.off()
        self.proj.off()
        self.amp.off()

# Client code
if __name__ == "__main__":
    amp = Amplifier()
    dvd = DVDPlayer()
    proj = Projector()
    home_theater = HomeTheaterFacade(amp, dvd, proj)

    home_theater.watch_movie("Inception")
    home_theater.end_movie()