"""
Модуль для работы с API HeadHunter.
"""

# Импорт необходимых модулей
from abc import ABC, abstractmethod
import requests


class BaseAPI(ABC):
    """
    Абстрактный класс для работы с API сервиса с вакансиями.
    """

    @abstractmethod
    def get_vacancies(self, keyword):
        """
        Абстрактный метод для получения вакансий по ключевому слову.
        """
        pass


class HHAPI(BaseAPI):
    """
    Класс для работы с API HeadHunter.
    """

    def __init__(self):
        """
        Инициализация объекта класса HHApi.
        """
        self.base_url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'per_page': 100}
        self.vacancies = []

    def get_vacancies(self, keyword):
        """
        Получение данных о вакансиях с сайта HeadHunter. + проверка статус-код ответа не 200.
        """
        self.params.update({'text': keyword})
        response = requests.get(self.base_url, params=self.params)
        if response.status_code == 200:
            return response.json()['items']
        else:
            raise Exception(f"Ошибка при получении данных: {response.status_code} - {response.text}")
