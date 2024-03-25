def caching_fibonacci():        # Оголошення функції з кешуванням
    cache = {}                  # Порожній словник для зберігання обчислення
    
    def fibonacci(n):           # Функція для обчислення чисел
        if n <= 0:              # Повернення перших двох чисел послыдовносты "0" та "1"
            return 0
        elif n == 1:
            return 1
        elif n in cache:        # Повернення числа без обчислення якщо воно вже є у кеші
            return cache[n]
        else:                    
            result = fibonacci(n - 1) + fibonacci(n - 2)        # Обчислення числа 
            cache[n] = result                                   # Зберігання у кеш
            return cache[n]                                     # Повернення збереженого кешу 
    return fibonacci                                            # Повернення внутрішньої функції

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(8))  
print(fib(16))  