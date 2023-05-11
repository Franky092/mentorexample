import time
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from examplekeyauto import keyautoexample

class Test_bmwstv:
    @pytest.mark.bmwstv
    @pytest.mark.bmwstvsend
    @pytest.mark.send
    def test_bmvstvsend(self,get_webdriver):
        get_webdriver.get('https://bmw-stv-keyauto.ru/podbor/')
        keyautoexample(get_webdriver)
        with allure.step("Дождаться загрузки и ввести номер телефона"):
            time.sleep(5)
            WebDriverWait(get_webdriver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div.form.b-titr__form div input'))).click()
            WebDriverWait(get_webdriver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div.form.b-titr__form div input'))).send_keys(
                '9621110149')
            pass
        with allure.step("После ввода номера нажать кнопку получть подборку"):
            time.sleep(1)
            WebDriverWait(get_webdriver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                "div.form.b-titr__form button"))).click()
            allure.attach(get_webdriver.get_screenshot_as_png(), name="Отправка", attachment_type=AttachmentType.PNG)
            pass
        with allure.step("Проверка наличие окна - спасибо"):
            time.sleep(3)
            assert WebDriverWait(get_webdriver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR,
                     "div[style*='pointer-events: auto;']")))
            pass