import os
import time
from modules.fibo import fibonacci_for_today
from modules.current_day import current_day
from modules.attach_trans import attach_trans
from pages.main_page import MainPage
import allure


@allure.feature('Main page login')
class TestMainPageLogin:
    @allure.title('Test login')
    def test_login(self, driver):
        page = MainPage(driver, 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
        page.open()
        page.click_customer_login()
        page.choose_name("Harry Potter")
        assert page.check_login() == "Harry Potter"


@allure.feature('Main page deposit')
class TestMainPageDeposit:
    @allure.title('Test deposit')
    def test_deposit(self, driver):
        page = MainPage(driver, 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
        page.open()
        page.click_customer_login()
        page.choose_name("Harry Potter")
        page.click_deposit()
        page.enter_deposit(fibonacci_for_today(current_day()))
        page.click_withdraw()
        page.enter_withdraw(fibonacci_for_today(current_day()))
        assert page.check_balance() == '0'


@allure.feature('Main page transactions')
class TestMainPageTransactions:
    @allure.title('Test transactions')
    def test_transaction(self, driver):
        page = MainPage(driver, 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
        page.open()
        page.click_customer_login()
        page.choose_name("Harry Potter")
        page.click_deposit()
        page.enter_deposit(fibonacci_for_today(current_day()))
        page.click_withdraw()
        page.enter_withdraw(fibonacci_for_today(current_day()))
        time.sleep(1)
        page.click_transaction()
        assert page.check_count_transaction() == 2
        page.save_in_csv()
        attach_trans()





