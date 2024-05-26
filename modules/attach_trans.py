import os
import allure

def attach_trans():
    file_path = "/home/vladimir/PycharmProjects/simbirsoft_test/transactions.csv"
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            allure.attach(content, name='trans.csv', attachment_type=allure.attachment_type.CSV)
    else:
        print("Приложение к тестам отсутствует")