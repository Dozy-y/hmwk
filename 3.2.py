t = input('Введите текст: ')
with open('user_input.txt', 'a+') as file:
    file.write(t)
    file.write(' ')
print('Текст pаписан')
