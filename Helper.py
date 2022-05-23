import json
class Helper():
    def getApiKey(self, keyName):
        with open('config.json') as json_file:
            data = json.load(json_file)
        return data[keyName]