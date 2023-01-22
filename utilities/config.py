import configparser
import os

config = configparser.RawConfigParser()
path = os.getcwd().replace("\\testCases","") + "\\config\\config.ini"
config.read(path)

class readConfig():
    @staticmethod
    def getBase_url():
        return config.get("common info", "base_url")