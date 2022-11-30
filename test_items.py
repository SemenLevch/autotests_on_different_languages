from selenium.webdriver.common.by import By
import time

def test_add_to_card_button_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    browser.get(link)
    time.sleep(3)
    add_to_card_button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")

    assert add_to_card_button

