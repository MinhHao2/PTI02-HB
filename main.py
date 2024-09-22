from PyQt6.QtWidgets import QApplication,QMainWindow,QMessageBox,QDialog,QWidget
from PyQt6 import uic,QtCore,QtGui,QtWidgets
from PyQt6.QtCore import QDate, QDateTime
import sys
import webbrowser
from model.Music import Music,ListMusic
from model.account import Account,ListAccount
from ui_py.ui_homedashboard import Ui_MainWindow
from ui_py.Sort import Ui_Sorting
# from AI.listen_and_speak import speech_to_text
class AddDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("Addsong.ui",self)
        self.buttonBox.accepted.connect(self.addMovie)
        self.buttonBox.rejected.connect(self.exit)
        self.btn_browseimg.clicked.connect(self.browseimage)
    def browseimage(self):
        filePath ,_ = QtWidgets.QFileDialog.getOpenFileName(self,"Select an image","","Image files(*.png *.jpg *.jpeg *bmp)")
        if filePath:
            self.txt_image.setText(filePath)
                

    def addMovie(self):
        self.l = ListMusic()
        self.l.add_music(Music("Null",self.lineEdit_name.text(),self.dateEdit_date.text(),self.lineEdit_score.text(),self.lineEdit_URL.text(),self.txt_image.text()))
        AdminPage.CallAfterInit()
        sort.loadDataObject()
        self.close()
    def exit(self):
        self.close
class EditDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.oldMusic = None
        uic.loadUi("Editsong.ui",self)
        self.buttonBox.accepted.connect(self.setNewMusic)
        self.btn_browseimg.clicked.connect(self.browseimage)
    def browseimage(self):
        filePath ,_ = QtWidgets.QFileDialog.getOpenFileName(self,"Select an image","","Image files(*.png *.jpg *.jpeg *bmp)")
        if filePath:
            self.txt_image.setText(filePath)

    def setOldMusic(self, music:Music):
        # Dat Ten Objects cho dung
        self.oldMusic = music
        self.lineEdit_name.setText(music.getName())
        date_str = music.getDay()
        date = QDate.fromString(date_str, "yyyy-MM-dd")
        self.dateEdit_date.setDate(date)
        self.lineEdit_score.setText(str(music.getScore()))
        self.lineEdit_URL.setText(music.getLink())
        self.txt_image.setText(music.getImg())

    def setNewMusic(self):
        # Xoa Movie cu
        self.l = ListMusic()
        self.l.delete_music_by_name(self.oldMusic.getName())
        # Them Movie Moi
        self.l.add_music(Music("Null",self.lineEdit_name.text(),self.dateEdit_date.text(),self.lineEdit_score.text(),self.lineEdit_URL.text(),self.txt_image.text()))
        AdminPage.CallAfterInit()
        sort.loadDataObject()
        self.close()

    def exit(self):
        self.close()
     
