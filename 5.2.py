class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    def set_radius(self, new_radius):
        self.radius = new_radius
r=input('Введите первый радиус: ')
Circle1=Circle(r)
Circle1.get_radius()
if input('Если хотоие изменить радиус введите 1, а 0 если нет: ') == '1':
    r1=input('Введите новый радиус: ')
    Circle1=Circle(r1)
    Circle1.get_radius()
    Circle1.set_radius(r1)
print('Ваш радиус: ', Circle1.get_radius())
