
from my_bot_base import *
import MetaTrader5 as mt5

class MyBot(MyBotBase):
  def __init__(self, data = "day:GOLD#:sell:-20"):
    self.data = data
    x = data.split(":")
    if len(x) >= 4:
      self.period = x[0]
      self.symbol = x[1] 
      # GOLD# or XAUUSD
      self.order_type = mt5.ORDER_TYPE_BUY if x[2] == "buy" else mt5.ORDER_TYPE_SELL
      self.sl = float(x[3])

  def buy(self):
    # todo: check balance and stop loss issues
    self.order_check(order_type=self.order_type, symbol=self.symbol, sl=self.sl)
    # todo: if retcode != 0, check from 
    # https://www.mql5.com/en/docs/constants/errorswarnings/enum_trade_return_codes
    
    return "buy"
  
  def sell(self):
    return "sell"
  
  def execute(self):
    if self.order_type == mt5.ORDER_TYPE_BUY:
      self.buy()
    else:
      self.sell()
      
    return "buy or sell ?"


