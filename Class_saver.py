import json
import os
from abc import ABC, abstractmethod

from Class_vacancy import Vacancy


class Saver(ABC):

    @abstractmethod
    def add_vacancy_in_file(self):
        pass

    @abstractmethod
    def get_vacancy_by_file(self):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass


class SaverJson(Saver):

    def __init__(self, filename, sort_vacancy):
        self.filename = filename
        self.sort_vacancy = sort_vacancy

    def add_vacancy_in_file(self):
        vacansy_json = []
        for vacancy in self.sort_vacancy:
            vacancy_dict = {
                'name_vacancies': vacancy.name,
                'organization': vacancy.organization,
                'salary_from': vacancy.salary_from,
                'salary_to': vacancy.salary_to,
                'experience': vacancy.experience,
                'requirement': vacancy.requirement,
                'responsibility': vacancy.responsibility,
                'api': vacancy.api,
                'url_vacancy': vacancy.url_vacancy
            }
            vacansy_json.append(vacancy_dict)
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(vacansy_json, file, ensure_ascii=False)
        return print("Вакансии записаны в файл")

    def get_vacancy_by_file(self):

        with open(self.filename, 'w', encoding='utf-8') as file:
            vacancys = json.load(file)
            vacancy_from_file = []
            for vacansy in vacancys:
                api = vacansy["api"],
                experience = vacansy["experience"],
                name = vacansy["name_vacancies"],
                organization = vacansy["organization"],
                requirement = vacansy["requirement"],
                responsibility = vacansy["responsibility"],
                salary_from = vacansy["salary_from"],
                salary_to = vacansy["salary_to"],
                url_vacancy = vacansy["url_vacancy"]

                vacancy_from_file.append(Vacancy(name, salary_from, salary_to, requirement,
                                                 responsibility, organization, experience, url_vacancy, api))

        return vacancy_from_file

    def get_vacancy_salary_most_x(self, user_salary):
        index = 0
        for vacansy in self.sort_vacancy:
            index += 1
            if vacansy.salary_to != 0:
                if vacansy.salary_to >= user_salary:
                    break
            else:
                if vacansy.salary_from != 0:
                    if vacansy.salary_to >= user_salary:
                        break

        user_sort_salary = self.sort_vacancy
        del user_sort_salary[index:-1]
        return user_sort_salary

    def delete_vacancy(self):
        if os.path.isfile(self.filename):
            os.remove(self.filename)
        else:
            return print("Файл отсутствует")

    def get_vacansy_keywords(self, keywords):
        user_keywords = keywords.split()
        vacancy_keywords = []
        for word in user_keywords:
            for vacansy in self.sort_vacancy:
                if word.lover() in str(vacansy.requirement):
                    vacancy_keywords.append(vacansy)
        return vacancy_keywords
