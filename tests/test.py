import unittest
from unittest.mock import patch
from main import user_interaction

class TestMain(unittest.TestCase):

    @patch('builtins.input', side_effect=['крановщик', '10', 'без опыта', '30000 - 50000'])
    def test_user_interaction_valid_input(self, mock_input):
        # Проверяем, что функция user_interaction корректно обрабатывает валидный ввод пользователя.
        with patch('src.main.print_vacancies') as mock_print:
            user_interaction()
            mock_print.assert_called()

    @patch('builtins.input', side_effect=['', '10', 'без опыта', '30000 - 50000'])
    def test_user_interaction_empty_input(self, mock_input):
        # Проверяем, что функция user_interaction корректно обрабатывает пустой ввод пользователя.
        with patch('src.main.print_vacancies') as mock_print:
            user_interaction()
            mock_print.assert_called()

    @patch('builtins.input', side_effect=['крановщик', 'abc', 'без опыта', '30000 - 50000'])
    def test_user_interaction_invalid_top_n(self, mock_input):
        # Проверяем, что функция user_interaction корректно обрабатывает некорректный ввод количества вакансий.
        with patch('src.main.print_vacancies') as mock_print:
            user_interaction()
            mock_print.assert_called()

    @patch('builtins.input', side_effect=['крановщик', '10', '', '30000 - 50000'])
    def test_user_interaction_empty_filter_words(self, mock_input):
        # Проверяем, что функция user_interaction корректно обрабатывает пустой ввод ключевых слов для фильтрации.
        with patch('src.main.print_vacancies') as mock_print:
            user_interaction()
            mock_print.assert_called()

    @patch('builtins.input', side_effect=['крановщик', '10', 'без опыта', ''])
    def test_user_interaction_empty_salary_range(self, mock_input):
        # Проверяем, что функция user_interaction корректно обрабатывает пустой ввод диапазона зарплат.
        with patch('src.main.print_vacancies') as mock_print:
            user_interaction()
            mock_print.assert_called()

    # Добавьте другие тесты для покрытия других сценариев использования.

if __name__ == '__main__':
    unittest.main()