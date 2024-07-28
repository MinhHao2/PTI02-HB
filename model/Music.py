import webbrowser
import json
class Music:
    def __init__(self,id_music,name_music,day_music,score_music,link_music):
        self.id = id_music
        self.name = name_music
        self.day = day_music
        self.score = score_music
        self.link = link_music
    def getName(self):
        return self.name
    def getID(self):
        return self.id
    def getDay(self):
        return self.day
    def getScore(self):
        return self.score
    def getLink(self):
        return self.link
    def show(self):
        print(self.id_music,"-",self.name_music,"-",self.date_music,"-",self.score_music,"-",self.link_music,"-")
    def open_music(self):
        webbrowser.open(self.link)
    
class ListMusic:
    def __init__(self):
        self.list = []
        self.LoadAllMusic()
    def getAllMusic(self):
        return self.list
    def add_music(self,Music):
        self.list.append(Music)
    def show_all_music(self):
        for i in self.list:
            i.show()
    def saveAllMusic(self):
        jsonfiles = list()
        for Music in self.list:
            jsonfiles.append(Music.__dict__)
        with open("model/movie.json","w")as file:
            json.dump(jsonfiles,file,indent=5) 
    def LoadAllMusic(self):
        with open("model/movie.json","r")as file:
            jsonFile = json.load(file)
            for M in jsonFile:
                music = Music(M["id"],M["name"],M["day"],M["score"],M["link"])
                self.add_music(music)
# while True: 
#     newlist.show_all_music()
#     x = input("Enter song's id:")
#     for i in newlist.getAllMusic():
#         if x == i :
#             i.open_movie()