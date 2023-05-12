from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.locators import BmwSeacrhLocators


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
