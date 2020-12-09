from time import sleep

def QualiyingRace(driver):
    driver.find_element_by_xpath('//*[text()="Start Qualifying Race"]').click()
    sleep(5)
