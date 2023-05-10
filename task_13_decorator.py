## Practice

# 1. Write a decorator that ensures a function is only called by users with a specific role. 
#    Each function should have an user_type with a string type in kwargs

# Оголошуємо декоратор is_admin, що отримує на вхід оригінальну функцію func
def is_admin(func):
    # В середині декоратора оголошуємо функцію-обгортку, що отримує ті ж параметри, що і оригінальна функція
    def wrapper(*args, **kwargs):
        # Перевіряємо чи містить kwargs ключ user_type зі значенням 'admin'
        if kwargs.get('user_type') != 'admin':
            # Якщо умова не виконується, викидаємо виключення ValueError
            raise ValueError('Permission denied')
        # Якщо умова виконується, викликаємо оригінальну функцію з вхідними параметрами
        return func(*args, **kwargs) 
    # Повертаємо функцію-обгортку, яка буде викликатися замість оригінальної функції
    return wrapper

'''
    Example

   
    @is_admin
    def show_customer_receipt(user_type: str):
        # some very dangerous operation

    show_customer_receipt(user_type='user')
    > ValueError: Permission denied

    show_customer_receipt(user_type='admin')
    > function pass as it should be
'''  

# 2. Write a decorator that wraps a function in a try-except block and print an error if error has happened
 
# Оголошуємо декоратор catch_errors, що отримує на вхід оригінальну функцію 
def catch_errors(func):
    # wrapper приймає будь-яку кількість позиційних та іменованих аргументів і передає їх у вхідну функцію
    def wrapper(*args, **kwargs):
        # вхідна функція виконується, якщо немає помилок
        try:
            return func(*args, **kwargs)
        # якщо виникає помилка, то вона ловиться, і виконується код в цьому блоку
        except Exception as e:
            # виводиться повідомлення про помилку, що сталась
            print(f'Found 1 error during execution of your function:{e}')
    # функція повертає нову функцію (wrapper), яка обгортає вхідну функцію і додає можливість ловити помилки
    return wrapper

'''
    Example
    
    @catch_errors
    def some_function_with_risky_operation(data):
        print(data['key'])


    some_function_with_risky_operation({'foo': 'bar'})
    > Found 1 error during execution of your function: KeyError no such key as foo

    some_function_with_risky_operation({'key': 'bar'})
    > bar
'''    


# 4. Optional: Create a function that caches the result of a function, 
#    so that if it is called with same argument multiple times, 
#    it returns the cached result first instead of re-executing the function. 

# Оголошуємо функцію-декоратор, яка буде приймати іншу функцію як аргумент та повертати нову функцію з кешуванням результатів
def memoize(func):
    # Створюємо словник для кешування результатів функції
    cache = {}
    
    # Оголошуємо нову функцію, яка буде обгорткою над оригінальною функцією
    def wrapper(*args):
        # Якщо ми вже кешували результат для цих аргументів - повертаємо його з кешу
        if args in cache:
            return cache[args]
        else:
             # Інакше, якщо ми ще не кешували результат - обчислюємо його та кешуємо
             result = func(*args)
             cache[args] = result
             return result
            
    # Повертаємо нову функцію
    return wrapper

@memoize               # використовуємо синтаксичний цукор для виклику декоратора
def my_function(x):
    # піднесення до степеня
    return x ** 2

print(my_function(5))  # обчислюється та повертається 25
print(my_function(5))  # повертається 25 з кешу, не обчислюється повторно   


