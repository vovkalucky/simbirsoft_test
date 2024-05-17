from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select


#### LOCATORS

CUSTOMER_LOGIN = (By.CSS_SELECTOR, "[ng-click='customer()']")
SELECT_LOGIN = (By.CSS_SELECTOR, "#userSelect")
BUTTON_SUBMIT_LOGIN = (By.CSS_SELECTOR, "[type='submit']")
BUTTON_DEPOSIT = (By.CSS_SELECTOR, "[ng-click='deposit()']")
INPUT_DEPOSIT = (By.CSS_SELECTOR, "[type='number']")
BUTTON_SUBMIT_DEPOSIT = (By.CSS_SELECTOR, "[type='submit']")
DEPOSIT_SUCCESSFUL = (By.CSS_SELECTOR, ".error.ng-binding")
BUTTON_WITHDRAW = (By.CSS_SELECTOR, "[ng-click='withdrawl()']")
INPUT_WITHDRAW = (By.CSS_SELECTOR, "[type='number']")
BUTTON_SUBMIT_WITHDRAW = (By.CSS_SELECTOR, "[type='submit']")
BALANCE_ALL = (By.CSS_SELECTOR, ".ng-binding")
BUTTON_TRANSACTION = (By.CSS_SELECTOR, "[ng-click='transactions()']")
TABLE_OF_TRANSACTIONS = (By.CSS_SELECTOR, "table.table-bordered.table-striped")
ROWS_TABLE = (By.CSS_SELECTOR, "tbody tr")
LOGIN = (By.CSS_SELECTOR, ".fontBig.ng-binding")

##### LOCATORS END

class MainPage(BasePage):
    def click_customer_login(self):
        self.element_is_visible(CUSTOMER_LOGIN).click()

    def choose_name(self, name):
        select_element = self.element_is_present(SELECT_LOGIN)
        select = Select(select_element)
        select.select_by_visible_text(name)
        self.element_is_visible(BUTTON_SUBMIT_LOGIN).click()

    def check_login(self):
        element = self.element_is_visible(LOGIN)
        return element.text

    def click_deposit(self):
        self.element_is_visible(BUTTON_DEPOSIT).click()

    def enter_deposit(self, sum_of_deposit):
        self.element_is_visible(INPUT_DEPOSIT).send_keys(sum_of_deposit)
        self.element_is_visible(BUTTON_SUBMIT_DEPOSIT).click()
        self.refresh_page()

    def check_deposit(self):
        return self.element_is_present(DEPOSIT_SUCCESSFUL)

    def click_withdraw(self):
        self.element_is_visible(BUTTON_WITHDRAW).click()

    def enter_withdraw(self, sum_of_withdraw):
        self.element_is_visible(INPUT_WITHDRAW).send_keys(sum_of_withdraw)
        self.element_is_visible(BUTTON_SUBMIT_WITHDRAW).click()

    def check_balance(self):
        all_elements = self.elements_are_present(BALANCE_ALL)
        return all_elements[2].text

    def click_transaction(self):
        self.element_is_visible(BUTTON_TRANSACTION).click()

    def check_count_transaction(self):
        rows = self.elements_are_visible(ROWS_TABLE)
        return len(rows)


