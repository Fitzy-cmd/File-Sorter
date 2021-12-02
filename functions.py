from typing import Match


class sizeToString():
    def __init__(self,size):
        self.sizeTypes = {
            "bytes":self.bytes(),
            "kilobytes":self.kilo(),
            "megabytes":self.mega(),
            "gigabytes":self.giga(),
            "terabytes":self.tera(),
            "petabytes":self.peta(),
        }
        self.size = size
    
    def determineSize(self):
        #1000000000000000
        pass