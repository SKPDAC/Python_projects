from openpyxl import Workbook
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdrivermanager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from datetime import datetime

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://chartink.com/screener/bbsq10c-test")
driver.implicitly_wait(10)
SymbolName=driver.find_elements(By.XPATH,"//a[contains(@class,'text-teal-700') and not (@title)]/parent::*/following-sibling::td//a[contains(@class,'text-teal-700') and not (@title)]")
Prices=driver.find_elements(By.XPATH,"//td[contains(@class,'sorting_1')]")
now = datetime.now()

MySymbol=[]
MyPrice=[]

for Symbol in SymbolName:
    MySymbol.append(Symbol.text)

print("*"*50)

for Price in Prices:
    MyPrice.append(Price.text)

FinalList=zip(MySymbol,MyPrice)

wb=Workbook()
wb['Sheet'].title='bbsq10c'
sh1=wb.active

sh1.append(['Symbol','Price'])
for x in list(FinalList):
    sh1.append(x)
wb.save("bbsq10c-test.xlsx")