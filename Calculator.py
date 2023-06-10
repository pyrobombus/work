def calculator():
    while True:
        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Выйти")

        choice = int(input("Введите номер операции: "))

        if choice == 5:
            print("Программа завершена.")
            break

        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        result = 0

        if choice == 1:
            result = num1 + num2
        elif choice == 2:
            result = num1 - num2
        elif choice == 3:
            result = num1 * num2
        elif choice == 4:
            if num2 != 0:
                result = num1 / num2
            else:
                print("Ошибка: деление на ноль")
                continue
        else:
            print("Ошибка: неверный выбор операции")
            continue

        print("Результат:", result)
        print()

calculator()


