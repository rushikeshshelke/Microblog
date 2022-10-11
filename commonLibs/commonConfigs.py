import os
import json

class CommonConfigs:

    def createDir(self,path):
        if os.path.isdir(path) == False:
            os.makedirs(path)
    
    def readJson(self,filename):
        with open(filename,'r') as file:
            jsonData = json.load(file)
        return jsonData