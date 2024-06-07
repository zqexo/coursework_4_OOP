from src.hh_api import HHAPI
from src.fileworker import JSONWorker
from src.vacancy import Vacancy
from src.utils import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, print_vacancies

def user_interaction():
    hh_api = HHAPI()
    json_worker = JSONWorker('vacancies.json')

    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат(например 30000 - 50000: ")  # Пример: 30000 - 50000

    hh_vacancies = hh_api.get_vacancies(search_query)
    vacancies_list = Vacancy.create_vacancies(hh_vacancies)

    for vacancy in vacancies_list:
        json_worker.add_vacancy(vacancy)

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    print_vacancies(top_vacancies)

if __name__ == "__main__":
    user_interaction()
