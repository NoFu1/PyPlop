from playsound import playsound
class plops:
    def __init__(self, overwrite_print = False):
        self.ressourses = "plops/"
        self.overwrite_print = overwrite_print

    def plop(self, plop: str):
        try:
            playsound(self.ressources + plop)
        except: #TODO make something usefull with the except...
            print("file probably not found")


