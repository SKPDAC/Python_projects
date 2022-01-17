import os.path
import time

import pandas as pd
from jugaad_trader import Zerodha

import KiteSettings


user_id = KiteSettings.user_id
password = KiteSettings.password
two_fa = KiteSettings.two_fa

kite = Zerodha(user_id, password, two_fa)

def retrieve():

    df = pd.read_excel("C:\\Users\\installuser\\OneDrive - IZ\\Scann-Data.xlsx", sheet_name='exit-on-4th-day')
    symbol= list(df['Symbol'][-1:])[0]
# count = list(df['Count'][-1:])[0]
    quantity= list(df['Quantity'][-1:])[0]
    return symbol, quantity

def ret_and_order():
    while(True):
        modt1 = os.path.getmtime(r"E:\\Saroj\\Automation\\ScanData\\15MIN\\Scann-Data.xlsx")
        while (True):
            modt2 = os.path.getmtime(r"E:\\Saroj\\Automation\\ScanData\\15MIN\\Scann-Data.xlsx")
            time.sleep(300)
            if modt2 != modt1:
                break
            symbol, quantity = retrieve()
            order(symbol, quantity)
# print(kite.login())
# print(kite.profile())
def order(symbol, quantity):
    order_resp = kite.place_order(variety=Zerodha.VARIETY_REGULAR,
                                   tradingsymbol="symbol",
                                   exchange=kite.EXCHANGE_NSE,
                                   transaction_type=kite.TRANSACTION_TYPE_BUY,
                                   quantity="quantity",
                                   order_type=kite.ORDER_TYPE_MARKET,
                                   product=kite.PRODUCT_CNC)
    print(order_resp)
