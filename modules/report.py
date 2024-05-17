import csv
from datetime import datetime


transactions = [
    {"datetime": datetime(2024, 5, 15, 10, 30, 15), "amount": 100.50, "type": "Credit"},
    {"datetime": datetime(2024, 5, 16, 14, 20, 35), "amount": 50.25, "type": "Debit"},
    {"datetime": datetime(2024, 5, 17, 8, 45, 55), "amount": 200.00, "type": "Credit"}
]


def write_transactions_to_csv(transactions, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Дата-времяТранзакции", "Сумма", "ТипТранзакции"])
        for transaction in transactions:
            # Форматируем дату и время транзакции в указанный формат
            formatted_datetime = transaction["datetime"].strftime("%d %B %Y %H:%M:%S")
            writer.writerow([formatted_datetime, transaction["amount"], transaction["type"]])


# Записываем данные о транзакциях в файл CSV
write_transactions_to_csv(transactions, "transactions.csv")
