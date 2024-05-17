# Тестовое задание

Запуск Selenium GRID в Docker для прогона тестов:
docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-chrome:latest

Не успел оформить парсинг данных в .csv файл и прикрепление его к allure отчету.
Использовал функцию write_transactions_to_csv,  создающую csv с нужными данными . 
Прикрепляю transactions.csv к последнему тесту.