class HomeMenuDashboard(QMainWindow,Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.CallAfterInit()
        self.pushButton_delete.clicked.connect(self.Delete)
        self.pushButton_add.clicked.connect(self.ShowAdd)
        self.pushButton_edit.clicked.connect(self.ShowEdit)
        self.pushButton_home.clicked.connect(self.goHome)
        self.pushButton_game.clicked.connect(self.goDiscover)
        self.btn_search.clicked.connect(self.search)
    def show(self):
        self.showFullScreen()
    def SearchBySpeech(self):
        valueSearch =speech_to_text()
        dataSearch = self.l.searchmusicbyname(valueSearch)
        self.ListMusic.clear()
        for music in dataSearch:
            self.listObject.addItem(music.getName())
    def search(self):
        self.listObject.clear()
        data=self.l.searchMusicByTitle(self.txt_search.text())
        for music in data :
            self.listObject.addItem(music.getName( ))
    def Delete(self):
        name_music = self.listObject.currentItem().text()
        self.listObject.takeItem(self.listObject.currentRow())
        self.l.delete_music_by_name(name_music)
        sort.loadDataObject()
        self.CallAfterInit()
    def ShowAdd(self):
        
        add.show()
    def ShowEdit(self):
        if self.listObject.currentRow() >= 0:
            edit.setOldMusic(self.l.getMusicbyname(self.listObject.currentItem().text()))
            edit.show()
    def CallAfterInit(self):
        self.l = ListMusic()
        self.listObject.clear()
        for Music in self.l.getAllMusic():
            self.listObject.addItem(Music.getName())
    def goDiscover(self):
        sort.show()
        self.close()
    def goHome(self):
        main.show()
        self.close()
    
def show_message_box(title, message, icon):
    msg_box = QMessageBox()
    msg_box.setWindowTitle(title)
    msg_box.setIcon(icon)
    msg_box.setText(message)
    msg_box.exec()

class LoginPage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Login.ui",self) # Load Giao diện từ file LoginPage.ui
        
    

        # ====== Kết nối sự kiện
        self.pushButton_Login.clicked.connect(self.loginClicked)
        self.pushButton_Createaccount.clicked.connect(self.Createaccount)
    def show(self):
        self.showFullScreen()
    # ====== Định nghĩa sự kiện
    def Createaccount(self):
        SigninPage.show()
        self.close()
    def loginClicked(self):
        if ListAcc.checkAccount(Account(self.lineEdit_Username.text(),self.lineEdit_Password.text())) == True:
            main.show()
            self.close()
        else:
            print("False password")
class SignIn(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Sign up.ui",self) # Load Giao diện từ file Sign up.ui
        
        self.pushButton_GoLogin.clicked.connect(self.GoLogin)
        self.pushButton_SignIn.clicked.connect(self.registerAccount)
    def show(self):
        self.showFullScreen()    
    def saveAccount(self):
        ListAcc.addAccount(Account(self.lineEdit_Username.text(),self.lineEdit_Password.text()))
        ListAcc.saveAllAccount()
        
    def GoLogin(self):
        loginPage.show()
        self.close()
    def registerAccount(self):
        username = self.lineEdit_Username.text()
        password = self.lineEdit_Password.text()
        confirmPassword = self.lineEdit_Confirmpassword.text()

        if not username or not password or not confirmPassword:
            show_message_box("Lỗi", "Vui lòng nhập đầy đủ thông tin.", QMessageBox.Icon.Warning)
            return

        if password != confirmPassword:
            show_message_box("Lỗi", "Mật khẩu không khớp! Vui lòng nhập lại.", QMessageBox.Icon.Warning)
            return
        
    
        show_message_box("Thành công", "Đăng ký thành công! Bạn có thể đăng nhập ngay bây giờ.", QMessageBox.Icon.Information)
        ListAcc.addAccount(Account(self.lineEdit_Username.text(),self.lineEdit_Password.text()))
        ListAcc.saveAllAccount()
        self.GoLogin()  # Chuyển về trang đăng nhập sau khi đăng ký thành công
class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Main.ui",self) # Load Giao diện từ file Sign up.ui
        self.pushButton_setting.clicked.connect(self.Homemenushow)
        self.pushButton_game.clicked.connect(self.SortPageshow)
        self.pushButton_checkArtist1.clicked.connect((lambda _,item="https://open.spotify.com/artist/4dpARuHxo51G3z768sgnrY": self.ArtistShow(item)))
        self.pushButton_checkArtist2.clicked.connect((lambda _,item="https://open.spotify.com/artist/04gDigrS5kc9YWfZHwBETP": self.ArtistShow(item)))
        self.pushButton_checkArtist3.clicked.connect((lambda _,item="https://open.spotify.com/artist/1Xyo4u8uXC1ZmMpatF05PJ": self.ArtistShow(item)))
        self.pushButton_checkArtist4.clicked.connect((lambda _,item="https://open.spotify.com/artist/4V8Sr092TqfHkfAA5fXXqG": self.ArtistShow(item)))
        self.pushButton_checkArtist5.clicked.connect((lambda _,item="https://open.spotify.com/artist/6M2wZ9GZgrQXHCFfjv46we": self.ArtistShow(item)))
        self.pushButton_checkArtist6.clicked.connect((lambda _,item="https://open.spotify.com/artist/7GlBOeep6PqTfFi59PTUUN": self.ArtistShow(item)))
        self.pushButton_checkArtist7.clicked.connect((lambda _,item="https://open.spotify.com/artist/74KM79TiuVKeVCqs8QtB0B": self.ArtistShow(item)))
        self.pushButton_checkArtist8.clicked.connect(self.open2links)
    def open2links(self):
        webbrowser.open("https://open.spotify.com/artist/1HY2Jd0NmPuamShAr6KMms")
        webbrowser.open("https://open.spotify.com/artist/0du5cEVh5yTK9QJze8zA0C")
    def ArtistShow(self,link_artist):
        webbrowser.open(link_artist)
    def show(self):
        self.showFullScreen()
    def SortPageshow(self):
        sort.show()
        self.close()
    def Homemenushow(self):
        AdminPage.show()
        self.close()

class SortingPage(QMainWindow,Ui_Sorting):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.l = ListMusic()
        self.loadDataObject()
        self.pushButton_home.clicked.connect(self.goHome)
        self.pushButton_setting.clicked.connect(self.goSetting)
        
    def show(self):
        self.showFullScreen()
    def loadDataObject(self):
        self.setupUi(self)
        self.l = ListMusic()
        self.pushButton_home.clicked.connect(self.goHome)
        self.pushButton_setting.clicked.connect(self.goSetting)
        for x in self.l.getAllMusic():
            self.widget_12 = QtWidgets.QWidget(parent=self.widget_2)
            self.widget_12.setMinimumSize(QtCore.QSize(214, 377))
            self.widget_12.setMaximumSize(QtCore.QSize(9999, 9999))
            self.widget_12.setStyleSheet("background-color: transparent;")
            self.widget_12.setObjectName("widget_12")
            self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_12)
            self.verticalLayout_6.setObjectName("verticalLayout_6")
            self.label_14 = QtWidgets.QLabel(parent=self.widget_12)
            self.label_14.setMaximumSize(QtCore.QSize(1111111, 111111))
            self.label_14.setText("123")
            self.label_14.setPixmap(QtGui.QPixmap(x.getImg()))
            self.label_14.setScaledContents(True)
            self.label_14.setObjectName("label_14")
            self.verticalLayout_6.addWidget(self.label_14)
            self.label_15 = QtWidgets.QLabel(parent=self.widget_12)
            font = QtGui.QFont()
            font.setPointSize(24)
            self.label_15.setFont(font)
            self.label_15.setStyleSheet("color:white;")
            self.label_15.setText(x.getName())
            self.label_15.setObjectName("label_15")
            self.verticalLayout_6.addWidget(self.label_15)
            self.label_16 = QtWidgets.QLabel(parent=self.widget_12)
            font = QtGui.QFont()
            font.setPointSize(16)
            self.label_16.setFont(font)
            self.label_16.setStyleSheet("color:grey;")
            self.label_16.setObjectName("label_16")
            self.label_16.setText(x.getDay())
            self.verticalLayout_6.addWidget(self.label_16)
            self.label_28 = QtWidgets.QLabel(parent=self.widget_12)
            font = QtGui.QFont()
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            self.label_28.setFont(font)
            self.label_28.setStyleSheet("color:rgb(0, 126, 0);")
            self.label_28.setObjectName("label_28")
            self.label_28.setText("Rating :"+ str(x.getScore())+"/10")
            self.verticalLayout_6.addWidget(self.label_28)
            self.pushButton_play = QtWidgets.QPushButton(parent=self.widget_12)
            icon4 = QtGui.QIcon()
            icon4.addPixmap(QtGui.QPixmap("../../Downloads/play.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.pushButton_play.setIcon(icon4)
            self.pushButton_play.setIconSize(QtCore.QSize(61, 42))
            self.pushButton_play.setObjectName("pushButton_play")
            self.pushButton_play.clicked.connect(lambda _,item=x: self.openLink(item))
            self.verticalLayout_6.addWidget(self.pushButton_play)
            self.horizontalLayout.addWidget(self.widget_12)
            self.widget_6 = QtWidgets.QWidget(parent=self.widget_2)
            self.widget_6.setObjectName("widget_6")
            self.horizontalLayout.addWidget(self.widget_6)
    def openLink(self,a):
        a.open_music()
    def goSetting(self):
        AdminPage.show()
        self.close()
    def goHome(self):
        main.show()
        self.close()


if __name__ == "__main__":
    ListAcc = ListAccount()
    app = QApplication(sys.argv)
    loginPage=LoginPage()
    SigninPage=SignIn()
    sort = SortingPage()
    add = AddDialog()
    edit =EditDialog()
    main =MainPage()
    AdminPage = HomeMenuDashboard()
    loginPage.show() # Và hiển thị n
    app.exec()