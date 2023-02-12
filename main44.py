class rot:
    """Родительский класс алкоголь"""

    def __init__(self, strength: str, name: str, cost: str, volume: str):
        self.strength = strength
        self.name = name
        self.cost = cost
        self.volume = volume

    def __str__(self):
        return f"Крепость:{self.strength}. Название:{self.name}. Цена:{self.cost}. Объем:{self.volume}."

    def __repr__(self):
        return f"{self.__class__.__name__}(strength={self.strength!r}, name={self.name!r}, cost={self.cost!r}, volume={self.volume!r})"


class grain(rot):
    """Дочерний класс зерновой спирт"""

    def __init__(self, strength: str, name: str, cost: str, volume: str, flavor: str):
        super().__init__(strength, name, cost, volume)
        if isinstance(flavor, int):
            if flavor > 0:
                self.flavor = flavor
            else:
                raise AttributeError("error of flavor")
        else:
            raise AttributeError("error of flavor")

    def __str__(self):
        return f"Крепость - {self.strength}. Производитель - {self.name}. Цена - {self.cost}. Объем - {self.volume}. Какое зерно - {self.flavor}"

    def __repr__(self):
        return f"{self.__class__.__name__}(strength={self.strength!r}, name={self.name!r}, cost={self.cost!r}, volume={self.volume!r}, flavor={self.flavor!r})"


class fruits(rot):
    """Дочерный класс фруктовый спирт"""

    def __init__(self, strength: str, name: str, cost: str, volume: str, species: str):
        super().__init__(strength, name, cost, volume)
        if isinstance(species, int):
            if species > 0:
                self.species = species
            else:
                raise AttributeError("error of species")
        else:
            raise AttributeError("error of species")

    def __str__(self):
        return f"Крепость - {self.strength}. Производитель - {self.name}. Цена - {self.cost}. Объем - {self.volume}. Какой фрукт - {self.species}"

    def __repr__(self):
        return f"{self.__class__.__name__}(strength={self.strength!r}, name={self.name!r}, topic={self.cost!r}, volume={self.volume!r}, species={self.species})"


class grape(rot):
    """Дочерный класс фруктовый спирт"""

    def __init__(self, strength: str, name: str, cost: str, volume: str, veriety: str):
        super().__init__(strength, name, cost, volume)
        if isinstance(veriety, int):
            if veriety > 0:
                self.veriety = veriety
            else:
                raise AttributeError("error of veriety")
        else:
            raise AttributeError("error of veriety")

    def __str__(self):
        return f"Крепость - {self.strength}. Производитель - {self.name}. Цена - {self.cost}. Объем - {self.volume}. Сорт винограда - {self.veriety}"

    def __repr__(self):
        return f"{self.__class__.__name__}(strength={self.strength!r}, name={self.name!r}, topic={self.cost!r}, volume={self.volume!r}, veriety={self.veriety})"


rot1 = rot('8.1', 'heineken', '49.99', '0,45')
print(rot1)
rot2 = grain('40', 'Синергия', '1493', '0,5', 'Солод')
print(rot2)
rot3 = fruits('40', 'Slaur Inernational', '2867', '0,5', 'яблочный')
print(rot3)
rot3 = grape('14,9', 'Мысхако', '884', '0,75', 'Каберне Совиньон')
print(rot3)
