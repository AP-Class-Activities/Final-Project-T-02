from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QHBoxLayout
import sys

class store(QWidget):
  def  __init__(self):
    super().__init__()
    self.setWindowTitle('فهرستی از محصولات در حال فروش')
    self.boxlayout=QVBoxLayout()
    self.setLayout(self.boxlayout)
    self.label1=QLabel('Label 1')
    self.label2=QLabel('Label 2')
    self.label3=QLabel('Label 3')
    self.label4=QLabel('Label 4')
    self.label5=QLabel('Label 5')
    self.label6=QLabel('Label 6')
    self.label7=QLabel('Label 7')
    self.label8=QLabel('Label 8')
    self.boxlayout.addWidget(sef.label1)
    self.boxlayout.addWidget(sef.label2)
    self.boxlayout.addWidget(sef.label3)
    self.boxlayout.addWidget(sef.label4)
    self.boxlayout.addWidget(sef.label5)
    self.boxlayout.addWidget(sef.label6)
    self.boxlayout.addWidget(sef.label7)
    self.boxlayout.addWidget(sef.label8)


    





class incom(QWidget):
  def  __init__(self):
    super().__init__()
    self.setWindowTitle('فهرستی از درآمد فروشنده ها')
    self.lineedit1=QLineEdit()
    self.lineedit2=QLineEdit()
    self.boxlayout=QVBoxLayout()
    self.setLayout(self.boxlayout)
    self.label1=QLabel('incom1')
    self.label2=QLabel('incom2')
    self.label3=QLabel('incom3')
    self.label4=QLabel('incom4')
    self.label5=QLabel('incom5')
    self.label6=QLabel('incom6')
    self.label7=QLabel('incom7')
    self.label8=QLabel('incom8')
    self.boxlayout.addWidget(self.label1)
    self.boxlayout.addWidget(self.label2)
    self.boxlayout.addWidget(self.label3)
    self.boxlayout.addWidget(self.label4)
    self.boxlayout.addWidget(self.label5)
    self.boxlayout.addWidget(self.label6)
    self.boxlayout.addWidget(self.label7)
    self.boxlayout.addWidget(self.label8)
    self.boxlayout.addWidget(self.LineEdit1)
    self.boxlayout.addWidget(self.LineEdit2)





    
    button=QPushButton('OK')
    self.boxlayout.addWidget(self.button1)

    self.butten1.clicked.connect(self.newlabel)

  def newlabel(self):
    self.label1.setText('عملیات با م.فقیت انجام شد')






class  makecommodity(QWidget):
  def  __init__(self):
    super().__init__()
    self.setWindowTitle('فهرستی از کالا ها به همراه توضیحات')
    self.boxlayout=QVBoxLayout()
    self.setLayout(self.boxlayout)
    self.label1=QLabel('name and description1')
    self.label2=QLabel('name and description2')
    self.label3=QLabel('name and description3')
    self.label4=QLabel('name and description4')
    self.label5=QLabel('name and description5')
    self.label6=QLabel('name and description6')
    self.label7=QLabel('name and description7')
    self.label8=QLabel('name and description8')
    self.boxlayout.addWidget(sef.label1)
    self.boxlayout.addWidget(sef.label2)
    self.boxlayout.addWidget(sef.label3)
    self.boxlayout.addWidget(sef.label4)
    self.boxlayout.addWidget(sef.label5)
    self.boxlayout.addWidget(sef.label6)
    self.boxlayout.addWidget(sef.label7)
    self.boxlayout.addWidget(sef.label8)

    button=QPushButton('OK')
    self.boxlayout.addWidget(self.button2)

    self.butten1.clicked.connect(self.newlabel)

  def newlabel(self):
    self.label2.setText('درخواست شما در سامانه ثبت گردید')

class general(QWidget):
  def __init__(self):
    super().__init__()
    layout=QHBoxLayout()
    self.setLayout(layout)
    store_widget=store()
    incom_widget=incom()
    makecommodity_widget=makecommodity()
    layout.addWidget(incom_widget)
    layout.addWidget(store_widget)
    layout.addWidget(makecommodity_widget)    





















