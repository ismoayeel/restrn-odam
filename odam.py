from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QMessageBox, QCheckBox, QRadioButton, QComboBox
class myclass(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("font-size:20px;")

        self.v_main_lay = QVBoxLayout()

        self.cmb = QComboBox()
        self.cmb.addItems(["Toshkent", "Samarqand", "Namangan", "Andijon", "Farg'ona", "Buxoro", "Jizzax", "Surhondaryo", "Qashqadaryo", "Sirdaryo", "Xorazm", "Navoiy"])
        self.cmb.activated[str].connect(self.funk)

        self.cmb2 = QComboBox()

        self.cmb_jins=QComboBox()
        self.cmb_jins.addItems(["Erkak", "Ayol"])

        self.cmb_millat=QComboBox()
        self.cmb_millat.addItems(["O'zbek", "Rus", "Tojik", "Kareys", "Qozoq", "Qirgiz"])
        

        self.edit=QLineEdit()
        self.edit.setPlaceholderText("Ism...")

        self.edit2 = QLineEdit()
        self.edit2.setPlaceholderText("Yosh...")

        self.submit_btn=QPushButton("SUBMIT")
        self.submit_btn.setStyleSheet("background: lightgreen; color:green;border-radius: 10px")
        self.submit_btn.clicked.connect(self.submit)

        self.v_main_lay.addWidget(self.cmb)
        self.v_main_lay.addWidget(self.cmb2)
        self.v_main_lay.addWidget(self.cmb_jins)
        self.v_main_lay.addWidget(self.cmb_millat)
        self.v_main_lay.addWidget(self.edit)
        self.v_main_lay.addWidget(self.edit2)
        self.v_main_lay.addWidget(self.submit_btn)

        self.setLayout(self.v_main_lay)
    
    def funk(self, data):
        if data == "Toshkent":
            self.cmb2.clear()
            self.cmb2.addItems(["Yunusobod", "Chilonzor", "Sergeli", "Yashnobod", "Mirzo Ulug'bek", "Yakkasaroy", "Shayhontohur", "Olmazor", "Mirobod"])
        elif data == "Namangan":
            self.cmb2.clear()
            self.cmb2.addItems(["Namangan", "Davlatobod", "Uychi", "Pop", "Chortoq", "Norin", "Kosonsoy", "Uchqorg'on", "Chust", "Toraqorg'on"])
        elif data == "Samarqand":
            self.cmb2.clear()
            self.cmb2.addItems(["Oqdaryo", "Jomboy", "Bulung'ur", "Narpay", "Ishtihon", "Nurota", "Urgut", "Toyloq"])
        elif data == "Andijon":
            self.cmb2.clear()
            self.cmb2.addItems(["Asaka", "Baliqchi", "Jalaquduq", "Marhamat", "Xonobod", "Pakhtabod", "Buloqboshi", "Xo'jaobod", "Qorg'ontepa"])
        elif data == "Farg'ona":
            self.cmb2.clear()
            self.cmb2.addItems(["Quva", "Beshariq", "Chortoq", "Oltinkul", "Yozyovon", "Bog'dod", "Qo'qon", "Marg'ilon", "Rishton"])
        elif data == "Sirdaryo":
            self.cmb2.clear()
            self.cmb2.addItems(["Guliston", "Sirdaryo", "Mirzaobod", "Oqoltin", "Sayxunobod", "Yangiyer"])
        elif data == "Qashqadaryo":
            self.cmb2.clear()
            self.cmb2.addItems(["Qarshi", "Koson", "Shahrisabz", "Kitob", "Chiroqchi", "Yakkabog'", "Dehqonobod"])
        elif data == "Xorazm":
            self.cmb2.clear()
            self.cmb2.addItems(["Urganch", "Xiva", "Gurlan", "Yangiariq", "Beruniy", "Shovot"])
        elif data == "Surhondaryo":
            self.cmb2.clear()
            self.cmb2.addItems(["Termez", "Angor", "Boysun", "Denov", "Sariosiyo", "Oltinsoy", "Sherobod", "Uzun"])
        elif data == "Navoiy":
            self.cmb2.clear()
            self.cmb2.addItems(["Zarafshon", "Qiziltepa", "Tomdi", "Uchkuduk", "Xatirchi", "Navoiy"])
        elif data == "Buxoro":
            self.cmb2.clear()
            self.cmb2.addItems(["Kogon", "G'ijduvon", "Vobkent", "Qorako'l", "Shofirkon", "Jondor", "Peshku", "Qorovulbozor"])
        elif data == "Jizzax":
            self.cmb2.clear()
            self.cmb2.addItems(["Zafarabad", "G'allaorol", "Baxmal", "Mirzacho'l", "Arnasay", "Do'stlik"])
    def submit(self):

        ism = self.edit.text()
        yosh = self.edit2.text()
        shahar = self.cmb.currentText()
        tuman = self.cmb2.currentText()
        jins = self.cmb_jins.currentText()
        millat = self.cmb_millat.currentText()

        self.msg=QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setStyleSheet("background:lightgrey;font-size:20px")
        self.msg.setFixedSize(500, 500)
        self.msg.setWindowTitle("Ma'lumotlar")
        self.msg.setInformativeText(f"Ism: {ism}\nYosh: {yosh}\nViloyat: {shahar}\nTuman: {tuman}\nJins: {jins}\nMillat: {millat}")
        self.msg.exec_()
        
app=QApplication([])
win=myclass()
win.show()
app.exec_()
