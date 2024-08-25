from PyQt6.QtWidgets import QApplication,QMainWindow,QMessageBox,QDialog,QWidget
from PyQt6 import uic,QtCore,QtGui,QtWidgets
from PyQt6.QtCore import QDate, QDateTime
import sys
from model.Music import Music,ListMusic
from model.account import Account,ListAccount
from ui_py.ui_homedashboard import Ui_MainWindow
from ui_py.Sort import Ui_Sorting
class AddDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("Addsong.ui",self)
        self.buttonBox.accepted.connect(self.addMovie)
        self.buttonBox.rejected.connect(self.exit)

    def addMovie(self):
        self.l = ListMusic()
        self.l.add_music(Music("Null",self.lineEdit_name.text(),self.dateEdit_date.text(),self.lineEdit_score.text(),self.lineEdit_URL.text()))
        AdminPage.CallAfterInit()
        self.close()
    def exit(self):
        self.close
class EditDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.oldMusic = None
        uic.loadUi("Editsong.ui",self)
        self.buttonBox.accepted.connect(self.setNewMusic)

    def setOldMusic(self, music:Music):
        # Dat Ten Objects cho dung
        self.oldMusic = music
        self.lineEdit_name.setText(music.getName())
        date_str = music.getDay()
        date = QDate.fromString(date_str, "yyyy-MM-dd")
        self.dateEdit_date.setDate(date)
        self.lineEdit_score.setText(music.getScore())
        self.lineEdit_URL.setText(music.getLink())

    def setNewMusic(self):
        # Xoa Movie cu
        self.l = ListMusic()
        self.l.delete_music_by_name(self.oldMusic.getName())
        # Them Movie Moi
        self.l.add_music(Music("Null",self.lineEdit_name.text(),self.dateEdit_date.text(),self.lineEdit_score.text(),self.lineEdit_URL.text()))
        AdminPage.CallAfterInit()
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
    def search(self):
        self.listObject.clear()
        data=self.l.searchMusicByTitle(self.txt_search.text())
        for music in data :
            self.listObject.addItem(music.getName())
    def Delete(self):
        name_music = self.listObject.currentItem().text()
        self.listObject.takeItem(self.listObject.currentRow())
        self.l.delete_music_by_name(name_music)
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
        

    def loadDataObject(self):
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
            self.label_14.setText("")
            self.label_14.setPixmap(QtGui.QPixmap("../../Downloads/Rolling in the deep.png"))
            self.label_14.setScaledContents(True)
            self.label_14.setObjectName("label_14")
            self.verticalLayout_6.addWidget(self.label_14)
            self.label_15 = QtWidgets.QLabel(parent=self.widget_12)
            font = QtGui.QFont()
            font.setPointSize(24)
            self.label_15.setFont(font)
            self.label_15.setStyleSheet("color:white;")
            self.label_15.setObjectName("label_15")
            self.verticalLayout_6.addWidget(self.label_15)
            self.label_16 = QtWidgets.QLabel(parent=self.widget_12)
            font = QtGui.QFont()
            font.setPointSize(16)
            self.label_16.setFont(font)
            self.label_16.setStyleSheet("color:grey;")
            self.label_16.setObjectName("label_16")
            self.verticalLayout_6.addWidget(self.label_16)
            self.label_28 = QtWidgets.QLabel(parent=self.widget_12)
            font = QtGui.QFont()
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            self.label_28.setFont(font)
            self.label_28.setStyleSheet("color:rgb(0, 126, 0);")
            self.label_28.setObjectName("label_28")
            self.verticalLayout_6.addWidget(self.label_28)
            self.pushButton_play = QtWidgets.QPushButton(parent=self.widget_12)
            icon4 = QtGui.QIcon()
            icon4.addPixmap(QtGui.QPixmap("../../Downloads/play.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.pushButton_play.setIcon(icon4)
            self.pushButton_play.setIconSize(QtCore.QSize(61, 42))
            self.pushButton_play.setObjectName("pushButton_play")
            self.pushButton_play.clicked.connect(lambda a: self.openlink(a=x))
            self.verticalLayout_6.addWidget(self.pushButton_play)
            self.horizontalLayout.addWidget(self.widget_12)
            self.widget_6 = QtWidgets.QWidget(parent=self.widget_2)
            self.widget_6.setObjectName("widget_6")
            self.horizontalLayout.addWidget(self.widget_6)
    def openlink(self,a):
        print("1")
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
    loginPage.show() # Và hiển thị nó
    app.exec()