# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RiwayatTidurUserInterface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 786)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.OpeningPanel = QtWidgets.QFrame(Form)
        self.OpeningPanel.setMaximumSize(QtCore.QSize(310, 16777215))
        self.OpeningPanel.setStyleSheet("QPushButton {\n"
"    background: rgb(240, 240, 240);\n"
"    border: 2px solid rgb(130, 130, 130);\n"
"    border-width: 2px;\n"
"    border-radius: 0px;\n"
"    color: black;\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgb(215, 215, 215);\n"
"}\n"
"QPushButton:pressed {\n"
"    background: rgb(200, 200, 200);\n"
"}")
        self.OpeningPanel.setObjectName("OpeningPanel")
        self.JurnalSubtitle = QtWidgets.QLabel(self.OpeningPanel)
        self.JurnalSubtitle.setGeometry(QtCore.QRect(30, 128, 271, 111))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.JurnalSubtitle.setFont(font)
        self.JurnalSubtitle.setWordWrap(True)
        self.JurnalSubtitle.setObjectName("JurnalSubtitle")
        self.JurnalTitle = QtWidgets.QLabel(self.OpeningPanel)
        self.JurnalTitle.setGeometry(QtCore.QRect(30, 64, 261, 61))
        font = QtGui.QFont()
        font.setFamily("HoloLens MDL2 Assets")
        font.setPointSize(22)
        self.JurnalTitle.setFont(font)
        self.JurnalTitle.setObjectName("JurnalTitle")
        self.ReturnButton = QtWidgets.QPushButton(self.OpeningPanel)
        self.ReturnButton.setGeometry(QtCore.QRect(30, 650, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ReturnButton.setFont(font)
        self.ReturnButton.setAutoFillBackground(False)
        self.ReturnButton.setStyleSheet("")
        self.ReturnButton.setCheckable(False)
        self.ReturnButton.setChecked(False)
        self.ReturnButton.setAutoDefault(False)
        self.ReturnButton.setDefault(False)
        self.ReturnButton.setFlat(False)
        self.ReturnButton.setObjectName("ReturnButton")
        self.StatisticsButton = QtWidgets.QPushButton(self.OpeningPanel)
        self.StatisticsButton.setGeometry(QtCore.QRect(30, 600, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.StatisticsButton.setFont(font)
        self.StatisticsButton.setStyleSheet("")
        self.StatisticsButton.setObjectName("StatisticsButton")
        self.horizontalLayout.addWidget(self.OpeningPanel)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 160, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 230, 60, 40))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(30, 290, 60, 40))
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(30, 350, 60, 40))
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(30, 410, 60, 40))
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(30, 470, 60, 40))
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(30, 530, 60, 40))
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(30, 590, 60, 40))
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(110, 240, 800, 20))
        self.progressBar.setMaximum(2400)
        self.progressBar.setProperty("value", 439)
        self.progressBar.setObjectName("progressBar")
        self.progressBar_2 = QtWidgets.QProgressBar(self.frame)
        self.progressBar_2.setGeometry(QtCore.QRect(110, 300, 800, 20))
        self.progressBar_2.setMaximum(2400)
        self.progressBar_2.setProperty("value", 659)
        self.progressBar_2.setObjectName("progressBar_2")
        self.progressBar_3 = QtWidgets.QProgressBar(self.frame)
        self.progressBar_3.setGeometry(QtCore.QRect(110, 360, 800, 20))
        self.progressBar_3.setMaximum(2400)
        self.progressBar_3.setProperty("value", 420)
        self.progressBar_3.setObjectName("progressBar_3")
        self.progressBar_4 = QtWidgets.QProgressBar(self.frame)
        self.progressBar_4.setGeometry(QtCore.QRect(110, 420, 800, 20))
        self.progressBar_4.setMaximum(2400)
        self.progressBar_4.setProperty("value", 429)
        self.progressBar_4.setObjectName("progressBar_4")
        self.progressBar_5 = QtWidgets.QProgressBar(self.frame)
        self.progressBar_5.setGeometry(QtCore.QRect(110, 480, 800, 20))
        self.progressBar_5.setMaximum(2400)
        self.progressBar_5.setProperty("value", 310)
        self.progressBar_5.setObjectName("progressBar_5")
        self.progressBar_6 = QtWidgets.QProgressBar(self.frame)
        self.progressBar_6.setGeometry(QtCore.QRect(110, 540, 800, 20))
        self.progressBar_6.setMaximum(2400)
        self.progressBar_6.setProperty("value", 549)
        self.progressBar_6.setObjectName("progressBar_6")
        self.progressBar_7 = QtWidgets.QProgressBar(self.frame)
        self.progressBar_7.setGeometry(QtCore.QRect(110, 600, 800, 20))
        self.progressBar_7.setMaximum(2400)
        self.progressBar_7.setProperty("value", 422)
        self.progressBar_7.setObjectName("progressBar_7")
        self.horizontalLayout.addWidget(self.frame)
        self.horizontalLayout.setStretch(0, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.JurnalSubtitle.setText(_translate("Form", "Seberapa lama kamu tidur hari ini?"))
        self.JurnalTitle.setText(_translate("Form", "Riwayat Tidur"))
        self.ReturnButton.setText(_translate("Form", "Kembali"))
        self.StatisticsButton.setText(_translate("Form", "Statistik"))
        self.label.setText(_translate("Form", "Rata - rata tidur: 5.39 jam"))
        self.label_2.setText(_translate("Form", "Sun"))
        self.label_5.setText(_translate("Form", "Sat"))
        self.label_6.setText(_translate("Form", "Fri"))
        self.label_7.setText(_translate("Form", "Thu"))
        self.label_8.setText(_translate("Form", "Wed"))
        self.label_9.setText(_translate("Form", "Tue"))
        self.label_10.setText(_translate("Form", "Mon"))
        self.progressBar.setFormat(_translate("Form", "%p%"))
        self.progressBar_2.setFormat(_translate("Form", "%p%"))
        self.progressBar_3.setFormat(_translate("Form", "%p%"))
        self.progressBar_4.setFormat(_translate("Form", "%p%"))
        self.progressBar_5.setFormat(_translate("Form", "%p%"))
        self.progressBar_6.setFormat(_translate("Form", "%p%"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
