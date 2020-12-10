from time import sleep

def QualiyingRace(driver):
    driver.find_element_by_xpath('//*[text()="Start Qualifying Race"]').click()
    sleep(6)
    while True:
        x=1
        while True:
            try:
                letter=driver.find_element_by_xpath('/html/body/div[1]/div/main/div/section/div[3]/div[1]/div[1]/div[2]/div[2]/div/span[{}]/span[1]'.format(x)).text
            except:
                break
            y=1
            while True:
                try:
                    letter=driver.find_element_by_xpath('/html/body/div[1]/div/main/div/section/div[3]/div[1]/div[1]/div[2]/div[2]/div/span[{}]/span[{}]'.format(x,y))
                    driver.find_element_by_xpath('/html/body/div[1]/div/main/div/section/div[3]/div[1]/div[1]/div[2]/input').send_keys(letter)
                    print(letter)
                    y+=1
                except:
                    break
            x+=1