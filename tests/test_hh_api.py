import unittest
from unittest.mock import patch, MagicMock
from src.hh_api import HHAPI


class TestHHAPI(unittest.TestCase):

    @patch('requests.get')
    def test_get_vacancies(self, mock_get):
        # Создаем экземпляр класса HHAPI
        hh_api = HHAPI()

        # Устанавливаем ожидаемый результат
        expected_result = [{'name': 'Software Engineer'}, {'name': 'Data Scientist'}]

        # Создаем макет ответа от API
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'items': expected_result}
        mock_get.return_value = mock_response

        # Вызываем метод get_vacancies
        result = hh_api.get_vacancies('python')

        # Проверяем, что результат соответствует ожидаемому
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
