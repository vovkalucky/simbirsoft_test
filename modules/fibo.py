def fibonacci_for_today() -> int:
    from datetime import datetime
    # Получаем текущую дату
    current_date = datetime.now()
    # Получаем день месяца и добавляем 1
    n = current_date.day + 1
    # Инициализируем первые два числа Фибоначчи
    fib_prev = 0
    fib_curr = 1
    # Вычисляем N-е число Фибоначчи
    for _ in range(2, n+1):
        fib_next = fib_prev + fib_curr
        fib_prev, fib_curr = fib_curr, fib_next
    return fib_curr
