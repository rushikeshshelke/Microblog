import logging

from commonLibs.globalvariables import GlobalVariables
from datetime import date
from commonLibs.commonConfigs import CommonConfigs
from logging.handlers import RotatingFileHandler

class InitialiseLogging:

    def setupLogging(self):
        logDirPath = GlobalVariables.APP_LOGS_PATH+"/"+str(date.today())
        CommonConfigs().createDir(logDirPath)
        appConfigFilePath = "{}/appConfigs.json".format(GlobalVariables.APP_CONFIG_PATH)
        jsonData = CommonConfigs().readJson(appConfigFilePath)
        log_path = "{}/{}".format(logDirPath,jsonData['filename'])
        handler = RotatingFileHandler(log_path,maxBytes=jsonData['maxSize'],backupCount=jsonData['rotateCount'])
        handler.setFormatter(logging.Formatter(jsonData['logFormat']))
        GlobalVariables.LOGGER = logging.getLogger(jsonData['appName'])
        GlobalVariables.LOGGER.setLevel(logging.DEBUG)

        if not GlobalVariables.LOGGER.hasHandlers():
            GlobalVariables.LOGGER.addHandler(handler)