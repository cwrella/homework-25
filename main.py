from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.gismeteo.kz/weather-astana-5164/month/')

elements = browser.find_elements(By.CLASS_NAME, 'temp')
for element in elements:
    print(element.text)







from bs4 import BeautifulSoup
import requests
link = 'https://weather.com/kk-KZ/weather/monthly/l/2721102ba0e310b4c3c92a3ca37552a5b37568b1e0c859b2f10941f65fd22968'
response = requests.get(link).text
soup = BeautifulSoup(response, 'lxml')
block = soup.find('div', id='WxuCalendar-main-69bb61a5-2a5f-4a3e-879c-53f37030c238')

paragraphs = block.find_all('div', class_='CalendarDateCell--temps--16oU1')

for paragraph in paragraphs:
    print(paragraph.text)

