
from abc import ABC, abstractmethod
# from multipledispatch import dispatch
# from typing import overload
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
    
    if mt5.initialize():
            
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

      bid = mt5.symbol_info_tick(symbol).bid
      print(f"bid: {bid}")
      
      ask = mt5.symbol_info_tick(symbol).ask
      print(f"ask: {ask}")
      
      spread = bid - ask
      print(f"spread: { abs(spread)}")
      
    else:
      print("MT5 init failed :(")
      
  
  
  # --------------------------
  def get_position_all_count(self):
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
  def get_position_count(self, symbol=None):
    try:
      mt5.initialize()
      print(symbol)
      print(type(symbol))
      print(f"symbol is None: {symbol is None}")
      # quit()
      
      if symbol is None:
        positions_total=mt5.positions_total()
        if positions_total>0:
            print("Total positions=",positions_total)
        else:
            print("Positions not found")
      else:
        # positions_total(symbol) is NOT WORKING
        positions_total=mt5.positions_total(symbol)
        if positions_total>0:
            print(f"Total {symbol} positions=",positions_total)
        else:
            print("Positions not found")
    except Exception as ex:
      logging.error( repr(ex) )
      print( repr(ex) )
  
  def get_positions(self, symbol=None ):
    mt5.initialize()
    if symbol is None:
      # "GOLD#"
      positions=mt5.positions_get()
      if positions is None:
        print("No positions, error code={}".format(mt5.last_error()))
      else:
        for position in positions:
          # 0 BUY position, 1 SELL position
          # if position.type == 1:                      
          # print(type(position))          
          print(f"{position.symbol} {position.type} {position.volume}" ) 
          # print(position)
        return positions
    else:
      positions=mt5.positions_get(symbol=symbol)
      print("OK---", len(positions))
      return positions
    
    return None
    
    
  def position_close_by_ticket(self):
    pass
  
  def position_exist(self, order_type = mt5.ORDER_TYPE_BUY, symbol = None ):
    positions = self.get_positions(symbol=symbol)
    # 0 BUY
    # 1 SELL    
    print("len: ", len(positions))
    count = 0
    for p in positions:
      if p.type == 1:
        count = count + 1
    
    print(f"sell: {count}")    

    return True
  
  def order_check(self, order_type = mt5.ORDER_TYPE_BUY, symbol=None, sl = 0):
    # prepare the request structure
    # symbol="GOLD#"
    mt5.initialize()
    
    symbol_info = mt5.symbol_info(symbol)  
    if symbol_info is None:
      print(symbol, "not found, can not call order_check()")
      # mt5.shutdown()
      quit()
    
    # if the symbol is unavailable in MarketWatch, add it
    if not symbol_info.visible:
      print(symbol, "is not visible, trying to switch on")
      if not mt5.symbol_select(symbol,True):
          print("symbol_select({}}) failed, exit",symbol)
          mt5.shutdown()
          quit()
        
    # prepare the request
    spread = abs( mt5.symbol_info_tick(symbol).bid-mt5.symbol_info_tick(symbol).ask )
    # sl must greater than abs(bid - ask)    
    point=mt5.symbol_info(symbol).point
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": 1.0,
        "type": mt5.ORDER_TYPE_BUY,
        "price": mt5.symbol_info_tick(symbol).ask,
        "sl": mt5.symbol_info_tick(symbol).ask-spread,
        "tp": mt5.symbol_info_tick(symbol).ask+spread,
        "deviation": 20,
        "magic": 234000,
        "comment": "python script",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    
    # perform the check and display the result 'as is'
    result = mt5.order_check(request)
    print(result)
    print()
    
    result_dict=result._asdict()
    retcode = result_dict.get("retcode")
    
    print( f"retcode is {retcode}"  )
    print(f" {order_type} price: {mt5.symbol_info_tick(symbol).ask} sl: {mt5.symbol_info_tick(symbol).ask-spread} tp: {mt5.symbol_info_tick(symbol).ask+spread} ")
    print(f"spread: {mt5.symbol_info_tick(symbol).bid-mt5.symbol_info_tick(symbol).ask}")
    
  def get_point(self, symbol):
    mt5.initialize()
    point=mt5.symbol_info(symbol).point
    print(f"point: {point}")
    
        
  @abstractmethod
  def buy(self):
    pass
  
  @abstractmethod
  def sell(self):
    pass


  @abstractmethod
  def execute(self):
    pass  
  