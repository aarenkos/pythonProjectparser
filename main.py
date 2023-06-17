import json

from API import HhApi, SuperJobAPI
from saver import SaverJson
from vacancy import Vacancy

# from vacancy import Vacancy

if __name__ == '__main__':
    search_text = input("Введите поисковый запрос: ").lower()
    # area = (input('Введите город для поиска вакансий: ')).lower().title()
    #
    # api_sj = SuperJobAPI(search_text, area)
    # api_hh = HhApi(search_text, area)
    #
    # data_hh = api_hh.get_vacancies()
    #
    # data_super_job = api_sj.get_vacancies()
    filename = f'{search_text}.json'
    sort_by_salary = Vacancy.sort_y_salary
    print(sort_by_salary)
    add_vacancy = SaverJson(filename, sort_by_salary)
    add_vacancy.add_vacancy_in_file()









