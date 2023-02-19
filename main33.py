class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook:
    """ Дочерний класс бумажные книги. """

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.author = None
        self.name = None
        self.pages = None
        if isinstance(pages, int):
            if pages > 0:
                self.pages = pages
            else:
                raise AttributeError("error count of pages")
        else:
            raise AttributeError("error type of pages")

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.name = None
        self.author = None
        self.duration = None
        if isinstance(duration, float):
            if duration > 0:
                self.duration = duration
            else:
                raise AttributeError("error time of duration")
        else:
            raise AttributeError("error type")

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


Book1 = Book('The Inhabited Island', 'Arkady and Boris Strugasky')
print(Book1)
Book2 = PaperBook('American Dirt', 'Jeanine Cummins', 510)
print(Book2)
Book3 = AudioBook('Bajazet', 'Valentin Pikul', 15963)
print(Book3)
