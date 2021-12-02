from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import requests, re, webbrowser, os
from pathlib import Path
import functions
__version__ = "0.0.3"
__beta__ = True


class GUI(object):
    def setupUi(self, Widget):
        self.widget = Widget
        self.widget.setObjectName("Widget")
        self.widget.resize(434, 411)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        self.widget.setFont(font)
        
        self.title = QtWidgets.QLabel(self.widget)
        self.title.setGeometry(QtCore.QRect(10, 0, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        
        self.updateButton = QtWidgets.QPushButton(self.widget)
        self.updateButton.setGeometry(QtCore.QRect(290, 10, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        self.updateButton.setFont(font)
        self.updateButton.setObjectName("updateButton")
        self.updateButton.clicked.connect(self.update)

        self.selectDirectoryButton = QtWidgets.QPushButton(self.widget)
        self.selectDirectoryButton.setGeometry(QtCore.QRect(329, 60, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        self.selectDirectoryButton.setFont(font)
        self.selectDirectoryButton.setObjectName("selectDirectoryButton")
        self.selectDirectoryButton.clicked.connect(self.selectDirectory)

        self.settingsButton = QtWidgets.QPushButton(self.widget)
        self.settingsButton.setGeometry(QtCore.QRect(350, 90, 80, 21))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        self.settingsButton.setFont(font)
        self.settingsButton.setObjectName("settingsButton")
        self.settingsButton.setEnabled(False)

        self.cdTitle = QtWidgets.QLabel(self.widget)
        self.cdTitle.setGeometry(QtCore.QRect(10, 120, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cdTitle.setFont(font)
        self.cdTitle.setObjectName("cdTitle")
        
        self.nofTitle = QtWidgets.QLabel(self.widget)
        self.nofTitle.setGeometry(QtCore.QRect(10, 140, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.nofTitle.setFont(font)
        self.nofTitle.setObjectName("nofTitle")

        self.etTitle = QtWidgets.QLabel(self.widget)
        self.etTitle.setGeometry(QtCore.QRect(10, 180, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.etTitle.setFont(font)
        self.etTitle.setObjectName("etTitle")

        self.tdsTitle = QtWidgets.QLabel(self.widget)
        self.tdsTitle.setGeometry(QtCore.QRect(10, 160, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tdsTitle.setFont(font)
        self.tdsTitle.setObjectName("tdsTitle")

        self.sortProgress = QtWidgets.QProgressBar(self.widget)
        self.sortProgress.setGeometry(QtCore.QRect(100, 210, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(8)
        self.sortProgress.setFont(font)
        self.sortProgress.setProperty("value", 0)
        self.sortProgress.setObjectName("sortProgress")

        self.startButton = QtWidgets.QPushButton(self.widget)
        self.startButton.setGeometry(QtCore.QRect(10, 210, 80, 31))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.startButton.clicked.connect(self.beginSort)
        self.startButton.setEnabled(False)

        self.fcTitle = QtWidgets.QLabel(self.widget)
        self.fcTitle.setGeometry(QtCore.QRect(10, 250, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.fcTitle.setFont(font)
        self.fcTitle.setObjectName("fcTitle")

        self.ttTitle = QtWidgets.QLabel(self.widget)
        self.ttTitle.setGeometry(QtCore.QRect(10, 290, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.ttTitle.setFont(font)
        self.ttTitle.setObjectName("ttTitle")

        self.trTitle = QtWidgets.QLabel(self.widget)
        self.trTitle.setGeometry(QtCore.QRect(10, 310, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.trTitle.setFont(font)
        self.trTitle.setObjectName("trTitle")

        self.cdLabel = QtWidgets.QLabel(self.widget)
        self.cdLabel.setGeometry(QtCore.QRect(120, 120, 311, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.cdLabel.setFont(font)
        self.cdLabel.setObjectName("cdLabel")

        self.cdButton = QtWidgets.QPushButton(self.widget)
        self.cdButton.setGeometry(QtCore.QRect(120, 120, 311, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.cdButton.setFont(font)
        self.cdButton.setObjectName("cdButton")
        self.cdButton.clicked.connect(lambda: self.showPopup("info", "Full Directory Path", self.dirString))
        self.cdButton.hide()
        

        self.nofLabel = QtWidgets.QLabel(self.widget)
        self.nofLabel.setGeometry(QtCore.QRect(110, 140, 71, 20))
        self.nofLabel.setObjectName("nofLabel")

        self.tdsLabel = QtWidgets.QLabel(self.widget)
        self.tdsLabel.setGeometry(QtCore.QRect(130, 160, 71, 20))
        self.tdsLabel.setObjectName("tdsLabel")

        self.etLabel = QtWidgets.QLabel(self.widget)
        self.etLabel.setGeometry(QtCore.QRect(110, 180, 171, 20))
        self.etLabel.setObjectName("etLabel")

        self.fcLabel = QtWidgets.QLabel(self.widget)
        self.fcLabel.setGeometry(QtCore.QRect(140, 250, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.fcLabel.setFont(font)
        self.fcLabel.setObjectName("fcLabel")

        self.ttLabel = QtWidgets.QLabel(self.widget)
        self.ttLabel.setGeometry(QtCore.QRect(110, 290, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.ttLabel.setFont(font)
        self.ttLabel.setObjectName("ttLabel")

        self.trLabel = QtWidgets.QLabel(self.widget)
        self.trLabel.setGeometry(QtCore.QRect(140, 310, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.trLabel.setFont(font)
        self.trLabel.setObjectName("trLabel")

        self.cdTitle_2 = QtWidgets.QLabel(self.widget)
        self.cdTitle_2.setGeometry(QtCore.QRect(10, 40, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cdTitle_2.setFont(font)
        self.cdTitle_2.setObjectName("cdTitle_2")

        self.dir, self.fileCount, self.dirSize, self.estimatedTime, \
            self.filesCompleted, self.timeTaken, self.timeRemaining = "---", "---", "---", "---", "---", "---", "---"

        self.retranslateUi(self.widget)
        self.checkForUpdate()
        QtCore.QMetaObject.connectSlotsByName(self.widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.title.setText(_translate("Widget", "File AutoSorter"))
        self.updateButton.setText(_translate("Widget", "PushButton"))
        self.selectDirectoryButton.setText(_translate("Widget", "Select Directory"))
        self.settingsButton.setText(_translate("Widget", "Settings"))
        self.cdTitle.setText(_translate("Widget", "Current Directory:"))
        self.nofTitle.setText(_translate("Widget", "Number of Files: "))
        self.etTitle.setText(_translate("Widget", "Estimated Time:"))
        self.tdsTitle.setText(_translate("Widget", "Total Directory Size: "))
        self.startButton.setText(_translate("Widget", "Start Sort"))
        self.fcTitle.setText(_translate("Widget", "Files Completed:"))
        self.ttTitle.setText(_translate("Widget", "Time Taken:"))
        self.trTitle.setText(_translate("Widget", "Time Remaining:"))
        self.cdLabel.setText(_translate("Widget", f"{self.dir}"))
        self.cdButton.setText(_translate("Widget", f"{self.dir}"))
        self.nofLabel.setText(_translate("Widget", f"{self.fileCount}"))
        self.tdsLabel.setText(_translate("Widget", f"{self.dirSize}"))
        self.etLabel.setText(_translate("Widget", f"{self.estimatedTime}"))
        self.fcLabel.setText(_translate("Widget", f"{self.filesCompleted}"))
        self.ttLabel.setText(_translate("Widget", f"{self.timeTaken}"))
        self.trLabel.setText(_translate("Widget", f"{self.timeRemaining}"))
        self.cdTitle_2.setText(_translate("Widget", "A project by Silveridge"))
    
    def checkForUpdate(self):
        _translate = QtCore.QCoreApplication.translate
        self.updateButton.setDisabled(True)
        self.updateButton.setText(_translate("Widget", "Checking for update..."))

        try:
            r = requests.get("https://raw.githubusercontent.com/Silveridge/File-Sorter/main/gui.py")

            remoteVersion = str(re.findall('__version__ = "(.*)"', r.text)[0])
            localVersion = __version__

            if __beta__:
                self.updateButton.setText(_translate("Widget", "Update Beta Version"))
                self.updateButton.setDisabled(False)
            else:
                if remoteVersion != localVersion:
                    self.updateButton.setDisabled(False)
                    self.updateButton.setText(_translate("Widget", "Update Available!"))
                else:
                    self.updateButton.setText(_translate("Widget", "No update available"))
        except Exception as e:
            print("Update search failed, aborting.")
    
    def update(self):
        webbrowser.open("https://github.com/Silveridge/File-Sorter/releases")
    
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
    
    def selectDirectory(self):
        self.dirString = str(QFileDialog.getExistingDirectory(None, "Select Directory"))
        if self.dir != "":
            self.setDirStats()
            self.retranslateUi(self.widget)
    
    def setDirStats(self):
        # CD, # of Files, Dir Size, est Time
        self.dir = Path(self.dirString)
        if len(list(self.dirString)) >= 50:
            self.cdLabel.hide()
            self.cdButton.show()
        else:
            self.cdLabel.show()
            self.cdButton.hide()
        self.fileCount = 0 # Total Files
        self.dirSize = 0 # Bytes
        for path in Path(self.dir).iterdir():
            if path.is_file():
                self.fileCount += 1
                self.dirSize += path.stat().st_size
        
        
        self.dirSize = functions.sizeToString(self.dirSize).sizeString

        self.startButton.setEnabled(True)
    
    def beginSort(self):
        self.thread = QThread()
        self.worker = functions.Sorter()
        self.progressSegment = int(100/int(self.fileCount))
        

        ## Begin Thread
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(lambda: self.worker.start(self.dirString))
        self.worker.finished.connect(self.thread.quit)
        self.worker.progress.connect(self.progress)
        self.thread.finished.connect(self.fin)
        self.thread.start()
    
    def fin(self):
        self.sortProgress.setValue(100)
    
    def progress(self):
        self.sortProgress.setValue(self.sortProgress.value() + self.progressSegment)