class Vacancy:
    def __init__(self, salary_from, salary_to):
        self.salary_from = salary_from
        self.salary_to = salary_to

    def __repr__(self):
        return f'Я вакансия, моя зп от: {self.salary_from}'

    def __lt__(self, other):
        return self.salary_from < other.salary_from

first = Vacancy(25000, 50000)
second = Vacancy(30000, 60000)
third = Vacancy(15000, 40000)

vacancies = [first, second, third]
result = sorted(vacancies)
print(result)
