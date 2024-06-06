from abc import ABC, abstractmethod


class Abstract(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __parsing__(self):
        pass


class Parser(Abstract):
    def __init__(self):
        pass

    def __parsing__(self):
        pass

    def cast_to_object_list(self):
        """Преобразование набора данных из JSON в список объектов"""
        pass


class HeadHunterAPI(Parser):

    def __init__(self):
        super().__init__()

    def __parsing__(self):
        pass

    def get_vacancies(self):
        """Получаем данные в формате json"""
        pass
