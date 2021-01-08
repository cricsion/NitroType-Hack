import OpenBrowser
import Racing 
from OpenBrowser import driver
from time import sleep

while True:#To input the typing speed
    try:
        speed=int(input("Enter the typing speed(in WPM): "))
        if speed<=0:
            print("Speed cannot be negative.\nTry Again.")
        else:
            break
    except ValueError:
        print("You cannot enter a character at this input field.\nTry Again.")

sleeptime=60/(speed*6)

def RaceAsGuest(driver):
    try:
        driver.find_element_by_xpath('//*[text()="Race as a Guest"]').click() #Race as Guest
    except:
        try:
            driver.find_element_by_css_selector('.tooltip').click() #Race as Guest
        except:
            pass
    sleep(3)
def RaceAgain(driver):
    try:
        driver.find_element_by_css_selector('.btn--gloss').click()#clicks on the Race Again button
    except:
        try:
            driver.find_element_by_xpath('//button[text()="Race Again"]').click()
        except:
            pass
OpenBrowser.Opening_Browser()
RaceAsGuest(driver)
Racing.Race(driver,sleeptime)
sleep(5)
while True:
    try:
        n=int(input("Enter the number of times you want the bot to perform: "))
        if n<=0:
            print("You cannot {} as the value of n".format(n))
        else:
            break
    except ValueError:
        print("You cannot enter a character at this input field.\nTry Again.")
RaceAsGuest(driver)
for cnt in range(n):
    Racing.Race(driver,sleeptime)
    sleep(15)
    if cnt!=(n-1):
        RaceAgain(driver)
print("The program has successfully ended.")