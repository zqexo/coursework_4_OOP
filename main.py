import json
import os


class Vacancy:
    def __init__(self, salary_from, salary_to):
        self.salary_from = salary_from
        self.salary_to = salary_to

    def __repr__(self):
        return f'Я вакансия, моя зп от: {self.salary_from}'

    def __lt__(self, other):
        return self.salary_from < other.salary_from

    def to_json(self):
        return {
            'salary_from': self.salary_from,
            'salary_to': self.salary_to,
        }


class JSONWorker():
    def __init__(self, file_name: str):
        # упрощённо -- надо иди с корневой директории
        self.path = os.path.join('data', file_name)

    def add_vacancy(self, vacancy: Vacancy):
        vac_info = vacancy.to_json()
        content = self.read_file()
        content.append(vac_info)
        self.write_file(content)
    def read_file(self):
        with open(self.path) as file:
            return json.load(file)

    def write_file(self, data):
        with open(self.path, 'a') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


first = Vacancy(25000, 50000)
second = Vacancy(30000, 60000)
third = Vacancy(15000, 40000)

vacancies = [first, second, third]
result = sorted(vacancies)
print(result)

json_worker = JSONWorker('vacancies.json')
json_worker.add_vacancy(third)
