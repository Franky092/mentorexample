import time

from Pages.BmwPage import QuizHelper
import allure

def test_bmw_quiz(browser):
    test_bmw_quiz = QuizHelper(browser)
    with allure.step("Открыть страницу"):
        test_bmw_quiz.go_to_site()
        pass
    with allure.step("Нажать кнопку - Начать подбор"):
        test_bmw_quiz.click_on_start_button()
        pass
    with allure.step("Ответить на вопрос номер 1"):
        test_bmw_quiz.click_on_question()
        test_bmw_quiz.click_on_next_button()
        pass
    with allure.step("Ответить на вопрос номер 2"):
        time.sleep(1)
        test_bmw_quiz.click_on_question()
        test_bmw_quiz.click_on_next_button()
        pass
    with allure.step("Ответить на вопрос номер 3"):
        time.sleep(1)
        test_bmw_quiz.click_on_question()
        test_bmw_quiz.click_on_next_button()
        pass
    with allure.step("Ответить на вопрос номер 4"):
        time.sleep(1)
        test_bmw_quiz.click_on_question()
        test_bmw_quiz.click_on_next_button()
        pass
    with allure.step("Ответить на вопрос номер 4"):
        time.sleep(1)
        test_bmw_quiz.click_on_question()
        test_bmw_quiz.click_on_next_button()
        pass
    with allure.step("Дождаться загрузки и ввести номер телефона"):
        test_bmw_quiz.send_phone_number("9991110001")
        pass
    with allure.step("После ввода номера нажать кнопку получть подборку"):
        test_bmw_quiz.click_on_send_button()
        pass
    with allure.step("Проверка наличие окна - спасибо"):
        assert test_bmw_quiz.find_popup()
    pass

