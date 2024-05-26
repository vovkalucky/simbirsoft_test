import pandas as pd
import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from locators.MainPage_locators import Locators
from datetime import datetime


class MainPage(BasePage):
    locators = Locators()

    def click_customer_login(self):
        with allure.step("Click CUSTOMER_LOGIN"):
            self.element_is_visible(self.locators.CUSTOMER_LOGIN).click()

    def choose_name(self, name):
        with allure.step("Choose name"):
            select_element = self.element_is_present(self.locators.SELECT_LOGIN)
            select = Select(select_element)
            select.select_by_visible_text(name)
            self.element_is_visible(self.locators.BUTTON_SUBMIT_LOGIN).click()

    def check_login(self):
        with allure.step("Check login"):
            element = self.element_is_visible(self.locators.LOGIN)
            return element.text

    def click_deposit(self):
        with allure.step("Click DEPOSIT"):
            self.element_is_visible(self.locators.BUTTON_DEPOSIT).click()

    def enter_deposit(self, sum_of_deposit):
        with allure.step("Enter deposit"):
            self.element_is_visible(self.locators.INPUT_DEPOSIT).send_keys(sum_of_deposit)
            self.element_is_visible(self.locators.BUTTON_SUBMIT_DEPOSIT).click()
            self.refresh_page()

    def click_withdraw(self):
        with allure.step("Click WITHDRAW"):
            self.element_is_visible(self.locators.BUTTON_WITHDRAW).click()

    def enter_withdraw(self, sum_of_withdraw):
        with allure.step("Enter withdraw"):
            self.element_is_visible(self.locators.INPUT_WITHDRAW).send_keys(sum_of_withdraw)
            self.element_is_visible(self.locators.BUTTON_SUBMIT_WITHDRAW).click()

    def check_balance(self):
        with allure.step("Check balance"):
            all_elements = self.elements_are_present(self.locators.BALANCE_ALL)
            return all_elements[2].text

    def click_transaction(self):
        with allure.step("Click TRANSACTIONS"):
            self.element_is_visible(self.locators.BUTTON_TRANSACTION).click()

    def check_count_transaction(self):
        with allure.step("Check counts of transactions"):
            rows = self.elements_are_visible(self.locators.ROWS_TABLE)
            return len(rows)

    def save_in_csv(self):
        with allure.step("Save trabsactions in csv file"):
            rows = self.elements_are_visible(self.locators.ROWS_TABLE)
            data = []
            for row in rows:
                # Найдите все ячейки в строке
                cols = row.find_elements(By.TAG_NAME, 'td')
                if len(cols) == 3:
                    date_str = cols[0].text
                    amount = cols[1].text
                    transaction_type = cols[2].text
                    # Конвертация даты в нужный формат
                    date_time_obj = datetime.strptime(date_str, '%B %d, %Y %I:%M:%S %p')
                    formatted_date = date_time_obj.strftime('%d %B %Y %H:%M:%S')
                    # Добавление данных в список
                    data.append([formatted_date, amount, transaction_type])

            # Преобразование данных в DataFrame
            df = pd.DataFrame(data, columns=['Дата-времяТранзакции', 'Сумма', 'ТипТранзакции'])

            # Сохранение в CSV файл
            df.to_csv('transactions.csv', index=False, sep=',')

            print("Данные успешно сохранены в transactions.csv")

