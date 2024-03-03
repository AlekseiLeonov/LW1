import doctest
# Класс, описывающий материальные объекты
class MaterialObject:
    def __init__(self, name: str, weight: float):
        """
        Конструктор класса MaterialObject.

        :param name: название объекта
        :param weight: вес объекта
        Пример использования:
        >>> obj = MaterialObject("Стол", 10.5) # инициализация экземпляра класса
        """
        self.name = name
        self.weight = weight

    def move(self, destination: str) -> None:
        """
        Метод, описывающий перемещение объекта.

        :param destination: место, куда перемещается объект

        :return: None

        Пример использования:
        >>> obj.move("Комната 1")
        """

    def break_object(self) -> None:
        """
        Метод, описывающий разрушение объекта.

        :return: None

        Пример использования:
        >>> obj.break_object()
        """

    def paint(self, color: str) -> None:
        """
        Метод, описывающий покраску объекта.

        :param color: цвет, в который покрашен объект

        :return: None

        Пример использования:
        >>> obj.paint("Красный")
        """


# Класс, описывающий нематериальные объекты
class NonMaterialObject:
    def __init__(self, name: str, description: str):
        """
        Конструктор класса NonMaterialObject.

        :param name: название объекта
        :param description:  описание объекта

        Пример использования:
        >>> obj = NonMaterialObject("Стек", "Пустой") # инициализация экземпляра класса
        """
        self.name = name
        self.description = description

    def use_object(self, action: str) -> None:
        """
        Метод, описывающий использование объекта.

        :param action: действие, совершаемое с объектом

        :return: None

        Пример использования:
        >>> obj.use_object("Положить данные в стек")
        """

    def change_description(self, new_description: str) -> None:
        """
        Метод, описывающий изменение описания объекта.

        :param new_description: новое описание объекта

        :return: None

        Пример использования:
        >>> obj.change_description("Содержит данные")
        """


# Класс, описывающий объекты "Мебель"
class Furniture:
    def __init__(self, name: str, material: str, dimensions: tuple):
        """
        Конструктор класса Furniture.

        :param name: название мебели
        :param material: материал, из которого сделана мебель
        :param dimensions: размеры мебели (ширина, высота, длина)

        Пример использования:
        >>> obj = Furniture("Стол", "Дерево", (100, 80, 150))
        """
        self.name = name
        self.material = material
        self.dimensions = dimensions

    def use_furniture(self, action: str) -> None:
        """
        Метод, описывающий использование мебели.

        :param action: str - действие, совершаемое с мебелью

        :return: None

        Пример использования:
        >>> obj.use_furniture("Сидеть за столом")
        """

    def rearrange(self, new_location: str) -> None:
        """
        Метод, описывающий перестановку мебели.

        :param new_location: str - новое место, где будет находиться мебель

        :return: None

        Пример использования:
        >>> obj.rearrange("Кухня")
        """

if __name__ == "__main__":
    doctest.testmod()
