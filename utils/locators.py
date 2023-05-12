from selenium.webdriver.common.by import By
class BmwSeacrhLocators:
    LOCATOR_BMW_START_BUTTON = (By.CSS_SELECTOR, "div.slick-active div.button.b-titr__button")
    LOCATOR_BMW_NEXT_BUTTON = (By.CSS_SELECTOR, "div.slick-active div div.b-titr__footer div.button")
    LOCATOR_BMW_QUESTION = (By.CSS_SELECTOR, 'div.slick-active div  div label:nth-child(3)')
    LOCATOR_BMW_PHONE = (By.CSS_SELECTOR, 'div.form.b-titr__form div input')
    LOCATOR_BMW_SEND_BUTTON = (By.CSS_SELECTOR, "div.form.b-titr__form button")
    LOCATOR_BMW_POPUP = (By.CSS_SELECTOR, "div[style*='pointer-events: auto;']")