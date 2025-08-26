try:
    num1 = float(input("Введите первое число: "))

    num2 = float(input("Введите второе число: "))

    print(f"Первое число: {num1}")
    print(f"Второе число: {num2}")

    message = '''
Выберете математическую операцию:

+ : Сложение
- : Вычитание
/ : Деление
* : Умножение

Ваш выбор: '''

    operation = input(message)

    if operation == '+':
        result = num1 + num2
        print(f"Результат сложения: {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"Результат вычитания: {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"Результат умножения: {result}")
    elif operation == '/':
        if num2 == 0:
            raise ZeroDivisionError("Деление на ноль невозможно!")
        result = num1 / num2
        print(f"Результат деления: {result}")
    else:
        raise ValueError("Неизвестная операция!")

except ValueError as e:
    print(f"Ошибка ввода: {e}")

except ZeroDivisionError as e:
    print(f"Математическая ошибка: {e}")

except Exception as e:
    print(f"Неожиданная ошибка: {e}")

finally:
    print("Программа завершила работу. Спасибо за использование!")