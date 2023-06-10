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

       
