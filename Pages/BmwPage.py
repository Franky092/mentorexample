from utils.BaseApp import BasePage
from selenium.webdriver.common.by import By


class BmwSeacrhLocators:
    LOCATOR_BMW_START_BUTTON = (By.CSS_SELECTOR, "div.slick-active div.button.b-titr__button")
    LOCATOR_BMW_NEXT_BUTTON = (By.CSS_SELECTOR, "div.slick-active div div.b-titr__footer div.button")
    LOCATOR_BMW_QUESTION = (By.CSS_SELECTOR, 'div.slick-active div  div label:nth-child(3)')
    LOCATOR_BMW_PHONE = (By.CSS_SELECTOR, 'div.form.b-titr__form div input')
    LOCATOR_BMW_SEND_BUTTON = (By.CSS_SELECTOR, "div.form.b-titr__form button")
    LOCATOR_BMW_POPUP = (By.CSS_SELECTOR, "div[style*='pointer-events: auto;']")


class QuizHelper(BasePage):

    def click_on_start_button(self):
        return self.find_element(BmwSeacrhLocators.LOCATOR_BMW_START_BUTTON, time=2).click()

    def click_on_question(self):
        return self.find_element(BmwSeacrhLocators.LOCATOR_BMW_QUESTION, time=2).click()

    def click_on_next_button(self):
        return self.find_element(BmwSeacrhLocators.LOCATOR_BMW_NEXT_BUTTON, time=5).click()

    def send_phone_number(self, phone):
        phoneadd = self.find_element(BmwSeacrhLocators.LOCATOR_BMW_PHONE)
        phoneadd.click()
        phoneadd.send_keys(phone)
        return phoneadd

    def click_on_send_button(self):
        return self.find_element(BmwSeacrhLocators.LOCATOR_BMW_SEND_BUTTON, time=5).click()

    def find_popup(self):
        return self.find_element(BmwSeacrhLocators.LOCATOR_BMW_POPUP, time=10)
