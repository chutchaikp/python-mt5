
import MetaTrader5 as mt5
from my_bot import MyBot

mb = MyBot()

# mb.get_symbols("BRENT")
# mb.desc()
# mb.get_position_count("BTCUSD#")
# mb.position_count()
# mb.get_positions("GOLD#")
# mb.positions_get()
# mb.position_exist(order_type=None, symbol="BTCUSD#")

# {

positions = mb.position_get_by("GOLD#", mt5.POSITION_TYPE_SELL)
if positions is not None and len(positions) > 0:
  # try to delete first position
  first = positions[0]
  result = mb.position_close(first)
  print("-----------------{")
  print(result)
  print(type(result)) # retcode=10009 - Request completed
  print("-----------------}")
else:
  print("position is None")
  
# }

# mb.type_check()




# mb.get_point("GOLD#") 
# # 0.01
# mb.get_point("BTCUSD#") 

# mb.order_check(order_type=mt5.ORDER_TYPE_BUY, symbol="GOLD#")
# retcode=10016 mean Invalid stops in the request
# ***** sl must greater than abs (bid - ask)


