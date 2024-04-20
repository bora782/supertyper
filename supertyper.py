from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keyboard
import time

browser = webdriver.Firefox()  
browser.get("https://10ff.net")

inputElement = browser.find_element(By.XPATH, f'//*[@id="username"]')
inputElement.send_keys('spiderman1984') # your username here
inputElement.send_keys(Keys.ENTER)

while True:
    the_text = []
    time.sleep(2)

    try:
        for i in range(1000):
            value = browser.find_element(By.XPATH, f'/html/body/div/div/div[3]/div[2]/div[1]/div/span[{i+1}]')
            inner_html = value.get_attribute('innerHTML')
            the_text.append(inner_html)
            the_text.append(" ")

    except:
        print("text saved")  

    try:
        waittime_element = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div")))
        waittime = waittime_element.text

        if waittime.isdigit():
            time.sleep(float(waittime) + 0.001)

            for word in the_text:
                keyboard.write(word)
                time.sleep(0.01)
            print("done\n")

    except:
        if "Waiting for additional players." in browser.page_source:
            print("Waiting for players...")
        else:
            pass

    time.sleep(5)
    browser.refresh()