# -*- coding: utf-8 -*-
#
#  PyiiASMH 3 (mainwindow_ui.py)
#  Copyright (c) 2011, 2012, Sean Power
#  All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#      * Redistributions of source code must retain the above copyright
#        notice, this list of conditions and the following disclaimer.
#      * Redistributions in binary form must reproduce the above copyright
#        notice, this list of conditions and the following disclaimer in the
#        documentation and/or other materials provided with the distribution.
#      * Neither the names of the authors nor the
#        names of its contributors may be used to endorse or promote products
#        derived from this software without specific prior written permission.
#   
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#  ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#  WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#  DISCLAIMED. IN NO EVENT SHALL SEAN POWER BE LIABLE FOR ANY
#  DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#  (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#  ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


from PyQt5 import QtCore, QtWidgets, QtGui

class MainWindowUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.close_event = False
        self.setupUi()

    def set_close_event(self, close_event):
        self.close_event = close_event

    def closeEvent(self, event):
        if self.close_event:
            reply = QtWidgets.QMessageBox(self)
            reply.setWindowTitle("Quit PyiiASMH 3")
            reply.setText("Are you sure you want to quit?")
            reply.setInformativeText("Unsaved data will be lost.")
            reply.setIcon(QtWidgets.QMessageBox.Warning)
            reply.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            reply.setDefaultButton(QtWidgets.QMessageBox.No)

            if reply.exec_() == QtWidgets.QMessageBox.No:
                event.ignore()
            else:
                event.accept()
        else:
            event.accept()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.setWindowModality(QtCore.Qt.NonModal)
        self.setEnabled(True)
        self.resize(494, 575)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(494, 575))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setWeight(42)
        self.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("PyiiASMH.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.codeinfoLayout = QtWidgets.QGridLayout()
        self.codeinfoLayout.setHorizontalSpacing(5)
        self.codeinfoLayout.setObjectName("codeinfoLayout")
        
        #XOR Textbox
        self.xorLabel = QtWidgets.QLabel(self.centralwidget)
        self.xorLabel.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xorLabel.sizePolicy().hasHeightForWidth())
        self.xorLabel.setSizePolicy(sizePolicy)
        self.xorLabel.setMinimumSize(QtCore.QSize(80, 23))
        self.xorLabel.setMaximumSize(QtCore.QSize(16777215, 23))
        self.xorLabel.setTextFormat(QtCore.Qt.PlainText)
        self.xorLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.xorLabel.setObjectName("xorLabel")
        self.codeinfoLayout.addWidget(self.xorLabel, 0, 0, 1, 1)
        self.xorLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.xorLineEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xorLineEdit.sizePolicy().hasHeightForWidth())
        self.xorLineEdit.setSizePolicy(sizePolicy)
        self.xorLineEdit.setMinimumSize(QtCore.QSize(43, 23))
        self.xorLineEdit.setMaximumSize(QtCore.QSize(43, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setWeight(42)
        self.xorLineEdit.setFont(font)
        self.xorLineEdit.setText("")
        self.xorLineEdit.setMaxLength(4)
        self.xorLineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.xorLineEdit.setObjectName("xorLineEdit")
        self.codeinfoLayout.addWidget(self.xorLineEdit, 0, 2, 1, 1)
        self.checksumLabel = QtWidgets.QLabel(self.centralwidget)
        self.checksumLabel.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checksumLabel.sizePolicy().hasHeightForWidth())
        self.checksumLabel.setSizePolicy(sizePolicy)
        self.checksumLabel.setMinimumSize(QtCore.QSize(80, 23))
        self.checksumLabel.setMaximumSize(QtCore.QSize(16777215, 23))
        self.checksumLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.checksumLabel.setObjectName("checksumLabel")
        self.codeinfoLayout.addWidget(self.checksumLabel, 1, 0, 1, 1)
        self.checksumLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.checksumLineEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checksumLineEdit.sizePolicy().hasHeightForWidth())
        self.checksumLineEdit.setSizePolicy(sizePolicy)
        self.checksumLineEdit.setMinimumSize(QtCore.QSize(25, 23))
        self.checksumLineEdit.setMaximumSize(QtCore.QSize(25, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setWeight(42)
        self.checksumLineEdit.setFont(font)
        self.checksumLineEdit.setAutoFillBackground(False)
        self.checksumLineEdit.setText("")
        self.checksumLineEdit.setMaxLength(2)
        self.checksumLineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.checksumLineEdit.setObjectName("checksumLineEdit")
        self.codeinfoLayout.addWidget(self.checksumLineEdit, 1, 2, 1, 1)
        
        self.gridLayout.addLayout(self.codeinfoLayout, 0, 3, 1, 2)

        self.codetypeLayout = QtWidgets.QGridLayout()
        self.codetypeLayout.setObjectName("codetypeLayout")

        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 130, 271, 58))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.codetypeSelect = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.codetypeSelect.setObjectName("codetypeSelect")
        self.codetypeSelect.addItems(["", "", "", "", "", ""])

        self.codetypeSelect.setCurrentIndex(4)

        self.codetypeSelect.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "C0", None))
        self.codetypeSelect.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "04/14", None))
        self.codetypeSelect.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "06/16", None))
        self.codetypeSelect.setItemText(3, QtWidgets.QApplication.translate("MainWindow", "C2/D2", None))
        self.codetypeSelect.setItemText(4, QtWidgets.QApplication.translate("MainWindow", "F2/F4", None))
        self.codetypeSelect.setItemText(5, QtWidgets.QApplication.translate("MainWindow", "RAW", None))

        self.codetypeLayout.addWidget(self.codetypeSelect, 0, 3, 1, 1)

        #BA/PO Address textbox
        self.bapoLabel = QtWidgets.QLabel(self.centralwidget)
        self.bapoLabel.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bapoLabel.sizePolicy().hasHeightForWidth())
        self.bapoLabel.setSizePolicy(sizePolicy)
        self.bapoLabel.setMinimumSize(QtCore.QSize(100, 23))
        self.bapoLabel.setMaximumSize(QtCore.QSize(16777215, 23))
        self.bapoLabel.setTextFormat(QtCore.Qt.PlainText)
        self.bapoLabel.setScaledContents(False)
        self.bapoLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.bapoLabel.setWordWrap(True)
        self.bapoLabel.setObjectName("bapoLabel")
        self.codetypeLayout.addWidget(self.bapoLabel, 1, 0, 1, 1)
        self.bapoLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.bapoLineEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bapoLineEdit.sizePolicy().hasHeightForWidth())
        self.bapoLineEdit.setSizePolicy(sizePolicy)
        self.bapoLineEdit.setMinimumSize(QtCore.QSize(79, 23))
        self.bapoLineEdit.setMaximumSize(QtCore.QSize(79, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setWeight(42)
        self.bapoLineEdit.setFont(font)
        self.bapoLineEdit.setText("")
        self.bapoLineEdit.setMaxLength(8)
        self.bapoLineEdit.setFrame(True)
        self.bapoLineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.bapoLineEdit.setObjectName("bapoLineEdit")
        self.codetypeLayout.addWidget(self.bapoLineEdit, 1, 3, 1, 1)

        #codetype label
        self.codetypeLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.codetypeLabel.sizePolicy().hasHeightForWidth())
        self.codetypeLabel.setSizePolicy(sizePolicy)
        self.codetypeLabel.setMinimumSize(QtCore.QSize(100, 21))
        self.codetypeLabel.setMaximumSize(QtCore.QSize(16777215, 21))
        self.bapoLabel.setScaledContents(False)
        self.bapoLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.codetypeLabel.setObjectName("codetypeLabel")
        self.codetypeLayout.addWidget(self.codetypeLabel, 0, 0, 1, 1)

        self.gridLayout.addLayout(self.codetypeLayout, 0, 0, 1, 2)

        self.opcodesLayout = QtWidgets.QGridLayout()
        self.opcodesLayout.setVerticalSpacing(20)
        self.opcodesLayout.setObjectName("opcodesLayout")
        self.opcodesLabel = QtWidgets.QLabel(self.centralwidget)
        self.opcodesLabel.setMinimumSize(QtCore.QSize(100, 30))
        self.opcodesLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont("Helvetica")
        font.setPointSize(12)
        font.setWeight(82)
        font.setBold(True)
        self.opcodesLabel.setFont(font)
        self.opcodesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.opcodesLabel.setObjectName("opcodesLabel")
        self.opcodesLayout.addWidget(self.opcodesLabel, 0, 0, 1, 1)
        self.opcodesPTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.opcodesPTextEdit.setMinimumSize(QtCore.QSize(180, 311))
        self.opcodesPTextEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        font.setWeight(34)
        fontMetrics = QtGui.QFontMetricsF(font)
        spaceWidth = fontMetrics.width(' ')
        self.opcodesPTextEdit.setFont(font)
        self.opcodesPTextEdit.setTabStopDistance(spaceWidth * 4)
        self.opcodesPTextEdit.setReadOnly(False)
        self.opcodesPTextEdit.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.opcodesPTextEdit.setBackgroundVisible(False)
        self.opcodesPTextEdit.setObjectName("opcodesPTextEdit")
        self.opcodesLayout.addWidget(self.opcodesPTextEdit, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.opcodesLayout, 2, 0, 1, 1)
        self.buttonandpbarLayout = QtWidgets.QGridLayout()
        self.buttonandpbarLayout.setContentsMargins(-1, 40, -1, -1)
        self.buttonandpbarLayout.setObjectName("buttonandpbarLayout")
        self.dsmButton = QtWidgets.QPushButton(self.centralwidget)
        self.dsmButton.setMinimumSize(QtCore.QSize(40, 40))
        self.dsmButton.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont("Helvetica")
        font.setPointSize(24)
        self.dsmButton.setFont(font)
        self.dsmButton.setCheckable(False)
        self.dsmButton.setChecked(False)
        self.dsmButton.setAutoDefault(True)
        self.dsmButton.setDefault(False)
        self.dsmButton.setFlat(False)
        self.dsmButton.setObjectName("dsmButton")
        self.buttonandpbarLayout.addWidget(self.dsmButton, 1, 1, 1, 1)
        self.asmButton = QtWidgets.QPushButton(self.centralwidget)
        self.asmButton.setMinimumSize(QtCore.QSize(40, 40))
        self.asmButton.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont("Helvetica")
        font.setPointSize(24)
        self.asmButton.setFont(font)
        self.asmButton.setCheckable(False)
        self.asmButton.setChecked(False)
        self.asmButton.setAutoDefault(True)
        self.asmButton.setDefault(False)
        self.asmButton.setFlat(False)
        self.asmButton.setObjectName("asmButton")
        self.buttonandpbarLayout.addWidget(self.asmButton, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.buttonandpbarLayout, 2, 1, 1, 3)
        self.geckocodesLayout = QtWidgets.QGridLayout()
        self.geckocodesLayout.setVerticalSpacing(20)
        self.geckocodesLayout.setObjectName("geckocodesLayout")

        #geckocodes label
        self.geckocodesLabel = QtWidgets.QLabel(self.centralwidget)
        self.geckocodesLabel.setMinimumSize(QtCore.QSize(100, 30))
        self.geckocodesLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont("Helvetica")
        font.setPointSize(12)
        font.setWeight(82)
        font.setBold(True)
        self.geckocodesLabel.setFont(font)
        self.geckocodesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.geckocodesLabel.setObjectName("geckocodesLabel")
        self.geckocodesLayout.addWidget(self.geckocodesLabel, 0, 0, 1, 1)

        #geckocodes textbox
        self.geckocodesPTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.geckocodesPTextEdit.setMinimumSize(QtCore.QSize(180, 311))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setWeight(34)
        fontMetrics = QtGui.QFontMetricsF(font)
        spaceWidth = fontMetrics.width(' ')
        self.geckocodesPTextEdit.setFont(font)
        self.geckocodesPTextEdit.setTabStopDistance(spaceWidth * 4)
        self.geckocodesPTextEdit.setObjectName("geckocodesPTextEdit")
        self.geckocodesLayout.addWidget(self.geckocodesPTextEdit, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.geckocodesLayout, 2, 4, 1, 1)

        #vertical separater
        self.vertSep = QtWidgets.QFrame(self.centralwidget)
        self.vertSep.setMinimumSize(QtCore.QSize(50, 70))
        self.vertSep.setFrameShape(QtWidgets.QFrame.VLine)
        self.vertSep.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vertSep.setObjectName("vertSep")
        self.gridLayout.addWidget(self.vertSep, 0, 2, 1, 1)

        #horizontal separater
        self.horiSep = QtWidgets.QFrame(self.centralwidget)
        self.horiSep.setMinimumSize(QtCore.QSize(470, 30))
        self.horiSep.setFrameShape(QtWidgets.QFrame.HLine)
        self.horiSep.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horiSep.setObjectName("horiSep")
        self.gridLayout.addWidget(self.horiSep, 1, 0, 1, 5)

        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 494, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.menuFile.setFont(font)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.menuEdit.setFont(font)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.menuHelp.setFont(font)
        self.menuHelp.setObjectName("menuHelp")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(self)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.actionNew.setFont(font)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(self)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.actionOpen.setFont(font)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(self)
        self.actionSave.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.actionSave.setFont(font)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(self)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.actionSave_As.setFont(font)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionReload = QtWidgets.QAction(self)
        self.actionReload.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.actionReload.setFont(font)
        self.actionReload.setObjectName("actionReload")
        self.actionQuit = QtWidgets.QAction(self)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.actionQuit.setFont(font)
        self.actionQuit.setMenuRole(QtWidgets.QAction.QuitRole)
        self.actionQuit.setObjectName("actionQuit")
        self.actionUndo = QtWidgets.QAction(self)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.actionUndo.setFont(font)
        self.actionUndo.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(self)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.actionRedo.setFont(font)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCut = QtWidgets.QAction(self)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.actionCut.setFont(font)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(self)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.actionCopy.setFont(font)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(self)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.actionPaste.setFont(font)
        self.actionPaste.setObjectName("actionPaste")
        self.actionDelete = QtWidgets.QAction(self)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.actionDelete.setFont(font)
        self.actionDelete.setObjectName("actionDelete")
        self.actionSelect_All = QtWidgets.QAction(self)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.actionSelect_All.setFont(font)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.actionPreferences = QtWidgets.QAction(self)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.actionPreferences.setFont(font)
        self.actionPreferences.setMenuRole(QtWidgets.QAction.PreferencesRole)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionAbout_PyiiASMH = QtWidgets.QAction(self)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.actionAbout_PyiiASMH.setFont(font)
        self.actionAbout_PyiiASMH.setMenuRole(QtWidgets.QAction.AboutRole)
        self.actionAbout_PyiiASMH.setObjectName("actionAbout_PyiiASMH")
        self.actionAbout_Qt = QtWidgets.QAction(self)
        self.actionAbout_Qt.setStatusTip("")
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.actionAbout_Qt.setFont(font)
        self.actionAbout_Qt.setMenuRole(QtWidgets.QAction.AboutQtRole)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.actionBuiltins_Help = QtWidgets.QAction(self)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.actionBuiltins_Help.setFont(font)
        self.actionBuiltins_Help.setMenuRole(QtWidgets.QAction.AboutRole)
        self.actionBuiltins_Help.setObjectName("actionBuiltins_Help")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionReload)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionPreferences)
        self.menuHelp.addAction(self.actionAbout_PyiiASMH)
        self.menuHelp.addAction(self.actionAbout_Qt)
        self.menuHelp.addAction(self.actionBuiltins_Help)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi()

        self.codetypeSelect.currentIndexChanged.connect(self.setEditFields)

        QtCore.QMetaObject.connectSlotsByName(self)

    def setEditFields(self):
        if self.codetypeSelect.currentText() in ("C0", "RAW"):
            self.bapoLabel.setDisabled(True)
            self.bapoLineEdit.setDisabled(True)
            self.xorLabel.setDisabled(True)
            self.xorLineEdit.setDisabled(True)
            self.checksumLabel.setDisabled(True)
            self.checksumLineEdit.setDisabled(True)
        elif self.codetypeSelect.currentText() in ("04/14", "06/16", "C2/D2"):
            self.bapoLabel.setEnabled(True)
            self.bapoLineEdit.setEnabled(True)
            self.xorLabel.setDisabled(True)
            self.xorLineEdit.setDisabled(True)
            self.checksumLabel.setDisabled(True)
            self.checksumLineEdit.setDisabled(True)
        else:
            self.bapoLabel.setEnabled(True)
            self.bapoLineEdit.setEnabled(True)
            self.xorLabel.setEnabled(True)
            self.xorLineEdit.setEnabled(True)
            self.checksumLabel.setEnabled(True)
            self.checksumLineEdit.setEnabled(True)


    def retranslateUi(self):
        self.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "PyiiASMH 3 - untitled", None))
        self.bapoLabel.setText(QtWidgets.QApplication.translate("MainWindow", "   Address/Offset", None))
        self.bapoLineEdit.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "80000000", None))
        self.xorLabel.setText(QtWidgets.QApplication.translate("MainWindow", "XOR Checksum", None))
        self.xorLineEdit.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "0000", None))
        self.checksumLabel.setText(QtWidgets.QApplication.translate("MainWindow", "Before/After", None))
        self.checksumLineEdit.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "00", None))

        self.codetypeSelect.setItemText(0, QtWidgets.QApplication.translate("Dialog", "C0", None))
        self.codetypeSelect.setItemText(1, QtWidgets.QApplication.translate("Dialog", "04/14", None))
        self.codetypeSelect.setItemText(2, QtWidgets.QApplication.translate("Dialog", "06/16", None))
        self.codetypeSelect.setItemText(3, QtWidgets.QApplication.translate("Dialog", "C2/D2", None))
        self.codetypeSelect.setItemText(4, QtWidgets.QApplication.translate("Dialog", "F2/F4", None))
        self.codetypeSelect.setItemText(5, QtWidgets.QApplication.translate("Dialog", "RAW", None))

        self.codetypeLabel.setText(QtWidgets.QApplication.translate("MainWindow", "   Code Type", None))
        self.opcodesLabel.setText(QtWidgets.QApplication.translate("MainWindow", "PPC Opcodes", None))
        self.dsmButton.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Disassemble Gecko codes", None))
        self.dsmButton.setText(QtWidgets.QApplication.translate("MainWindow", "←", None))
        self.asmButton.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Assemble opcodes", None))
        self.asmButton.setText(QtWidgets.QApplication.translate("MainWindow", "→", None))
        self.geckocodesLabel.setText(QtWidgets.QApplication.translate("MainWindow", "Gecko Codes", None))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("MainWindow", "&File", None))
        self.menuEdit.setTitle(QtWidgets.QApplication.translate("MainWindow", "&Edit", None))
        self.menuHelp.setTitle(QtWidgets.QApplication.translate("MainWindow", "&Help", None))
        self.actionNew.setText(QtWidgets.QApplication.translate("MainWindow", "&New", None))
        self.actionNew.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Start a new session", None))
        self.actionNew.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+N", None))
        self.actionOpen.setText(QtWidgets.QApplication.translate("MainWindow", "&Open...", None))
        self.actionOpen.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Open a saved session", None))
        self.actionOpen.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+O", None))
        self.actionSave.setText(QtWidgets.QApplication.translate("MainWindow", "&Save", None))
        self.actionSave.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Save the current session", None))
        self.actionSave.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+S", None))
        self.actionSave_As.setText(QtWidgets.QApplication.translate("MainWindow", "Save &As...", None))
        self.actionSave_As.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Save the current session to another file", None))
        self.actionSave_As.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Shift+S", None))
        self.actionReload.setText(QtWidgets.QApplication.translate("MainWindow", "&Reload", None))
        self.actionReload.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Reload the current session from disk", None))
        self.actionReload.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+R", None))
        self.actionQuit.setText(QtWidgets.QApplication.translate("MainWindow", "&Quit", None))
        self.actionQuit.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Quit the application", None))
        self.actionQuit.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Q", None))
        self.actionUndo.setText(QtWidgets.QApplication.translate("MainWindow", "Undo", None))
        self.actionUndo.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Undo the last action", None))
        self.actionUndo.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Z", None))
        self.actionRedo.setText(QtWidgets.QApplication.translate("MainWindow", "Redo", None))
        self.actionRedo.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Redo the last action", None))
        self.actionRedo.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Shift+Z", None))
        self.actionCut.setText(QtWidgets.QApplication.translate("MainWindow", "Cut", None))
        self.actionCut.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Cuts the selected text and places it on the clipboard", None))
        self.actionCut.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+X", None))
        self.actionCopy.setText(QtWidgets.QApplication.translate("MainWindow", "Copy", None))
        self.actionCopy.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Copies the selected text and places it on the clipboard", None))
        self.actionCopy.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+C", None))
        self.actionPaste.setText(QtWidgets.QApplication.translate("MainWindow", "Paste", None))
        self.actionPaste.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Paste the contents of the clipboard", None))
        self.actionPaste.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+V", None))
        self.actionDelete.setText(QtWidgets.QApplication.translate("MainWindow", "Delete", None))
        self.actionDelete.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Deletes the selected text", None))
        self.actionSelect_All.setText(QtWidgets.QApplication.translate("MainWindow", "Select All", None))
        self.actionSelect_All.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Select all of the text", None))
        self.actionSelect_All.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+A", None))
        self.actionPreferences.setText(QtWidgets.QApplication.translate("MainWindow", "&Preferences...", None))
        self.actionPreferences.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Open the application preferences dialog", None))
        self.actionAbout_PyiiASMH.setText(QtWidgets.QApplication.translate("MainWindow", "About &PyiiASMH 3...", None))
        self.actionAbout_Qt.setText(QtWidgets.QApplication.translate("MainWindow", "About &Qt...", None))
        self.actionBuiltins_Help.setText(QtWidgets.QApplication.translate("MainWindow", "Builtins...", None))

