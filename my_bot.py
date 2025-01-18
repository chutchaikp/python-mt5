
from my_bot_base import *
import MetaTrader5 as mt5

class MyBot(MyBotBase):
  def __init__(self, data = "hello"):
    self.say = data

  # def pts(self):
  #   mt5.initialize()
  #   positions=mt5.positions_get()
  #   if positions==None:
  #       print("No positions on USDCHF, error code={}".format(mt5.last_error()))
  #   elif len(positions)>0:
  #       print("Total positions on USDCHF =",len(positions))
  #       # display all open positions
  #       for position in positions:
  #           print(position)
  #   print( type(positions) )

  def buy(self):
    return "buy"
  
  def sell(self):
    return "sell"


