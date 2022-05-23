import sqlite3, requests, time
from Helper import Helper


class Stocks():
    def __init__(self):
        self.initialInvestment = 0
        self.currentTotalValue = 0
        self.difference = 0
        self.weeklyGain = 0
        self.monthlyGain = 0
        self.dailyGain = 0
        helper = Helper()

        self.url = "https://yh-finance.p.rapidapi.com/stock/v3/get-statistics"
        self.headers = {
            "X-RapidAPI-Host": "yh-finance.p.rapidapi.com",
            "X-RapidAPI-Key": helper.getApiKey("yahooApiKey")
        }

        self.con = sqlite3.connect('stocks.db')
        self.cursor = self.con.cursor() 

    def options(self):
        print("Please select an option\n====================\n1) Add a stock\n"
        + "2) Sell a stock\n")

    def getCurrentPrice(self, symbol):
        querystring = {"symbol": symbol}
        response = requests.request("GET", self.url, headers=self.headers, params=querystring)
        requestData = response.json()
        return requestData["price"]["regularMarketPrice"]["raw"]

    def selectStock(self, symbol):
        return self.cursor.execute("SELECT * FROM STOCKS WHERE symbol = \"" + symbol + "\"")


    def addStock(self, symbol, name, price, quantity):
        currentPrice = str(price)
        if self.selectStock(symbol) is None:
            self.cursor.execute("INSERT INTO STOCKS VALUES (\'" + symbol + "\', \'" + name + "\', " + str(quantity)
            + ", " + currentPrice + ", + " + currentPrice + ", " + currentPrice + ", " + currentPrice + ", " + currentPrice + ")")
            self.con.commit()
        else:
            self.cursor.execute("UPDATE STOCKS SET qty = qty + " +  str(quantity) + ", moneyInvested = moneyInvested + " 
            + currentPrice + " WHERE symbol = \'" + symbol + "\'")
            self.con.commit()


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
    
    def update(self):
        immediateTime = time.localtime()
        self.addStock('AAPL', 'Apple', 100, 1)
        for row in self.selectStock('AAPL'):  
            print(row)
