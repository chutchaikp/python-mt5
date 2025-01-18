
from abc import ABC, abstractmethod
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
      # print(search_symbols)
      for s in search_symbols:
        print(s.name)
      
    
   
      
  
  @abstractmethod
  def buy(self):
    pass
  
  @abstractmethod
  def sell(self):
    pass