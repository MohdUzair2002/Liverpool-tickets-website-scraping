from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
linkslist=[]
left=[]
right=[]
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
S=Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=S,options=chrome_options)
browser.get('https://www.liverpoolfc.com/tickets/tickets-availability')
wait = WebDriverWait(browser, 60)
# element = wait.until(EC.element_to_be_clickable((By.NAME,"username")))
# cookies=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text(),'Accept All Cookies')]")))
# cookies=browser.find_element(By.XPATH,"//*[contains(text(),'Accept All Cookies')]")
# cookies.click()
# browser.execute_script("arguments[0].click();", cookies)
# time.sleep(2000)
time.sleep(35)
links=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@class='ticket-card fixture']")))
links=browser.find_elements(By.XPATH,"//a[@class='ticket-card fixture']")
title=[]
for link in links:
  title.append(link.text)
  href=link.get_attribute("href")
  linkslist.append(href)
i=0
while(i<len(linkslist)):
    browser.get(linkslist[i])
    j=0
    print(title[i])
    name_left=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='salename']")))
    name_left=browser.find_elements(By.XPATH,"//span[@class='salename']")
    for name_left1 in name_left:
     left.append(name_left1.text)
    name_right=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='status']")))
    name_right=browser.find_elements(By.XPATH,"//span[@class='status']")
    for name_right1 in name_right:

     right.append(name_right1.text)
    while(j<len(right)):
        print( f"{left[j]} : {right[j]}")
        j+=1
    if (i==(len(linkslist))-1):
        i=0
    i+=1