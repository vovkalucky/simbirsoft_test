def fibonacci_for_today(current_day) -> int:
    n = current_day + 1
    fib_prev = 0
    fib_curr = 1
    for _ in range(2, n+1):
        fib_next = fib_prev + fib_curr
        fib_prev, fib_curr = fib_curr, fib_next
    return fib_curr

