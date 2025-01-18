
from abc import ABC, abstractmethod
from multipledispatch import dispatch
import MetaTrader5 as mt5
import logging

logging.basicConfig(
  filename='log.txt',
  level=logging.INFO,
  format='%(asctime)s %(levelname)s -> %(message)s'
)

class MyBotBase(ABC):
  def __init__(self):
    pass
  
  def get_symbols(self, ticker = ""):
    logging.info("get_symbols has been accessed!")
    mt5.initialize()        
    if len(ticker) > 0:
      key = f"*{ticker}*"
      search_symbols=mt5.symbols_get(key)
      print('len: ', len(search_symbols))
      print( 'type: ', type(search_symbols) )
      for x in search_symbols:
        print(x.name)
    else:
      search_symbols=mt5.symbols_get()      
      print( 'type: ', type(search_symbols) )      
      for s in search_symbols:
        print(s.name)
          
  def desc(self):
    mt5.initialize()
    
    print()
    print(mt5.last_error())
    
    print()
    print(mt5.account_info())
    
    print()
    print(mt5.terminal_info())
    
    print("MetaTrader5 package author: ",mt5.__author__)
    print("MetaTrader5 package version: ",mt5.__version__)
    print()
    print(mt5.version())
    print()

    symbol = "GOLD#"
    # symbol = "BTCUSD#"

    print(f"symbol: {symbol}")
    
    path = mt5.symbol_info(symbol).path
    print(f"path: {path}")
    print()
    
    leverage = mt5.account_info().leverage
    print(f"LEVERAGE: {leverage}")
    
    trade_size = mt5.symbol_info(symbol).trade_contract_size
    print(f"TRADE SIZE: {trade_size}")
    
    min_lot = mt5.symbol_info(symbol).volume_min
    print(f"MIN LOT: {min_lot}")
    
    max_lot = mt5.symbol_info(symbol).volume_max
    print(f"MAX LOT: {max_lot}")

    price = (mt5.symbol_info(symbol).ask + mt5.symbol_info(symbol).bid)/2
    print(f"PRICE: {price}")

    # bid = mt5.symbol_info(symbol).bid
    bid = mt5.symbol_info_tick(symbol).bid
    print(f"bid: {bid}")
    
    ask = mt5.symbol_info_tick(symbol).ask
    print(f"ask: {ask}")
    
    spread = bid - ask
    print(f"spread: { abs(spread)}")
    
  @dispatch()
  def get_position_count(self):
    try:
      mt5.initialize()
      positions_total=mt5.positions_total()
      if positions_total>0:
          print("Total positions=",positions_total)
      else:
          print("Positions not found")
    except Exception as ex:
      logging.error( repr(ex) )
      print( repr(ex) )
      
  #  = "GOLD#"
  @dispatch(str)
  def get_position_count(self, symbol):
    try:
      mt5.initialize()
      positions_total=mt5.positions_total(symbol)
      if positions_total>0:
          print("Total positions=",positions_total)
      else:
          print("Positions not found")
    except Exception as ex:
      logging.error( repr(ex) )
      print( repr(ex) )
    
  def position_exist(self, symbol = "GOLD#", order_type = mt5.ORDER_TYPE_BUY):
    return True
        
  @abstractmethod
  def buy(self):
    pass
  
  @abstractmethod
  def sell(self):
    pass