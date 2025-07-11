from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

try:
    chrome_driver_path = "C:/Users/Acer/Desktop/chromedriver-win64/chromedriver.exe"
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)

    driver.get("https://www.tpointtech.com")
    driver.back()
    time.sleep(3)
    driver.forward()
    time.sleep(3)
    driver.get("https://www.google.com")
    driver.refresh()
    driver.quit()

except Exception as e:
    print("Error:", e)
