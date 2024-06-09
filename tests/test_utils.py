import unittest
from src.utils import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies
from src.vacancy import Vacancy


class TestUtils(unittest.TestCase):

    def setUp(self):
        self.vacancies = [
            Vacancy("Software Engineer", "url1", 50000, 70000, "Moscow", "3-6 years"),
            Vacancy("Data Scientist", "url2", 60000, 80000, "Saint Petersburg", "1-3 years"),
            Vacancy("Backend Developer", "url3", 40000, 60000, "Novosibirsk", "3-6 years"),
            Vacancy("Frontend Developer", "url4", 45000, 65000, "Moscow", "1-3 years")
        ]

    def test_filter_vacancies(self):
        keywords = ["Engineer", "Data"]
        filtered = filter_vacancies(self.vacancies, keywords)
        self.assertEqual(len(filtered), 2)
        self.assertEqual(filtered[0].name, "Software Engineer")
        self.assertEqual(filtered[1].name, "Data Scientist")


    def test_sort_vacancies(self):
        sorted_vacancies = sort_vacancies(self.vacancies)
        self.assertEqual(len(sorted_vacancies), 4)
        self.assertEqual(sorted_vacancies[0].name, "Data Scientist")
        self.assertEqual(sorted_vacancies[1].name, "Software Engineer")
        self.assertEqual(sorted_vacancies[2].name, "Frontend Developer")
        self.assertEqual(sorted_vacancies[3].name, "Backend Developer")

    def test_get_top_vacancies(self):
        top_n = 2
        top_vacancies = get_top_vacancies(self.vacancies, top_n)
        self.assertEqual(len(top_vacancies), top_n)
        self.assertEqual(top_vacancies[0].name, "Software Engineer")
        self.assertEqual(top_vacancies[1].name, "Data Scientist")


if __name__ == "__main__":
    unittest.main()
