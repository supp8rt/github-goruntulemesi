from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()  
driver.get("https://gihtub.com/supp8rt") # buraya kendi githubunu yaz  

while True:
    sleep(1) 
    driver.refresh()  
