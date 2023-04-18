# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jurnal_tmp_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import Jurnal
import JurnalController
import JurnalCreateForm
from custom import UIWindow


class Ui_Form(UIWindow):
    def setupUi(self, Form):
        self.jurnalController = JurnalController.JurnalController()

        Form.setObjectName("Jurnal Menu")
        Form.resize(1280, 786)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.OpeningPanel = QtWidgets.QFrame(Form)
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
        self.JurnalSubtitle.setGeometry(QtCore.QRect(30, 128, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.JurnalSubtitle.setFont(font)
        self.JurnalSubtitle.setWordWrap(True)
        self.JurnalSubtitle.setObjectName("JurnalSubtitle")
        self.JurnalTitle = QtWidgets.QLabel(self.OpeningPanel)
        self.JurnalTitle.setGeometry(QtCore.QRect(30, 64, 142, 35))
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
        self.line = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(40, 64, 20, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border: 1px solid rgb(130, 130, 130);\n"
"    padding-left: 10px;\n"
"    font: 11pt \"MS Shell Dlg 2\";\n"
"    min-height: 50px;\n"
"    text-align: left;\n"
"\n"
"    margin-left: 20px;\n"
"    margin-right: 30px;\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgb(215, 215, 215);\n"
"}\n"
"QPushButton:pressed {\n"
"    background: rgb(200, 200, 200);\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.createNewJurnal)

        self.verticalLayout.addWidget(self.pushButton)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setStyleSheet("QLabel {\n"
"    border: 1px solid rgb(130, 130, 130);\n"
"    padding-left: 10px;\n"
"    font: 11pt \"MS Shell Dlg 2\";\n"
"    min-height: 50px;\n"
"    text-align: left;\n"
"\n"
"    margin-left: 10px;\n"
"}\n"
"QLabel:hover {\n"
"    background: rgb(215, 215, 215);\n"
"}\n"
"QLabel:pressed {\n"
"    background: rgb(200, 200, 200);\n"
"}")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 856, 888))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(self.spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(2, 3)
        
        self.jurnalController.foreach(self.insertLabel)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.JurnalSubtitle.setText(_translate("Form", "Apa yang kamu pikirkan hari ini?"))
        self.JurnalTitle.setText(_translate("Form", "Jurnal"))
        self.ReturnButton.setText(_translate("Form", "Kembali"))
        self.StatisticsButton.setText(_translate("Form", "Statistik"))
        self.pushButton.setText(_translate("Form", "+          Tambah Jurnal Baru"))

    def createNewJurnal(self):
        try:
            self.jurnalController.checkToday()
            self._onswitch('Home')
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Terjadi kesalahan!")
            msg.setText(str(e))
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.exec_()

    def insertLabel(self, jurnal: Jurnal.Jurnal):
        newLabel = jurnal.createLabel()
        newLabel.parent = self.scrollAreaWidgetContents

        self.verticalLayout_2.removeItem(self.spacerItem)
        self.verticalLayout_2.addWidget(newLabel)
        self.verticalLayout_2.addItem(self.spacerItem)

        newLabel.show()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
