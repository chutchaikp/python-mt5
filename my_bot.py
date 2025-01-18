
from my_bot_base import *
import MetaTrader5 as mt5

class MyBot(MyBotBase):
  def __init__(self, data = "hello"):
    self.say = data

  def get_say(self):
    return self.say

  def get_ask(self):
    mt5.initialize()    
    return mt5.symbol_info_tick("GOLD#").ask
  
  def get_bid(self):
    mt5.initialize()    
    return mt5.symbol_info_tick("GOLD#").bid
  
  def get_other(self):
    return "hello"
  


  def pts(self):
    mt5.initialize()
    positions=mt5.positions_get()
    if positions==None:
        print("No positions on USDCHF, error code={}".format(mt5.last_error()))
    elif len(positions)>0:
        print("Total positions on USDCHF =",len(positions))
        # display all open positions
        for position in positions:
            print(position)

    print( type(positions) )

  # def get_positions(self):   
    
  #   if mt5.last_error():
  #     print(mt5.last_error())

  #   if mt5.initialize():
  #     search_symbols=mt5.symbols_get()
  #     #  "*GOL*")
  #     print('len: ', len(search_symbols))
  #     for s in search_symbols:
  #       print(s.name)
  #       print()
  #   else:
  #     print("failed")
  
  def buy(self):
    return "buy"
  
  def sell(self):
    return "sell"


