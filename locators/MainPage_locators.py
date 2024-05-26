from selenium.webdriver.common.by import By


class Locators:
    CUSTOMER_LOGIN = (By.CSS_SELECTOR, "[ng-click='customer()']")
    SELECT_LOGIN = (By.CSS_SELECTOR, "#userSelect")
    BUTTON_SUBMIT_LOGIN = (By.CSS_SELECTOR, "[type='submit']")
    LOGIN = (By.CSS_SELECTOR, ".fontBig.ng-binding")
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
