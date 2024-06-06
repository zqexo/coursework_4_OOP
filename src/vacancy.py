class Vacancy:
    def __init__(self, name, url, salary_from, salary_to, city, experience):
        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.city = city
        self.experience = expirience
        self.snippets = None
        self.validate()

    def validate(self):
        if self.salary_from == None:
            self.salary_from = 0

    @classmethod
    def create_vacancies(cls, data):
        instances = []
        for vac_info in data:
            if vac_info.get('alternate_url'):
                url = vac_info.get('altenate_url')
                ...

                instances = cls(name, url, salary_from, salary_to)

