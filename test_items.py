import pytest
from selenium import webdriver
import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('language', ["236895/step/1", "236896/step/1", "236897/step/1", "236898/step/1",  "236899/step/1", "236903/step/1", "236904/step/1", "236905/step/1"])
def test_entertime(browser, language):
    link = f"https://stepik.org/lesson/{language}/"
    browser.get(link)
    textar = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.TAG_NAME, "textarea"))
    )
    answer = math.log(int(time.time()))
    textar.send_keys(str(answer))
    submit_but = browser.find_element_by_class_name("submit-submission")
    submit_but.click()
    message = WebDriverWait(browser, 2).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "smart-hints__hint"))
    )
    print(message.text)
    assert "Correct" in message.text
