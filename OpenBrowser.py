from selenium import webdriver
from time import sleep

driver=webdriver.Firefox(executable_path='geckodriver.exe')
def Opening_Browser():
    driver.get('https://www.nitrotype.com/') #URL of the website
    sleep(6) #Depending on your internet speed you can adjust it 
