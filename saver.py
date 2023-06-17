import json
from abc import ABC, abstractmethod


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

    def __init__(self, filename, sort_by_salary):
        self.sort_by_salary = sort_by_salary
        self.filename = filename


    def add_vacancy_in_file(self):

        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.sort_by_salary, file, ensure_ascii=False)
            self.filename.close()



    def get_vacancy_by_file(self):
        pass


    def delete_vacancy(self):
        pass







