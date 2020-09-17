from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)
wait_1 = WebDriverWait(browser, 12)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    button1 = wait_1.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button1 = browser.find_element_by_css_selector("#book")
    button1.click()
    num_input = int(browser.find_element_by_css_selector("#input_value").text)
    x = num_input
    y = calc(x)
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    button2 = browser.find_element_by_css_selector("#solve")
    button2.click()

finally:
    time.sleep(10)
    browser.quit()
