from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
import urllib.parse
import pymysql
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

search = "대복집"
conn = pymysql.connect(host='localhost',
                                 user='dwk9181',
                                 password='',
                                 database='final_db',
                                 )



cur = conn.cursor()
sql1 = "select name from landmarkapp_restaurants"

sql = "select address from landmarkapp_restaurants where name = %s"
cur.execute(sql, search)
output = cur.fetchall()


for i in output:
    output = i

    for i in output:
         output = i


conn.close

search1 = search + ' ' + output

encode = urllib.parse.quote_plus(search1)

driver = webdriver.Chrome('C:/Users/82108/Downloads/chromedriver_win32 (1)/chromedriver.exe')
driver.get("https://map.naver.com/v5/search/" + encode)

##################################
driver.implicitly_wait(3)



driver.switch_to.frame("entryIframe")




response = driver.page_source
soup = BeautifulSoup(response, 'html.parser')



for i in soup.select('#app-root > div > div > div.place_detail_wrapper > div:nth-child(4) > div > div.place_section.no_margin > div > ul > li._1M_Iz'):

    print(i.text)


# response = urlopen("https://map.naver.com/v5/search/" + encode)
#
# soup = BeautifulSoup(response, 'html.parser')
#
# soup.select("span._3ZA0S")
#
# print(soup)






