from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_france_button_name(browser):
    browser.get(link)
    time.sleep(5)
    button = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert button is not None


