from playsound import playsound

class sounds:
    def play(self, sound: str):
        playsound('sounds/' + sound)

