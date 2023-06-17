import time

from Class_saver import SaverJson
from Class_vacancy import Vacancy


def user_interaction():
    while True:

        user_command_1 = int(input(
            "1 - Вывести список вакансий, в определенном городе, по ключевому слову, отсортированный по зарплате.\n"
            "0 - Выход\n"
        ))
        if user_command_1 == 0:
            break
        elif user_command_1 == 1:
            search_text = input("Введите поисковый запрос для поиска вакансий: ").lower()
            area = (input('Введите город для поиска вакансий: ')).lower().title()

            # api_sj = SuperJobAPI(search_text, area)
            # api_hh = HhApi(search_text, area)
            # data_hh = api_hh.get_vacancies()
            # data_super_job = api_sj.get_vacancies()

            modifity_sj_vacancy = Vacancy.get_modifity_vacancy_sj()

            modifity_hh_vacancy = Vacancy.get_modifity_vacancy_hh()
            all_vacancy = Vacancy.summ_vacancy(modifity_sj_vacancy, modifity_hh_vacancy)

            sort_vacancy_salary = Vacancy.sort_by_salary(all_vacancy)
            print("Вакансии отсортированы")
            time.sleep(1)
            for vacancy in sort_vacancy_salary:
                print(vacancy)
            filename = f'{search_text}.json'
            add_vacancy = SaverJson(filename, sort_vacancy_salary)
            user_command_2 = int(input(
                f"1 - Записать список вакансий в файл {search_text}.json\n"
                "2 - Удалить списк вакансий\n"
                "3 - Вывести список вакансий по ключевым словам\n"
                "4 - Вывести вакансии с зарплатой выше введенной\n"
                "0 - Выход\n"
            ))
            if user_command_2 == 1:
                add_vacancy = SaverJson(filename, sort_vacancy_salary)
                add_vacancy.add_vacancy_in_file()
            elif user_command_2 == 2:
                add_vacancy = SaverJson(filename, sort_vacancy_salary)
                add_vacancy.delete_vacancy()
            elif user_command_2 == 3:
                keywords = str(input("Введите ключевые слова через пробел\n"))
                if len(keywords) == 0:
                    print("Некорректный ввод")
                else:
                    add_vacancy = SaverJson(filename, sort_vacancy_salary)
                    vacancy_keywords = add_vacancy.get_vacansy_keywords(keywords)
                    if len(vacancy_keywords) == 0:
                        print("По данным словам вакансии не найдены")
                    else:
                        for vacancy in vacancy_keywords:
                            print(vacancy)
                    user_command_3 = int(input(
                        f"1 - Записать список вакансий в файл {search_text}.json\n"
                        "2 - Удалить списк вакансий\n"
                        "0 - Выход\n"
                    ))
                    if user_command_3 == 1:
                        add_vacancy_keywords = SaverJson(filename, vacancy_keywords)
                        add_vacancy_keywords.add_vacancy_in_file()
                    elif user_command_3 == 2:
                        add_vacancy_keywords = SaverJson(filename, vacancy_keywords)
                        add_vacancy_keywords.delete_vacancy()
                    else:
                        break
            elif user_command_2 == 4:
                user_salary = int(input("Введите пороговое значение зарплаты\n"))
                user_sort_salary = add_vacancy.get_vacancy_salary_most_x(user_salary)
                for vacancy in user_sort_salary:
                    print(vacancy)
                user_command_4 = int(input(
                    f"1 - Записать список вакансий в файл {search_text}.json\n"
                    "2 - Удалить списк вакансий\n"
                    "0 - Выход\n"
                    ))
                if user_command_4 == 1:
                    add_vacancy_salary = SaverJson(filename, user_sort_salary)
                    add_vacancy_salary.add_vacancy_in_file()
                elif user_command_4 == 2:
                    add_vacancy_salary = SaverJson(filename, user_sort_salary)
                    add_vacancy_salary.delete_vacancy()
                else:
                    break
            else:
                break
        else:
            break
