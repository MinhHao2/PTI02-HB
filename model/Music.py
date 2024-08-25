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
        print(self.id,"-",self.name,"-",self.day,"-",self.score,"-",self.link)
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
        self.saveAllMusic()
    def delete_music_by_name(self,name_music):
        for Music in self.list:
            if Music.getName()== name_music:
                self.list.remove(Music)
        self.saveAllMusic()
    def edit_music_by_name(self,name_old_music:str,new_music:Music):
        for music in self.list:
            if music.getName()==name_old_music:
                self.list.remove(music)
                self.list.append(new_music)
        self.saveAllMusic()

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

    def searchMusicByTitle(self, name):
        result = []
        for music in self.list:
            if name in music.getName():
                result.append(music)
                music.show()
        return result
    def getMusicbyname(self,nameMusic):
        for music in self.list:
            if music.getName()==nameMusic:
                return music


# while True:  
#     newlist.show_all_music()
#     x = input("Enter song's id:")
#     for i in newlist.getAllMusic():
#         if x == i :
#             i.open_movie()
l = ListMusic()
l.edit_music_by_name("Roar2",Music("1","Roar","1/1/1111","6.2","Ko co link"))
l.searchMusicByTitle("C")
