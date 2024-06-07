import unittest
from unittest.mock import patch
from main import user_interaction

class TestMain(unittest.TestCase):

    @patch('builtins.input', side_effect=['���������', '10', '��� �����', '30000 - 50000'])
    def test_user_interaction_valid_input(self, mock_input):
        # ���������, ��� ������� user_interaction ��������� ������������ �������� ���� ������������.
        with patch('src.main.print_vacancies') as mock_print:
            user_interaction()
            mock_print.assert_called()

    @patch('builtins.input', side_effect=['', '10', '��� �����', '30000 - 50000'])
    def test_user_interaction_empty_input(self, mock_input):
        # ���������, ��� ������� user_interaction ��������� ������������ ������ ���� ������������.
        with patch('src.main.print_vacancies') as mock_print:
            user_interaction()
            mock_print.assert_called()

    @patch('builtins.input', side_effect=['���������', 'abc', '��� �����', '30000 - 50000'])
    def test_user_interaction_invalid_top_n(self, mock_input):
        # ���������, ��� ������� user_interaction ��������� ������������ ������������ ���� ���������� ��������.
        with patch('src.main.print_vacancies') as mock_print:
            user_interaction()
            mock_print.assert_called()

    @patch('builtins.input', side_effect=['���������', '10', '', '30000 - 50000'])
    def test_user_interaction_empty_filter_words(self, mock_input):
        # ���������, ��� ������� user_interaction ��������� ������������ ������ ���� �������� ���� ��� ����������.
        with patch('src.main.print_vacancies') as mock_print:
            user_interaction()
            mock_print.assert_called()

    @patch('builtins.input', side_effect=['���������', '10', '��� �����', ''])
    def test_user_interaction_empty_salary_range(self, mock_input):
        # ���������, ��� ������� user_interaction ��������� ������������ ������ ���� ��������� �������.
        with patch('src.main.print_vacancies') as mock_print:
            user_interaction()
            mock_print.assert_called()

    # �������� ������ ����� ��� �������� ������ ��������� �������������.

if __name__ == '__main__':
    unittest.main()