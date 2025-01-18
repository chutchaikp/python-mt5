
import MetaTrader5 as mt5
from my_bot import MyBot

m = MyBot()

# m.get_symbols("BTC")
# m.desc()
# m.get_position_count("BTCUSD#")
# m.position_count()
# m.get_positions("GOLD#")
# m.get_positions()
# m.position_exist(order_type=None, symbol="BTCUSD#")

# m.get_point("GOLD#") 
# 0.01
# m.get_point("BTCUSD#") 

m.order_check(order_type=mt5.ORDER_TYPE_BUY, symbol="GOLD#")
# retcode=10016 mean Invalid stops in the request
# ***** sl must greater than abs (bid - ask)


