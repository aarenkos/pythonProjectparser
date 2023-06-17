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

    modifity_sj_vacancy = Vacancy.get_modifity_vacancy_sj()

    modifity_hh_vacancy = Vacancy.get_modifity_vacancy_hh()
    all_vacancy = Vacancy.summ_vacancy(modifity_sj_vacancy, modifity_hh_vacancy)


    sort_vacancy_salary = Vacancy.sort_by_salary(all_vacancy)
    print(sort_vacancy_salary)
    for vacancy in sort_vacancy_salary:
        print(type(vacancy.name))

    filename = f'{search_text}.json'


    add_vacancy = SaverJson(filename, sort_vacancy_salary)
    print(add_vacancy)
    add_vacancy.add_vacancy_in_file()


    #
    #
    #
    #
    #
    #
    #
    #
