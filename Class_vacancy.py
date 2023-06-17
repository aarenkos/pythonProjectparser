import json


class Vacancy:
    """Класс, для работы с вакансиями.\n
    Содержит 9 атрибутов вакансии, для прдеставления экземпляра класса.\n
    Поддерживает создание экземпляров класса из полученных ранее файлов с вакансиями.\n
    Валидизирует атрибуты класса.\n
    Сортирует экземпляры класса по зарплате.
    """
    def __init__(self, name: str, salary_from: int, salary_to: int, requirement: str, responsibility: str,
                 organization: str, experience: str, url_vacancy: str, api: str):
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.requirement = requirement
        self.responsibility = responsibility
        self.organization = organization
        self.experience = experience
        self.url_vacancy = url_vacancy
        self.api = api

    def __str__(self):
        """Метод возвращает удобочитаемое  представление экземпляров класса Vacancy."""

        return f""" 
        Название вакансии: {self.name}
        Название оргинизации: {self.organization},
        Зарплата от: {self.salary_from},
        Зарплата до: {self.salary_to},
        Требуемый опыт: {self.experience},
        Требования: {self.requirement},
        Обязанности: {self.responsibility},
        API : {self.api},
        Ссылка на вакансию: {self.url_vacancy}
        """

    @staticmethod
    def get_modifity_vacancy_hh():
        """Метод валидизирует артибуты класса,\n
         конвертирует зарплату в рубли,\n
         создает список с экземплярами вакансий HeadHanter"""

        modifity_hh_vacancy = []
        try:
            with open('data_hh.json', encoding='utf8') as file_hh:
                data_hh_vacancy = json.load(file_hh)
                file_hh.close()
        except FileNotFoundError:
            return []
        else:
            for vacancy_hh in data_hh_vacancy:
                if vacancy_hh['name'] is None:
                    name = 'Нет названия вакансии'
                else:
                    name = vacancy_hh['name']
                if vacancy_hh['salary']['from'] is None:
                    salary_from = 0
                else:
                    if vacancy_hh['salary']['currency'] == "USD":
                        salary_from = (vacancy_hh['salary']['from']) * 83
                    elif vacancy_hh['salary']['currency'] == "EUR":
                        salary_from = (vacancy_hh['salary']['from']) * 90
                    else:
                        salary_from = vacancy_hh['salary']['from']
                if vacancy_hh['salary']['to'] is None:
                    salary_to = 0
                else:
                    if vacancy_hh['salary']['currency'] == "USD":
                        salary_to = (vacancy_hh['salary']['to']) * 83
                    elif vacancy_hh['salary']['currency'] == "EUR":
                        salary_to = (vacancy_hh['salary']['to']) * 90
                    else:
                        salary_to = vacancy_hh['salary']['to']
                if vacancy_hh['snippet']['requirement'] is None:
                    requirement = 'Требования не указаны'
                else:
                    requirement = vacancy_hh['snippet']['requirement']
                if vacancy_hh['snippet']['responsibility'] is None:
                    responsibility = 'Обязанности не указаны'
                else:
                    responsibility = vacancy_hh['snippet']['responsibility']
                if vacancy_hh['employer']['name'] is None:
                    organization = 'Название организации не указано'
                else:
                    organization = vacancy_hh['employer']['name']
                if vacancy_hh['experience']['name'] is None:
                    experience = 'Требуемый опыт не указан'
                else:
                    experience = vacancy_hh['experience']['name']
                if vacancy_hh['alternate_url'] is None:
                    url_vacancy = 'Адрес вакансии не указан'
                else:
                    url_vacancy = vacancy_hh['alternate_url']
                api = 'HeadHunter'

                modifity_hh_vacancy.append(Vacancy(name, salary_from, salary_to, requirement,
                                                   responsibility, organization, experience, url_vacancy, api))

            return modifity_hh_vacancy

    @staticmethod
    def get_modifity_vacancy_sj():
        """Метод валидизирует артибуты класса, конвертирует зарплату в рубли, создает список с
        экземплярами вакансий SuperJob"""

        modifity_sj_vacancy = []
        try:
            with open('data_sj.json', encoding='utf8') as file_sj:
                data_sj_vacancy = json.load(file_sj)
                file_sj.close()
        except FileNotFoundError:
            return []
        else:
            for vacancy_sj in data_sj_vacancy:
                if vacancy_sj['profession'] is None:
                    name = 'Нет названия вакансии'
                else:
                    name = vacancy_sj['profession']
                if vacancy_sj['payment_from'] is None:
                    salary_from = 0
                else:
                    salary_from = vacancy_sj['payment_from']
                if vacancy_sj['payment_to'] is None:
                    salary_to = 0
                else:
                    salary_to = vacancy_sj['payment_to']
                if vacancy_sj['vacancyRichText'] is None:
                    requirement = 'Требования не указаны'
                else:
                    requirement = None
                if vacancy_sj['candidat'] is None:
                    responsibility = 'Обязанности не указаны'
                else:
                    responsibility = vacancy_sj['candidat']
                if vacancy_sj['firm_name'] is None:
                    organization = 'Название организации не указано'
                else:
                    organization = vacancy_sj['firm_name']
                if vacancy_sj['experience']['title'] is None:
                    experience = 'Требуемый опыт не указан'
                else:
                    experience = vacancy_sj['experience']['title']
                if vacancy_sj['link'] is None:
                    url_vacancy = 'Адрес вакансии не указан'
                else:
                    url_vacancy = vacancy_sj['link']
                api = 'SuperJob'

                modifity_sj_vacancy.append(Vacancy(name, salary_from, salary_to, requirement,
                                                   responsibility, organization, experience, url_vacancy, api))

            return modifity_sj_vacancy

    @staticmethod
    def summ_vacancy(modifity_sj_vacancy: list, modifity_hh_vacancy: list):
        """Метод суммирует списки вакансий HeadHunter и SuperJob. Возвращает общий список вакансий"""
        all_vacancy = modifity_sj_vacancy + modifity_hh_vacancy

        return all_vacancy

    @staticmethod
    def sort_by_salary(all_vacancy):
        """Метод сортирует общий список вакансий по зарплате в порядке убывания"""

        sort_vacancy_salary = sorted(all_vacancy, key=lambda x: x.salary_to if x.salary_to else x.salary_from,
                                     reverse=True)

        return sort_vacancy_salary
