class Vacancy:
    def __init__(self, name, url, salary_from, salary_to, city, experience):
        self.name = name
        self.url = url
        self.salary_from = salary_from or 0
        self.salary_to = salary_to or 0
        self.city = city
        self.experience = experience

    def __repr__(self):
        return f'{self.name} ({self.salary_from}-{self.salary_to})'

    def __lt__(self, other):
        return self.salary_from < other.salary_from

    @classmethod
    def create_vacancies(cls, data):
        instances = []
        for vac_info in data:
            if vac_info.get('alternate_url'):
                instances.append(cls(
                    name=vac_info.get('name'),
                    url=vac_info.get('alternate_url'),
                    salary_from=vac_info.get('salary_from'),
                    salary_to=vac_info.get('salary_to'),
                    city=vac_info.get('area', {}).get('name'),
                    experience=vac_info.get('experience', {}).get('name')
                ))
        return instances
