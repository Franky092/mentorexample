import time
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def keyautoexample(get_webdriver):
    with allure.step("Нажать кнопку - Начать подбор"):
        time.sleep(1)
        WebDriverWait(get_webdriver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.slick-active div.button.b-titr__button"))).click()
        allure.attach(get_webdriver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
        pass
    with allure.step("Выбрать элемент и нажать кнопку Далее"):
        time.sleep(1)
        WebDriverWait(get_webdriver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            'div.slick-active div  div label:nth-child(3)'))).click()
        get_webdriver.find_element(By.CSS_SELECTOR,
                                   'div.slick-active div div.b-titr__footer div.button').click()
        pass
    with allure.step("Выбрать второй элемент и нажать кнопку Далее"):
        time.sleep(1)
        WebDriverWait(get_webdriver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            'div.slick-active div  div label:nth-child(3)'))).click()
        get_webdriver.find_element(By.CSS_SELECTOR,
                                   'div.slick-active div div.b-titr__footer div.button').click()
        pass
    with allure.step("Выбрать трейтий элемент и нажать кнопку Далее"):
        time.sleep(1)
        WebDriverWait(get_webdriver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            'div.slick-active div  div label:nth-child(3)'))).click()
        get_webdriver.find_element(By.CSS_SELECTOR,
                                   'div.slick-active div div.b-titr__footer div.button').click()
        pass
    with allure.step("Выбрать четвертый и нажать кнопку Далее"):
        time.sleep(1)
        WebDriverWait(get_webdriver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            'div.slick-active div  div label:nth-child(3)'))).click()
        get_webdriver.find_element(By.CSS_SELECTOR,
                                   'div.slick-active div div.b-titr__footer div.button').click()
        pass

