class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    def set_password(self, new_password):
        self.password = new_password
        print("Пароль изменён")
    def check_password(self, password):
        if password == self.password:
            return True
        else:
            return False
user = UserAccount("user1", "user1.com", "password")
if input('Введите 1 если хотите изменить пароль и 0 если нет: ')=='1':
    user.set_password(input('Введите новый пароль: '))
print(user.check_password(input('Введите пароль: ')))
