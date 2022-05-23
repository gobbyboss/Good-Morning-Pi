import Stocks
from time import sleep

class Goodmorning():
    def __init__(self):
        self.stocks = Stocks.Stocks()
    
    def run(self):
        self.stocks.update()

client = Goodmorning()
while True:
    client.run()
    sleep(20)