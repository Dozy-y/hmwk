def file(name, m):
    try:
        with open(name, 'r') as file:
            if m == '1':
                for l in file:
                    print(l)
            elif m == '2':
                print(file.read())
    except FileNotFoundError:
        print('Файл небыл найден')

name = input('Введите название файла: ')
m = input('Введите 1 чтобы файл читался построчно или 2 чтобы полностью: ')
file(name, m)
