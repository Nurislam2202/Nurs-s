# Есть 4 принципов ООП (наследование, полиморфизм, инкапсуляция, абстракция)
# суперкласс\родительский класс

class Books:

    prise = 350

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'{self.title} \nавтор:{self.author}\n'

    def prise_book(self):
        ...
book1 = Books("Преступление и наказание",'Достоевский')
# print(book1)
#
# book2=Books("Джамиля","Чингиз Айтматов")
# print(book2)

# дочерний класс
class Manga(Books):

    prise = 600

    def __init__(self, title, author, image='default.jpg'):
        Books.__init__(self, title, author)
        super().__init__(title, author)
        self.image = image

    def reverse(self):
        print('читай с права на лево')

    def __str__(self):
        return f'{super().__str__()}\n{self.image}\nцена:{self.prise}'

manga = Manga('Берсерк','Миура')
# manga.author = 'Кентаро'
print(manga)
manga.reverse()
# DRY

class Anime(Manga):
    def __init__(self, title, author, drive_image):
        Books.__init__(self, title, author)
        self.drive_image = drive_image

    def prise_book(self):
        print('120 за серию')

    def __len__(self):
        return self.prise

    def __str__(self):
        return f'название: {self.title}\nавтор: {self.author}\nкадры: {self.drive_image}'

anime = Anime('Naruto','Kisimoto','24')
print(anime.title, anime.author, anime.drive_image)
anime.prise_book()
print(Anime.mro())
print(len(anime))
print(anime)
