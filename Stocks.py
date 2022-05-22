import sqlite3, requests, json, time

class Stocks():
    def __init__(self):
        self.initialInvestment = 0
        self.currentTotalValue = 0
        self.difference = 0
        self.weeklyGain = 0
        self.monthlyGain = 0
        self.dailyGain = 0

        self.url = "https://yh-finance.p.rapidapi.com/stock/v3/get-statistics"
        self.headers = {
            "X-RapidAPI-Host": "yh-finance.p.rapidapi.com",
            "X-RapidAPI-Key": self.getApiKey("yahooApiKey")
        }

        self.con = sqlite3.connect('stocks.db')
        self.cursor = self.con.cursor() 

    def options(self):
        print("Please select an option\n====================\n1) Add a stock\n"
        + "2) Sell a stock\n")

    def addStock(self, symbol, name, price, quantity):
        currentPrice = str(self.getCurrentPrice(symbol))
        self.cursor.execute("INSERT INTO STOCKS VALUES (\'" + symbol + "\', \'" + name + "\', " + str(quantity)
        + ", " + str(price) + ", + " + currentPrice + ", " + currentPrice + ", " + currentPrice + ", " + currentPrice + ")")

    def createTable(self): 
        self.cursor.execute("CREATE TABLE STOCKS(symbol text, name text, qty real,"
        + " moneyInvested real, currentPrice real, morningPrice real, mondayPrice real, monthPrice real)")
        self.con.commit()

    def updateMorningPrice(self,):
        print("success")

    def updateMondayPrice(self):
        print("success")

    def updateMonthlyPrice(self):
        print("success")
    
    def getCurrentPrice(self, symbol):
        querystring = {"symbol": symbol}
        response = requests.request("GET", self.url, headers=self.headers, params=querystring)
        requestData = response.json()
        return requestData["price"]["regularMarketPrice"]["raw"]


    def getApiKey(self, keyName):
        with open('config.json') as json_file:
            data = json.load(json_file)
        return data[keyName]

    def update(self):
        immediateTime = time.localtime()
        print(immediateTime)
        print("Updated!")

stock = Stocks()

stock.update()
