# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(876, 558)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.caesars_input = QtWidgets.QTextBrowser(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.caesars_input.sizePolicy().hasHeightForWidth()
        )
        self.caesars_input.setSizePolicy(sizePolicy)
        self.caesars_input.setMaximumSize(QtCore.QSize(568, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.caesars_input.setFont(font)
        self.caesars_input.setReadOnly(False)
        self.caesars_input.setObjectName("caesars_input")
        self.verticalLayout.addWidget(self.caesars_input)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.shift = QtWidgets.QSpinBox(self.tab_3)
        self.shift.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.shift.setMinimum(0)
        self.shift.setMaximum(31)
        self.shift.setProperty("value", 1)
        self.shift.setObjectName("shift")
        self.horizontalLayout.addWidget(self.shift)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.shift_try = QtWidgets.QSpinBox(self.tab_3)
        self.shift_try.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.shift_try.setMinimum(0)
        self.shift_try.setMaximum(31)
        self.shift_try.setProperty("value", 1)
        self.shift_try.setObjectName("shift_try")
        self.horizontalLayout_2.addWidget(self.shift_try)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.caesars_encode = QtWidgets.QPushButton(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.caesars_encode.setFont(font)
        self.caesars_encode.setMouseTracking(True)
        self.caesars_encode.setStyleSheet(
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(120, 183, 140);\n"
            "border-radius: 20px;\n"
            "border: 2px solid #094065;"
        )
        self.caesars_encode.setObjectName("caesars_encode")
        self.verticalLayout_4.addWidget(self.caesars_encode)
        self.caesars_decode = QtWidgets.QPushButton(self.tab_3)
        self.caesars_decode.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.caesars_decode.setFont(font)
        self.caesars_decode.setMouseTracking(True)
        self.caesars_decode.setStyleSheet(
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(120, 183, 140);\n"
            "border-radius: 20px;\n"
            "border: 2px solid #094065;"
        )
        self.caesars_decode.setObjectName("caesars_decode")
        self.verticalLayout_4.addWidget(self.caesars_decode)
        self.caesars_cryptanalysis = QtWidgets.QPushButton(self.tab_3)
        self.caesars_cryptanalysis.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.caesars_cryptanalysis.setFont(font)
        self.caesars_cryptanalysis.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.caesars_cryptanalysis.setStyleSheet(
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(120, 183, 140);\n"
            "border-radius: 20px;\n"
            "border: 2px solid #094065;"
        )
        self.caesars_cryptanalysis.setObjectName("caesars_cryptanalysis")
        self.verticalLayout_4.addWidget(self.caesars_cryptanalysis)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.caesars_output = QtWidgets.QTextBrowser(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.caesars_output.sizePolicy().hasHeightForWidth()
        )
        self.caesars_output.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.caesars_output.setFont(font)
        self.caesars_output.setReadOnly(True)
        self.caesars_output.setObjectName("caesars_output")
        self.verticalLayout_5.addWidget(self.caesars_output)
        self.verticalLayout_8.addLayout(self.verticalLayout_5)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.caesars_load = QtWidgets.QPushButton(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.caesars_load.setFont(font)
        self.caesars_load.setStyleSheet(
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(120, 183, 140);\n"
            "border-radius: 20px;\n"
            "border: 2px solid #094065;"
        )
        self.caesars_load.setObjectName("caesars_load")
        self.verticalLayout_7.addWidget(self.caesars_load)
        self.caesars_save = QtWidgets.QPushButton(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.caesars_save.setFont(font)
        self.caesars_save.setStyleSheet(
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(120, 183, 140);\n"
            "border-radius: 20px;\n"
            "border: 2px solid #094065;"
        )
        self.caesars_save.setObjectName("caesars_save")
        self.verticalLayout_7.addWidget(self.caesars_save)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.horizontalLayout_5.addLayout(self.verticalLayout_8)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.vigenere_input = QtWidgets.QTextBrowser(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.vigenere_input.sizePolicy().hasHeightForWidth()
        )
        self.vigenere_input.setSizePolicy(sizePolicy)
        self.vigenere_input.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.vigenere_input.setFont(font)
        self.vigenere_input.setReadOnly(False)
        self.vigenere_input.setObjectName("vigenere_input")
        self.verticalLayout_2.addWidget(self.vigenere_input)
        self.verticalLayout_12.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.key = QtWidgets.QLineEdit(self.tab_4)
        self.key.setInputMask("")
        self.key.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.key.setCursorPosition(4)
        self.key.setClearButtonEnabled(True)
        self.key.setObjectName("key")
        self.horizontalLayout_3.addWidget(self.key)
        self.verticalLayout_12.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.key_try = QtWidgets.QLineEdit(self.tab_4)
        self.key_try.setAutoFillBackground(False)
        self.key_try.setInputMethodHints(QtCore.Qt.ImhNone)
        self.key_try.setClearButtonEnabled(True)
        self.key_try.setObjectName("key_try")
        self.horizontalLayout_4.addWidget(self.key_try)
        self.verticalLayout_12.addLayout(self.horizontalLayout_4)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.vigenere_encode = QtWidgets.QPushButton(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.vigenere_encode.setFont(font)
        self.vigenere_encode.setStyleSheet(
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(120, 183, 140);\n"
            "border-radius: 20px;\n"
            "border: 2px solid #094065;"
        )
        self.vigenere_encode.setObjectName("vigenere_encode")
        self.verticalLayout_10.addWidget(self.vigenere_encode)
        self.vigenere_decode = QtWidgets.QPushButton(self.tab_4)
        self.vigenere_decode.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.vigenere_decode.setFont(font)
        self.vigenere_decode.setStyleSheet(
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(120, 183, 140);\n"
            "border-radius: 20px;\n"
            "border: 2px solid #094065;"
        )
        self.vigenere_decode.setObjectName("vigenere_decode")
        self.verticalLayout_10.addWidget(self.vigenere_decode)
        self.vigenere_visualize_entropy = QtWidgets.QPushButton(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.vigenere_visualize_entropy.setFont(font)
        self.vigenere_visualize_entropy.setStyleSheet(
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(120, 183, 140);\n"
            "border-radius: 20px;\n"
            "border: 2px solid #094065;"
        )
        self.vigenere_visualize_entropy.setObjectName("vigenere_visualize_entropy")
        self.verticalLayout_10.addWidget(self.vigenere_visualize_entropy)
        self.verticalLayout_12.addLayout(self.verticalLayout_10)
        self.horizontalLayout_6.addLayout(self.verticalLayout_12)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_10 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_11.addWidget(self.label_10)
        self.vigenere_output = QtWidgets.QTextBrowser(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.vigenere_output.sizePolicy().hasHeightForWidth()
        )
        self.vigenere_output.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vigenere_output.setFont(font)
        self.vigenere_output.setReadOnly(True)
        self.vigenere_output.setObjectName("vigenere_output")
        self.verticalLayout_11.addWidget(self.vigenere_output)
        self.verticalLayout_13.addLayout(self.verticalLayout_11)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.vigenere_entropy = QtWidgets.QLineEdit(self.tab_4)
        self.vigenere_entropy.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.vigenere_entropy.setFont(font)
        self.vigenere_entropy.setDragEnabled(False)
        self.vigenere_entropy.setReadOnly(True)
        self.vigenere_entropy.setObjectName("vigenere_entropy")
        self.horizontalLayout_8.addWidget(self.vigenere_entropy)
        self.verticalLayout_14.addLayout(self.horizontalLayout_8)
        self.vigenere_load = QtWidgets.QPushButton(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.vigenere_load.setFont(font)
        self.vigenere_load.setStyleSheet(
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(120, 183, 140);\n"
            "border-radius: 20px;\n"
            "border: 2px solid #094065;"
        )
        self.vigenere_load.setObjectName("vigenere_load")
        self.verticalLayout_14.addWidget(self.vigenere_load)
        self.vigenere_save = QtWidgets.QPushButton(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.vigenere_save.setFont(font)
        self.vigenere_save.setStyleSheet(
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(120, 183, 140);\n"
            "border-radius: 20px;\n"
            "border: 2px solid #094065;"
        )
        self.vigenere_save.setObjectName("vigenere_save")
        self.verticalLayout_14.addWidget(self.vigenere_save)
        self.verticalLayout_13.addLayout(self.verticalLayout_14)
        self.horizontalLayout_6.addLayout(self.verticalLayout_13)
        self.verticalLayout_15.addLayout(self.horizontalLayout_6)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 400))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_16.addWidget(self.tableWidget)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.bitwise_input = QtWidgets.QTextBrowser(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.bitwise_input.sizePolicy().hasHeightForWidth()
        )
        self.bitwise_input.setSizePolicy(sizePolicy)
        self.bitwise_input.setMaximumSize(QtCore.QSize(568, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.bitwise_input.setFont(font)
        self.bitwise_input.setReadOnly(False)
        self.bitwise_input.setObjectName("bitwise_input")
        self.verticalLayout_3.addWidget(self.bitwise_input)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.bitwise_encode = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.bitwise_encode.setFont(font)
        self.bitwise_encode.setStyleSheet(
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(120, 183, 140);\n"
            "border-radius: 20px;\n"
            "border: 2px solid #094065;"
        )
        self.bitwise_encode.setObjectName("bitwise_encode")
        self.verticalLayout_21.addWidget(self.bitwise_encode)
        self.bitwise_decode = QtWidgets.QPushButton(self.tab)
        self.bitwise_decode.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.bitwise_decode.setFont(font)
        self.bitwise_decode.setStyleSheet(
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(120, 183, 140);\n"
            "border-radius: 20px;\n"
            "border: 2px solid #094065;"
        )
        self.bitwise_decode.setObjectName("bitwise_decode")
        self.verticalLayout_21.addWidget(self.bitwise_decode)
        self.bitwise_visualize = QtWidgets.QPushButton(self.tab)
        self.bitwise_visualize.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.bitwise_visualize.setFont(font)
        self.bitwise_visualize.setStyleSheet(
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(120, 183, 140);\n"
            "border-radius: 20px;\n"
            "border: 2px solid #094065;"
        )
        self.bitwise_visualize.setObjectName("bitwise_visualize")
        self.verticalLayout_21.addWidget(self.bitwise_visualize)
        self.verticalLayout_3.addLayout(self.verticalLayout_21)
        self.horizontalLayout_7.addLayout(self.verticalLayout_3)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_12 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_19.addWidget(self.label_12)
        self.bitwise_output = QtWidgets.QTextBrowser(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.bitwise_output.sizePolicy().hasHeightForWidth()
        )
        self.bitwise_output.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bitwise_output.setFont(font)
        self.bitwise_output.setReadOnly(True)
        self.bitwise_output.setObjectName("bitwise_output")
        self.verticalLayout_19.addWidget(self.bitwise_output)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.bitwise_load = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.bitwise_load.setFont(font)
        self.bitwise_load.setStyleSheet(
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(120, 183, 140);\n"
            "border-radius: 20px;\n"
            "border: 2px solid #094065;"
        )
        self.bitwise_load.setObjectName("bitwise_load")
        self.verticalLayout_20.addWidget(self.bitwise_load)
        self.bitwise_save = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.bitwise_save.setFont(font)
        self.bitwise_save.setStyleSheet(
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(120, 183, 140);\n"
            "border-radius: 20px;\n"
            "border: 2px solid #094065;"
        )
        self.bitwise_save.setObjectName("bitwise_save")
        self.verticalLayout_20.addWidget(self.bitwise_save)
        self.verticalLayout_19.addLayout(self.verticalLayout_20)
        self.horizontalLayout_7.addLayout(self.verticalLayout_19)
        self.verticalLayout_16.addLayout(self.horizontalLayout_7)
        self.verticalLayout_18.addLayout(self.verticalLayout_16)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout_17.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Входной текст"))
        self.caesars_input.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;"><br /></p></body></html>',
            )
        )
        self.label.setText(_translate("MainWindow", "Сдвиг для кодирования"))
        self.label_2.setText(_translate("MainWindow", "Сдвиг для декодирования"))
        self.caesars_encode.setText(_translate("MainWindow", "Encode"))
        self.caesars_decode.setText(_translate("MainWindow", "Decode"))
        self.caesars_cryptanalysis.setText(_translate("MainWindow", "Сryptanalysis"))
        self.label_6.setText(_translate("MainWindow", "Выходной текст"))
        self.caesars_output.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;"><br /></p></body></html>',
            )
        )
        self.caesars_load.setText(_translate("MainWindow", "Load"))
        self.caesars_save.setText(_translate("MainWindow", "Save"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Шифр Цезаря")
        )
        self.label_7.setText(_translate("MainWindow", "Входной текст"))
        self.vigenere_input.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;"><br /></p></body></html>',
            )
        )
        self.label_3.setText(_translate("MainWindow", "Ключ для кодирования"))
        self.key.setText(_translate("MainWindow", "КЛЮЧ"))
        self.label_4.setText(_translate("MainWindow", "Ключ для декодирования"))
        self.key_try.setText(_translate("MainWindow", "КЛЮЧ"))
        self.vigenere_encode.setText(_translate("MainWindow", "Encode"))
        self.vigenere_decode.setText(_translate("MainWindow", "Decode"))
        self.vigenere_visualize_entropy.setText(
            _translate("MainWindow", "Visualize Entropy")
        )
        self.label_10.setText(_translate("MainWindow", "Выходной текст"))
        self.vigenere_output.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;"><br /></p></body></html>',
            )
        )
        self.label_9.setText(_translate("MainWindow", "Энтропия"))
        self.vigenere_load.setText(_translate("MainWindow", "Load"))
        self.vigenere_save.setText(_translate("MainWindow", "Save"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_4),
            _translate("MainWindow", "Шифр Виженера"),
        )
        self.label_8.setText(_translate("MainWindow", "Входной текст"))
        self.bitwise_input.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;"><br /></p></body></html>',
            )
        )
        self.bitwise_encode.setText(_translate("MainWindow", "Encode"))
        self.bitwise_decode.setText(_translate("MainWindow", "Decode"))
        self.bitwise_visualize.setText(_translate("MainWindow", "Visualize"))
        self.label_12.setText(_translate("MainWindow", "Выходной текст"))
        self.bitwise_output.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;"><br /></p></body></html>',
            )
        )
        self.bitwise_load.setText(_translate("MainWindow", "Load"))
        self.bitwise_save.setText(_translate("MainWindow", "Save"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab),
            _translate("MainWindow", "Побитовые операции"),
        )