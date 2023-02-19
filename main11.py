from typing import Union

import doctest


class Pillow:
    def __init__(self, width: Union[int, float],
                 length: Union[int, float]):  # Класс "Подушка" с 2 характеристиками - ширина и длина
        """
        Создание и подготовка к работе объекта "Подушка"
        :param width: ширина подушки
        :param length: длина подушки
        Примеры:
        pillow1 = Pillow(70,70)
        """
        self.length = None
        self.width = None
        self.lenght = None
        self.init_width(width)  # Атрибут ширины
        self.init_lenght(length)  # Атрибут длины

    def init_width(self, width: (int, float)):
        if not isinstance(width, (int, float)):
            raise TypeError('Значение должно быть числом')
        if width < 0:
            raise ValueError('Значение должно быть больше нуля')
        self.width = width

    def init_lenght(self, length: (int, float)):
        if not isinstance(length, (int, float)):
            raise TypeError('Значение должно быть числом')
        if length < 0:
            raise ValueError('Значение должно быть больше нуля')
        self.length = length

    def sqr_pillow(self):
        """
        функция по поиску площади подушки
        :return: площадь
        """
        print(f"{self.length * self.width} - площадь подушки")

    def perim_pillow(self):
        """
        функция по поиску периметра подушки
        :return: периметр
        """
        print(f'{2 * (self.length + self.width)} - периметр подушки')


class Microcontroller:
    def __init__(self, price: Union[int, float],
                 bit_depth: Union[int, float]):  # Класс "Микроконтроллер" c 2 характеристиками - цена и битность
        """
        Создание и подготовка к работе объекта "Микроконтроллер"
        :param price: цена
        :param bit_depth: битность
        """
        self.price = None
        self.bit_depth = None
        self.init_price(price)  # Атрибут стоимости
        self.init_bit_depth(bit_depth)  # Атрибут битности

    def init_price(self, pr: (int, float)):
        if not isinstance(pr, (int, float)):
            raise TypeError('Значение должно быть числом')
        if pr < 0:
            raise ValueError('Значение должно быть больше нуля')
        self.price = pr

    def init_bit_depth(self, bit: (int, float)):
        if not isinstance(bit, (int, float)):
            raise TypeError('Значение должно быть числом')
        if bit < 0:
            raise ValueError('Объем должен быть больше нуля')
        self.bit_depth = bit

    def bit_to_pr(self):
        """
        Функция по поиску битности микроконтроллера к его цене
        :return: отношение битности к стоимости
        """
        print(f"{self.bit_depth / self.price} - отношение битности к стоимости")

    def pr_to_bit(self):
        """
        Функция по поиску стоимости к битности
        :return: отношение стоимости к битности
        """
        print(f"{self.price / self.bit_depth} - отношение стоимости к битности")


class Song:
    def __init__(self, bitrate: Union[int, float], duration: Union[int, float]):
        # Класс "Песня" с 2 характеристиками - битрейт и длительность.
        """
        Создание и подготовка к работе объекта "Песня"
        :param bitrate: битрейт
        :param duration: число секунд
        """
        self.bitrate = None
        self.duration = None
        self.init_bitrate(bitrate)  # Атрибут колтчества информации за одну секунду
        self.init_duration(duration)  # Атрибут числа секунд

    def init_bitrate(self, bitr: (int, float)):
        if not isinstance(bitr, (int, float)):
            raise TypeError('Значение должно быть числом')
        if bitr < 0:
            raise ValueError('Значение должно быть больше нуля')
        self.bitrate = bitr

    def init_duration(self, dur: (int, float)):
        if not isinstance(dur, (int, float)):
            raise TypeError('Значение должно быть числом')
        if dur < 0:
            raise ValueError('Значение должно быть больше нуля')
        self.duration = dur

    def sam_freq(self):
        """
        Функция по поиску частоты дискретизации для 24 битных стерео записей
        :return: частота дискретизации
        """
        print(f"{self.bitrate / 24*2} - частота дискретизации")

    def weight(self):
        """
        Функция по поиску веса песни
        :return: вес всей песни
        """
        print(f"{self.bitrate * self.duration} - вес песни")

    if __name__ == "__main__":
        doctest.testmod()  # тестирование примеров, которые находятся в документации
    # TODO Написать 3 класса с документацией и аннотацией типов

    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass


pillow1 = Pillow(70, 70)
pillow1.perim_pillow()
pillow1.sqr_pillow()
microcontroller1 = Microcontroller(1751, 8)
microcontroller1.bit_to_pr()
microcontroller1.pr_to_bit()
song1 = Song(2822400, 195)
song1.sam_freq()
song1.weight()
