import os
from modules.fibo import fibonacci_for_today
from pages.main_page import MainPage
import allure


@allure.feature('Main page')
class TestMainPage:
    @allure.title('Test login')
    def test_login(self, driver):
        page = MainPage(driver, 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
        page.open()
        page.click_customer_login()
        page.choose_name("Harry Potter")
        assert page.check_login() == "Harry Potter"

    @allure.title('Test deposit')
    def test_deposit(self, driver):
        page = MainPage(driver, 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
        page.open()
        page.click_customer_login()
        page.choose_name("Harry Potter")
        page.click_deposit()
        page.enter_deposit(fibonacci_for_today())
        page.click_withdraw()
        page.enter_withdraw(fibonacci_for_today())
        assert page.check_balance() == '0'

    @allure.title('Test transactions')
    def test_transaction(self, driver):
        page = MainPage(driver, 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
        page.open()
        page.click_customer_login()
        page.choose_name("Harry Potter")
        page.click_deposit()
        page.enter_deposit(fibonacci_for_today())
        page.click_withdraw()
        page.enter_withdraw(fibonacci_for_today())
        page.refresh_page()
        page.click_transaction()
        assert page.check_count_transaction() == 2
        file_path = "/home/vladimir/PycharmProjects/simbirsoft_test/modules/transactions.csv"
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                content = file.read()
                allure.attach(content, name='trans.csv', attachment_type=allure.attachment_type.CSV)




