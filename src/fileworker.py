"""
Модуль для работы с файлами, сохранение и загрузка данных о вакансиях.
"""

from abc import ABC, abstractmethod
import json
import os
from src.vacancy import Vacancy


class FileWorker(ABC):
    """
    Абстрактный Класс для работы с JSON файлами.
    """

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, criteria):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass


class JSONWorker(FileWorker):
    """
    Класс для работы с JSON-файлами.
    """

    def __init__(self, file_name: str):
        """
        Инициализация объекта класса JSONWorker.
        """
        self.path = os.path.join('data', file_name)

    def add_vacancy(self, vacancy: Vacancy):
        """
        Добавление вакансии
        """
        vac_info = vacancy.__dict__
        content = self.read_file()
        content.append(vac_info)
        self.write_file(content)

    def get_vacancies(self, criteria):
        """
        Получение вакансии
        """
        content = self.read_file()
        return [vac for vac in content if criteria in vac['name']]

    def delete_vacancy(self, vacancy: Vacancy):
        """
        Удаление вакансии
        """
        content = self.read_file()
        content = [vac for vac in content if vac['name'] != vacancy.name]
        self.write_file(content)

    def read_file(self):
        """
        Чтение файла
        """
        if not os.path.exists(self.path):
            return []
        with open(self.path) as file:
            return json.load(file)

    def write_file(self, data):
        """
        Запись файла
        """
        with open(self.path, 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
