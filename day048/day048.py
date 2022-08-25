from bs4 import BeautifulSoup
from selenium.webdriver import ChromeOptions, Chrome
from selenium import webdriver
import time

options=ChromeOptions()
options.headless=True
driver=webdriver.Chrome(executable_path=r'C:\Users\singh\Downloads\chromedriver_win32\chromedriver.exe')
driver.get('https://twitter.com/narendramodi')
time.sleep(5)
soup=BeautifulSoup(driver.page_source,"html.parser")
all=soup.find_all('span')
a=0
for i in all:
    print(f'{a} -- {i.text}')
    a+=1



