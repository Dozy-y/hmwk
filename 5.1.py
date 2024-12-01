class Book:
    def init(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        return self.title, self.author, self.year
book1 = Book('Война и мир', 'Лев Толстой', 1869)
print(book1.get_info())
