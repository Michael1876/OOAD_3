try:
    a = float(input("Число 1: "))
    b = float(input("Число 2: "))
    op = input("Операция (+, -, *, /): ").strip()

    ops = {
        '+': a + b, 
        '-': a - b, 
        '*': a * b, 
        '/': a / b if b != 0 else "Ошибка: /0"
    }

    print(f"Результат: {ops.get(op, 'Неверный оператор')}")

except ValueError:
    print("Ошибка: введите числа")
