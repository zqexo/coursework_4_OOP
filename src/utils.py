"""
Функции для взаимодействия с пользователем через консоль.
"""


def filter_vacancies(vacancies, keywords):
    """
    Фильтрация вакансий по ключевым словам.
    """
    return [vac for vac in vacancies if any(word in vac.name for word in keywords)]


def get_vacancies_by_salary(vacancies, salary_range):
    """
    Получение списка вакансий в заданном диапазоне зарплат.
    """
    salary_min, salary_max = map(int, salary_range.split('-'))
    return [vac for vac in vacancies if vac.salary_from >= salary_min and vac.salary_to <= salary_max]


def sort_vacancies(vacancies):
    """
    Сортировка списка вакансий по зарплате.
    """
    return sorted(vacancies, key=lambda x: x.salary_from, reverse=True)


def get_top_vacancies(vacancies, top_n):
    """
    Получение топ N вакансий по зарплате.
    """
    return vacancies[:top_n]


def print_vacancies(vacancies):
    """
    Вывод списка вакансий.
    """
    for vac in vacancies:
        print(vac)
