from abc import ABC, abstractmethod
import requests


class BaseAPI(ABC):
    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class HHApi(BaseAPI):

    def __init__(self):
        self.base_url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'per_page': 100}
        self.vacancies = []

    def get_vacancies(self, keyword):
        """Получаем данные в формате json"""
        self.params.update({'text': keyword})
        response = requests.get(self.base_url, params=self.params)
        return response.json()['items']


if __name__ == '__main__':
    api_requests = HHApi()
    api_requests.get_vacancies('крановщик')
