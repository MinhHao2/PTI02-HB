from PyQt6.QtWidgets import QApplication,QMainWindow,QMessageBox,QDialog
from PyQt6 import uic
import sys
from model.Music import Music,ListMusic
from model.account import Account,ListAccount
from ui_py.ui_homedashboard import Ui_MainWindow
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
        uic.loadUi("Editsong.ui",self)
        self.buttonBox.accepted.connect(self.EditMovie)
        self.buttonBox.rejected.connect(self.exit)

    def EditMovie(self):
        ...
        self.close()
    def exit(self):
        self.close       
class HomeMenuDashboard(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.CallAfterInit()
        self.pushButton_delete.clicked.connect(self.Delete)
        self.pushButton_add.clicked.connect(self.ShowAdd)
        self.pushButton_edit.clicked.connect(self.ShowEdit)
    def Delete(self):
        name_music = self.listObject.currentItem().text()
        self.listObject.takeItem(self.listObject.currentRow())
        self.l.delete_music_by_name(name_music)
        self.CallAfterInit()
    def ShowAdd(self):
        add.show()
    def ShowEdit(self):
        edit.show()
    def CallAfterInit(self):
        self.l = ListMusic()
        self.listObject.clear()
        for Music in self.l.getAllMusic():
            self.listObject.addItem(Music.getName())
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
        self.l = ListAccount()

        # ====== Kết nối sự kiện
        self.pushButton_Login.clicked.connect(self.loginClicked)
        self.pushButton_Createaccount.clicked.connect(self.Createaccount)
    # ====== Định nghĩa sự kiện
    def Createaccount(self):
        SigninPage.show()
        self.close()
    def loginClicked(self):
        if self.l.checkAccount(Account(self.lineEdit_Username.text(),self.lineEdit_Password.text())) == True:
            SigninPage.show()
            self.close()
        else:
            print("False password")
class SignIn(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Sign up.ui",self) # Load Giao diện từ file Sign up.ui
        self.pushButton_GoLogin.clicked.connect(self.GoLogin)
        self.pushButton_SignIn.clicked.connect(self.registerAccount)
        self.l = ListAccount()
    def saveAccount(self):
        self.l.addAccount(Account(self.lineEdit_Username.text(),self.lineEdit_Password.text()))
        self.l.saveAllAccount()
    def GoLogin(self):
        LoginPage.show()
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
        self.GoLogin()  # Chuyển về trang đăng nhập sau khi đăng ký thành công
        self.l.addAccount(Account(self.lineEdit_Username.text(),self.lineEdit_Password.text()))
        self.l.saveAllAccount()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    LoginPage=LoginPage()
    SigninPage=SignIn()
    add = AddDialog()
    edit =EditDialog()
    AdminPage = HomeMenuDashboard()
    AdminPage.show() # Và hiển thị nó
    app.exec()