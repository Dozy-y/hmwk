v = int(input("Напишите 1 если хотите чтение построчно и 2 если целиком: "))
if v == 1:
    with open('example.txt', 'r') as file:
        for a in file:
            print(a)
elif v == 2:
    with open('example.txt', 'r') as file:
        b = file.read()
        print(b)
else:
    print("Неправильный выбор. Выберите между 1 и 2.")
