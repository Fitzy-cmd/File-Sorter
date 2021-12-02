from typing import Match
from PyQt5.QtCore import QObject, QThread, pyqtSignal as signal
import os, shutil

class Sorter(QObject):
    finished = signal()
    progress = signal()

    def start(self, pathStr):
        self.filters = {}
        self.path = pathStr
        self.loadFileFilters()
        self.checkFolderPaths()
        for filename in os.listdir(self.path):
            currentFilePath = os.path.join(self.path, filename)
            if os.path.isfile(currentFilePath):
                for fileExt in self.filters:
                    if fileExt in filename:
                        newFilePath = os.path.join(self.path, self.filters[fileExt])
                        shutil.move(currentFilePath, newFilePath)
                self.progress.emit()
        self.finished.emit()
    
    def loadFileFilters(self):
        with open("fileFilters.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip("\n")
                fileExt, folder = line.split("|")
                if fileExt not in self.filters:
                    self.filters[fileExt] = folder
    
    def checkFolderPaths(self):
        print(self.filters)
        for fileExt in self.filters:
            folderpath = os.path.join(self.path, self.filters[fileExt])
            if not os.path.exists(folderpath):
                os.makedirs(folderpath)
            
        

class sizeToString():
    def __init__(self,size):
        self.size = size

        self.sizeTypes = {
            "bytes":self.bytes(),
            "kilobytes":self.kilo(),
            "megabytes":self.mega(),
            "gigabytes":self.giga(),
            "terabytes":self.tera(),
            "petabytes":self.peta()
        }
        self.determineSize()
        
    def determineSize(self):
        if self.size >= 1000000000000000:
            size = "petabytes"
        elif self.size >= 1000000000000:
            size = "terabytes"
        elif self.size >= 1000000000:
            size = "gigabytes"
        elif self.size >= 1000000:
            size = "megabytes"
        elif self.size >= 1000:
            size = "kilobytes"
        else:
            size = "bytes"

        self.sizeString = self.sizeTypes[size]
    
    def bytes(self):
        return f"{self.size} bytes"
    
    def kilo(self):
        return f"{round(self.size / 1000)}KB"
    
    def mega(self):
        return f"{round(self.size / 1000000)}MB"
    
    def giga(self):
        return f"{round(self.size / 1000000000)}GB"
    
    def tera(self):
        return f"{round(self.size / 1000000000000)}TB"
    
    def peta(self):
        return f"{round(self.size / 1000000000000000)}PB"