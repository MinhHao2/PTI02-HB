import json
class Account:
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def show(self):
        print("US:",self.username,"PW:",self.password)
    def setNewPassword(self,password):
        self.password = password
    def getUsername(self):
        return self.username
    def getPassword(self):
        return self.password
class ListAccount:
    def __init__(self):
        self.list = []
        self.loadAllAccounts()
    def checkAccount(self,account):
       self.showAllAccount()
       return (account.getUsername() + ":" + account.getPassword())in self.list
    def addAccount(self,account):
        self.list.append(account.getUsername() + ":" + account.getPassword())
    def showAllAccount(self):
        print(self.list)
    def changePassword(self,username,oldpassword,newpassword):
        for account in self.list:
            if account.username == username :
                if account.password == oldpassword :
                    account.setNewPassword(newpassword)
                else:
                    print("Wrong password!")

    def saveAllAccount(self):
        jsonfiles = list()
        for account in self.list:
            ["123:123","use:ps"]
            pos = account.find(":")
            us = account[:pos]
            ps = account[pos+1:]
            newAccount = Account(us,ps)
            jsonfiles.append(newAccount.__dict__)
        with open("model/account.json","w")as file:
            json.dump(jsonfiles,file,indent=2)
    def loadAllAccounts(self):
        with open("model/account.json","r")as file:
            jsonFile = json.load(file)


            for account in jsonFile:
                self.list.append(account["username"]+":"+account["password"])


        




