from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def ideti_skelbima():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://elenta.lt/registracija")
    driver.find_element(By.CLASS_NAME, "fc-button").click()

    time.sleep(2)

    driver.find_element(By.NAME, "UserName").send_keys("vardas123")
    driver.find_element(By.NAME, "Email").send_keys("vardas123@evardas123.com")
    driver.find_element(By.NAME, "Password").send_keys("Slaptazodis123")
    driver.find_element(By.NAME, "Password2").send_keys("Slaptazodis123")
    driver.find_element(By.CSS_SELECTOR, "input.button.bigNavBtn2").click()

    driver.get("https://elenta.lt/patalpinti/pasirinkti-kategorija")

    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Transporto skelbimai").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Automobiliai - Siūlau / parduodu").click()


    time.sleep(2)
    driver.find_element(By.NAME, "title").send_keys("Parduodu auto")
    driver.find_element(By.NAME, "text").send_keys("naudotas automobilis, tvarkingas")
    driver.find_element(By.NAME, "price").send_keys("120")
    driver.find_element(By.NAME, "phone").send_keys("062312561")
    driver.find_element(By.ID, "submit-button").click()
    time.sleep(2)
    driver.find_element(By.ID, "inputfile").send_keys(r"C:\Users\Vartotojas\OneDrive\Desktop\123.jpeg")
    time.sleep(2)
    driver.find_element(By.ID, "forward-button").click()

    return driver

driver = ideti_skelbima()



input()
