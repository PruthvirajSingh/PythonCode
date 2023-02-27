import configparser

config=configparser.RawConfigParser()
# config.read(".\\Configration\config.ini")
config.read("C:/Users/Pruthvirajsing/PycharmProjects/pythonProject2/Configration/config.ini")
class ReadConfig():
    @staticmethod
    def readBaseUrl():
        url=config.get("common info","baseURL")
        return url
    @staticmethod
    def readUserName():
        username=config.get("common info","username")
        return username
    @staticmethod
    def readPassword():
        password=config.get("common info","password")
        return password