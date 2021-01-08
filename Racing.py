from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def Race(driver,inputdelay):
    try:
        driver.find_element_by_xpath('//*[text()="Start Qualifying Race"]').click()
    except:
        pass
    try:
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.dash-copy')))
    except:
        print("Something went wrong \nQuiting Program")
        exit()
    typingtab=driver.find_element_by_css_selector('.dash-copy')
    driver.find_element_by_css_selector('.dash-copy-input').click() #clicks on the input tab
    inputtab=driver.find_element_by_css_selector('.dash-copy-input')
    words=typingtab.find_elements_by_css_selector('.dash-word')
    for word in words:
        errorcnt=0
        while True:
            try:
                letter=word.find_element_by_css_selector('.is-waiting').text
                inputtab.send_keys(letter)
                sleep(inputdelay)
                errorcnt=0
            except:
                try:
                    letter=word.find_element_by_css_selector('.is-waiting').text
                    inputtab.send_keys(letter)
                    sleep(inputdelay)
                    errorcnt=0
                    try:
                        letter=word.find_element_by_css_selector('.is-incorrect').text
                        inputtab.send_keys(letter)
                        sleep(inputdelay)
                    except:
                        pass
                except:
                    errorcnt+=1
                    if errorcnt==5:
                        break

    print("Race has successfully ended.")