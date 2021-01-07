import OpenBrowser
import QualifyingRace 
from OpenBrowser import driver
from time import sleep

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
        driver.find_element_by_css_selector('.btn--gloss').click()
    except:
        try:
            driver.find_element_by_xpath('//button[text()="Race Again"]').click()
        except:
            pass
OpenBrowser.Opening_Browser()
RaceAsGuest(driver)
QualifyingRace.QualiyingRace(driver)
sleep(5)
while True:
    try:
        n=int(input("Enter the number of times you want the bot to perform race: "))
        if n<=0:
            print("You cannot {} as the value of n".format(n))
        else:
            break
    except:
        print("You cannot enter a character at this input field.\nTry Again.")
RaceAsGuest(driver)
for cnt in range(n):
    QualifyingRace.QualiyingRace(driver)
    sleep(15)
    if cnt!=(n-1):
        RaceAgain(driver)
print("The program has successfully ended.")