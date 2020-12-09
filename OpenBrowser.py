from selenium import webdriver
from time import sleep

driver=webdriver.Firefox(executable_path='geckodriver.exe')
def Opening_Browser():
    driver.get('https://www.nitrotype.com/') #URL of the website
    sleep(6) #Depending on your internet speed you can adjust it 

def RaceAsGuest():
    driver.find_element_by_xpath('//*[text()="Race as a Guest"]').click() #Race as Guest
    sleep(3)

Opening_Browser()
RaceAsGuest()