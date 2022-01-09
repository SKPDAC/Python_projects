import pandas as pd
from jugaad_trader import Zerodha

import KiteSettings

user_id = KiteSettings.user_id
password = KiteSettings.password
two_fa = KiteSettings.two_fa

kite = Zerodha(user_id, password, two_fa)

# print(kite.login())
# print(kite.profile())

# order_resp = kite.place_order(variety=Zerodha.VARIETY_REGULAR,
#                               tradingsymbol="INFY",
#                               exchange=kite.EXCHANGE_NSE,
#                               transaction_type=kite.TRANSACTION_TYPE_BUY,
#                               quantity="1",
#                               order_type=kite.ORDER_TYPE_MARKET,
#                               product=kite.PRODUCT_CNC)
# print(order_resp)
