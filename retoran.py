from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QMessageBox, QCheckBox, QRadioButton

class myclass(QWidget):
    def __init__(self):
        super().__init__()

        self.v_main_lay=QVBoxLayout()
        self.h_lay=QHBoxLayout()

        self.chek_btn=QPushButton("Chek")
        self.chek_btn.clicked.connect(self.chek)

        self.exit_btn=QPushButton("EXIT")
        self.exit_btn.clicked.connect(exit)

        self.h_lay.addWidget(self.chek_btn)
        self.h_lay.addWidget(self.exit_btn)

# */********************************************               menyu

        self.taom_1=QLabel("1-taomlar")
        self.taom_2=QLabel("2-taomlar")
        self.ichimlik=QLabel("Ichimliklar")
        self.desert=QLabel("Desertlar")
        
        self.t11=QCheckBox("Osh  --> 40000")
        self.t12=QCheckBox("Somsa  --> 10000")
        self.t13=QCheckBox("Lag'mon  --> 35000")
        self.t14=QCheckBox("Sho'rva  --> 30000")
        self.t15=QCheckBox("Mastava  --> 40000")

        self.t21=QCheckBox("Shashlik  --> 15000")
        self.t22=QCheckBox("Bishteks  --> 30000")
        self.t23=QCheckBox("Lavash  --> 37000")
        self.t24=QCheckBox("Gamburger  --> 38000")
        self.t25=QCheckBox("Hotdog  --> 14000")

        self.i1=QCheckBox("Choy  --> 5000")
        self.i2=QCheckBox("Pepsi  --> 12000")
        self.i3=QCheckBox("Coca Cola --> 13000")
        self.i4=QCheckBox("Fanta  --> 12000")
        self.i5=QCheckBox("Sprite  --> 12000")

        self.d1=QCheckBox("Chizkeyk  --> 32000")
        self.d2=QCheckBox("Medovik  --> 38000")
        self.d3=QCheckBox("Napaleon  --> 30000")
        self.d4=QCheckBox("Snikers  --> 32000")
        self.d5=QCheckBox("Vishnya chiz  --> 45000")

        self.lst=[self.t11, self.t12, self.t13, self.t14, self.t15, 
                  self.t21, self.t22, self.t23, self.t24, self.t25, 
                  self.i1, self.i2, self.i3, self.i4,self.i5, 
                  self.d1, self.d2, self.d3, self.d4, self.d5]

# ******************************************               menyu + layout

        self.v_main_lay.addWidget(self.taom_1)
        self.v_main_lay.addWidget(self.t11)
        self.v_main_lay.addWidget(self.t12)
        self.v_main_lay.addWidget(self.t13)
        self.v_main_lay.addWidget(self.t14)
        self.v_main_lay.addWidget(self.t15)

        self.v_main_lay.addWidget(self.taom_2)
        self.v_main_lay.addWidget(self.t21)
        self.v_main_lay.addWidget(self.t22)
        self.v_main_lay.addWidget(self.t23)
        self.v_main_lay.addWidget(self.t24)
        self.v_main_lay.addWidget(self.t25)

        
        self.v_main_lay.addWidget(self.ichimlik)
        self.v_main_lay.addWidget(self.i1)
        self.v_main_lay.addWidget(self.i2)
        self.v_main_lay.addWidget(self.i3)
        self.v_main_lay.addWidget(self.i4)
        self.v_main_lay.addWidget(self.i5)

    
        self.v_main_lay.addWidget(self.desert)
        self.v_main_lay.addWidget(self.d1)
        self.v_main_lay.addWidget(self.d2)
        self.v_main_lay.addWidget(self.d3)
        self.v_main_lay.addWidget(self.d4)
        self.v_main_lay.addWidget(self.d5)

        self.v_main_lay.addLayout(self.h_lay)

        self.setLayout(self.v_main_lay)
        
    def chek(self):
        self.chek_btn.hide()
        self.exit_btn.hide()
        for i in self.lst:
            if not i.isChecked():
                i.hide()

app=QApplication([])
win=myclass()
win.show()
app.exec_()
