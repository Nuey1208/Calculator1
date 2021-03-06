# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalQt1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(370, 552)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.OutputLabel = QtWidgets.QLabel(self.centralwidget)
        self.OutputLabel.setGeometry(QtCore.QRect(10, 10, 351, 81))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(28)
        self.OutputLabel.setFont(font)
        self.OutputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.OutputLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.OutputLabel.setLineWidth(2)
        self.OutputLabel.setMidLineWidth(0)
        self.OutputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.OutputLabel.setObjectName("OutputLabel")
        self.CE = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("CE"))
        self.CE.setGeometry(QtCore.QRect(10, 100, 80, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.CE.setFont(font)
        self.CE.setObjectName("CE")
        self.deleting = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.delete_it())
        self.deleting.setGeometry(QtCore.QRect(100, 100, 80, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.deleting.setFont(font)
        self.deleting.setObjectName("deleting")
        self.Divide = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("/"))
        self.Divide.setGeometry(QtCore.QRect(190, 100, 80, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Divide.setFont(font)
        self.Divide.setObjectName("Divide")
        self.multiply = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("*"))
        self.multiply.setGeometry(QtCore.QRect(280, 100, 80, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.multiply.setFont(font)
        self.multiply.setObjectName("multiply")
        self.Seven = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("7"))
        self.Seven.setGeometry(QtCore.QRect(10, 180, 80, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Seven.setFont(font)
        self.Seven.setObjectName("Seven")
        self.Nine = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("9"))
        self.Nine.setGeometry(QtCore.QRect(190, 180, 80, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Nine.setFont(font)
        self.Nine.setObjectName("Nine")
        self.Minus = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("-"))
        self.Minus.setGeometry(QtCore.QRect(280, 180, 80, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Minus.setFont(font)
        self.Minus.setObjectName("Minus")
        self.Eight = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("8"))
        self.Eight.setGeometry(QtCore.QRect(100, 180, 80, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Eight.setFont(font)
        self.Eight.setObjectName("Eight")
        self.Four = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("4"))
        self.Four.setGeometry(QtCore.QRect(10, 260, 80, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Four.setFont(font)
        self.Four.setObjectName("Four")
        self.Six = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("6"))
        self.Six.setGeometry(QtCore.QRect(190, 260, 80, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Six.setFont(font)
        self.Six.setObjectName("Six")
        self.Plus = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("+"))
        self.Plus.setGeometry(QtCore.QRect(280, 260, 80, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Plus.setFont(font)
        self.Plus.setObjectName("Plus")
        self.Five = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("5"))
        self.Five.setGeometry(QtCore.QRect(100, 260, 80, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Five.setFont(font)
        self.Five.setObjectName("Five")
        self.One = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("1"))
        self.One.setGeometry(QtCore.QRect(10, 340, 80, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.One.setFont(font)
        self.One.setObjectName("One")
        self.Three = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("3"))
        self.Three.setGeometry(QtCore.QRect(190, 340, 80, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Three.setFont(font)
        self.Three.setObjectName("Three")
        self.Equal = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.equal_it())
        self.Equal.setGeometry(QtCore.QRect(280, 340, 80, 155))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Equal.setFont(font)
        self.Equal.setObjectName("Equal")
        self.Two = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("2"))
        self.Two.setGeometry(QtCore.QRect(100, 340, 80, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Two.setFont(font)
        self.Two.setObjectName("Two")
        self.Zero = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("0"))
        self.Zero.setGeometry(QtCore.QRect(10, 420, 171, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Zero.setFont(font)
        self.Zero.setObjectName("Zero")
        self.Dot = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.dot_it())
        self.Dot.setGeometry(QtCore.QRect(190, 420, 80, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Dot.setFont(font)
        self.Dot.setObjectName("Dot")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 370, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    #Doing the <<
    def delete_it(self):
        #Grab what's on the screen already
        screen = self.OutputLabel.text()
        #Delete from the back
        screen = screen[:-1]
        #Return back that new list
        self.OutputLabel.setText(screen)

    #Doing the equal:
    def equal_it(self):
        #Grab what's on the screen already
        screen = self.OutputLabel.text()
        try:
            #Do the math
            answer = eval(screen)
            #Output the answer to the screen
            self.OutputLabel.setText(str(answer))
        except:
            self.OutputLabel.setText("ERROR")


    
    #Add Decimal
    def dot_it(self):
        #Grab what's on the screen already
        screen = self.OutputLabel.text()
        
        if screen[-1] == ".":
            pass
        else:
            self.OutputLabel.setText(f'{screen}.')

    #Pressing Button
    def press_it(self, pressed):
        screen = self.OutputLabel.text()
        #Checking if input after answer is int so screen need to recalculate(start from "0")
        if isinstance(pressed, int) == True:
            screen == "0"
        #If input is "/,*,-,+" then continue the calculation
        else:
            pass
        #If press 'CE' set text '0'.
        if pressed == "CE":
            self.OutputLabel.setText('0')
        else:
            #Deleting "0" in the front ex. 083 -> 83
            if self.OutputLabel.text() == "0":
                self.OutputLabel.setText("")
            self.OutputLabel.setText(f'{self.OutputLabel.text()}{pressed}')

    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.OutputLabel.setText(_translate("MainWindow", "0"))
        self.CE.setText(_translate("MainWindow", "CE"))
        self.deleting.setText(_translate("MainWindow", "<<"))
        self.Divide.setText(_translate("MainWindow", "/"))
        self.multiply.setText(_translate("MainWindow", "*"))
        self.Seven.setText(_translate("MainWindow", "7"))
        self.Nine.setText(_translate("MainWindow", "9"))
        self.Minus.setText(_translate("MainWindow", "-"))
        self.Eight.setText(_translate("MainWindow", "8"))
        self.Four.setText(_translate("MainWindow", "4"))
        self.Six.setText(_translate("MainWindow", "6"))
        self.Plus.setText(_translate("MainWindow", "+"))
        self.Five.setText(_translate("MainWindow", "5"))
        self.One.setText(_translate("MainWindow", "1"))
        self.Three.setText(_translate("MainWindow", "3"))
        self.Equal.setText(_translate("MainWindow", "="))
        self.Two.setText(_translate("MainWindow", "2"))
        self.Zero.setText(_translate("MainWindow", "0"))
        self.Dot.setText(_translate("MainWindow", "."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
