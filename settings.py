from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QWidget, QInputDialog, QMessageBox
from PyQt5.QtCore import QObject
import sys


class Settings(QObject):
    def setupUi(self, Widget):
        self.widget = Widget
        Widget.setObjectName("Widget")
        Widget.resize(339, 296)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        Widget.setFont(font)
        self.settingsTitle = QtWidgets.QLabel(self.widget)
        self.settingsTitle.setGeometry(QtCore.QRect(10, 0, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.settingsTitle.setFont(font)
        self.settingsTitle.setObjectName("settingsTitle")

        self.feTitle = QtWidgets.QLabel(self.widget)
        self.feTitle.setGeometry(QtCore.QRect(70, 80, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.feTitle.setFont(font)
        self.feTitle.setObjectName("feTitle")

        self.fTitle = QtWidgets.QLabel(self.widget)
        self.fTitle.setGeometry(QtCore.QRect(170, 80, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.fTitle.setFont(font)
        self.fTitle.setObjectName("fTitle")

        self.ffSplitter = QtWidgets.QFrame(self.widget)
        self.ffSplitter.setGeometry(QtCore.QRect(160, 80, 3, 61))
        self.ffSplitter.setFrameShape(QtWidgets.QFrame.VLine)
        self.ffSplitter.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.ffSplitter.setObjectName("ffSplitter")

        self.fileExtSelect = QtWidgets.QComboBox(self.widget)
        self.fileExtSelect.setGeometry(QtCore.QRect(60, 100, 90, 22))
        self.fileExtSelect.setObjectName("fileExtSelect")
        
        self.folderLabel = QtWidgets.QLabel(self.widget)
        self.folderLabel.setGeometry(QtCore.QRect(170, 100, 101, 20))
        self.folderLabel.setObjectName("folderLabel")

        self.ffTitle = QtWidgets.QLabel(self.widget)
        self.ffTitle.setGeometry(QtCore.QRect(10, 40, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.ffTitle.setFont(font)
        self.ffTitle.setObjectName("ffTitle")

        self.afeButton = QtWidgets.QPushButton(self.widget)
        self.afeButton.setGeometry(QtCore.QRect(10, 160, 141, 21))
        self.afeButton.setObjectName("afeButton")
        self.afeButton.clicked.connect(lambda: self.getUserInput("New File Extension", "Add a new file extension", "addNewItem"))

        self.efeButton = QtWidgets.QPushButton(self.widget)
        self.efeButton.setGeometry(QtCore.QRect(10, 190, 141, 21))
        self.efeButton.setObjectName("efeButton")
        self.efeButton.clicked.connect(self.editFileExtension)

        self.eafButton = QtWidgets.QPushButton(self.widget)
        self.eafButton.setGeometry(QtCore.QRect(170, 190, 161, 21))
        self.eafButton.setObjectName("eafButton")

        self.rfeButton = QtWidgets.QPushButton(self.widget)
        self.rfeButton.setGeometry(QtCore.QRect(10, 220, 141, 21))
        self.rfeButton.setObjectName("rfeButton")

        self.rmfButton = QtWidgets.QPushButton(self.widget)
        self.rmfButton.setGeometry(QtCore.QRect(170, 220, 161, 21))
        self.rmfButton.setObjectName("rmfButton")

        self.settingsSplitter1 = QtWidgets.QFrame(self.widget)
        self.settingsSplitter1.setGeometry(QtCore.QRect(0, 260, 351, 16))
        self.settingsSplitter1.setFrameShape(QtWidgets.QFrame.HLine)
        self.settingsSplitter1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.settingsSplitter1.setObjectName("settingsSplitter1")

        self.aafButton = QtWidgets.QPushButton(self.widget)
        self.aafButton.setGeometry(QtCore.QRect(170, 160, 161, 21))
        self.aafButton.setObjectName("aafButton")
        
        self.currentFolderText = "---"

        self.retranslateUi(self.widget)
        QtCore.QMetaObject.connectSlotsByName(self.widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.settingsTitle.setText(_translate("Widget", "Settings"))
        self.feTitle.setText(_translate("Widget", "File Extension"))
        self.fTitle.setText(_translate("Widget", "Associated Folder"))
        self.folderLabel.setText(_translate("Widget", self.currentFolderText))
        self.ffTitle.setText(_translate("Widget", "File:Folder Settings"))
        self.afeButton.setText(_translate("Widget", "Add File Extension"))
        self.efeButton.setText(_translate("Widget", "Edit File Extension"))
        self.eafButton.setText(_translate("Widget", "Edit Associated Folder"))
        self.rfeButton.setText(_translate("Widget", "Remove File Extension"))
        self.rmfButton.setText(_translate("Widget", "Remove Associated Folder"))
        self.aafButton.setText(_translate("Widget", "Add Associated Folder"))
    
    def populateWidgets(self):
        self.extensionFolder = {}
        ## Get current options
        with open("fileFilters.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                idx = lines.index(line)
                line = line.strip("\n").split("|")
                lines[idx] = line
            file.close()
        
        # add options to combobox
        for i in range(0, len(lines)):
            fileExt = lines[i][0]
            self.extensionFolder[fileExt] = lines[i][1]
            found = False
            for i in range(self.fileExtSelect.count()):
                if fileExt == self.fileExtSelect.itemText(i):
                    found = True
            if not found:
                self.fileExtSelect.addItem(fileExt)

        self.currentFolderText = self.extensionFolder[self.fileExtSelect.currentText()]
        self.retranslateUi(self.widget)
        
        self.fileExtSelect.currentTextChanged.connect(self.loadAssociatedFile)
    
    def showPopup(self, type, title, text):
        msgBox = QMessageBox()
        if type == "info":
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setStandardButtons(QMessageBox.Ok)
        elif type == "warn":
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgBox.setText(text)
        msgBox.setWindowTitle(title)
        msgBox.exec_()

    def loadAssociatedFile(self):
        self.currentFolderText = self.extensionFolder[self.fileExtSelect.currentText()]
        self.retranslateUi(self.widget)
    
    def clearComboBox(self):
        self.fileExtSelect.clear()

    def getUserInput(self, title, text, type):
        if type == "addNewItem":
            self.extValue, submitted = QInputDialog.getText(None, title, text)
            if submitted and self.extValue != '':
                if list(self.extValue)[0] == ".":
                        items = []
                        for ext in self.extensionFolder:
                            if self.extensionFolder[ext] not in items:
                                items.append(self.extensionFolder[ext])
                        self.folderValue, submitted = QInputDialog.getItem(None, title, text, items, 0, False)
                        if submitted and self.folderValue != '':
                            found = False # Check to make sure file ext. doesn't already exist
                            for ext in self.extensionFolder:
                                if ext == self.folderValue:
                                    found = True
                            if not found: # If file is unique
                                with open("fileFilters.txt","a") as file:
                                    file.write(f"\n{self.extValue}|{self.folderValue}")
                                self.populateWidgets()
                            else:
                                self.showPopup("info","File Extension Already Exists", "That file extension already exists!")
        elif type == "editFileExt":
            items = []
            for ext in self.extensionFolder:
                if self.extensionFolder[ext] not in items:
                    items.append(ext)
            self.selectedFileExtForEditing, submitted = QInputDialog.getItem(None, title, text, items, 0, False)
            if submitted:
                self.editedValue, submitted = QInputDialog.getText(None, "Edit File Extension", "Enter the file's edits", QLineEdit.Normal, self.selectedFileExtForEditing)
                if submitted:
                    self.extensionFolder[self.selectedFileExtForEditing] = self.editedValue
                    with open("fileFilters.txt","r") as file:
                        lines = file.readlines()
                        found = False
                        for line in lines:
                            if self.selectedFileExtForEditing in line and found == False:
                                idx = lines.index(line)
                                line = line.split("|")
                                line[0] = self.editedValue
                                newString = f"{line[0]}|{line[1]}"
                                lines[idx] = newString
                                found = True
                        file.close()
                    with open("fileFilters.txt", "w") as file:
                        for line in lines:
                            file.write(line)
                        file.close()
                    self.clearComboBox()
                    self.populateWidgets()

    
    def editFileExtension(self):
        self.getUserInput("Select file extension", "Select a file extension to edit","editFileExt")