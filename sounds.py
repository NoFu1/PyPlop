from playsound import playsound

class sounds:
    def _play(self, file):
        playsound(file)

    def scream(self):
        self._play('sounds/scream.mp3')
