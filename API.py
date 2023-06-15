import json
import os
from abc import ABC, abstractmethod
import requests

class AbstractVacancyAPI(ABC):
    @abstractmethod
    def get_vacancies(self, search_text):
        pass

class HHAPI(AbstractVacancyAPI):

    def __init__(self):
        self.url = f"https://api.hh.ru/vacancies"

    def search_area_hh(self, area):
        with open('areas.json', encoding='utf8') as f:
            areas_text = f.read()
            areas_ = json.loads(areas_text)
            for v in areas_:
                if area == v[3]:
                    area_hh = int(v[2])
                    return area_hh
            else:
                return 'Город не найден'

    def get_vacancies (self, search_text, area_hh):
        url = self.url
        params = {
            "User-Agent": "ParserVacancyRA (a.a.renkos@gmail.com)",
            'text': search_text,
            'only_with_salary': True,
            'area': area_hh,
            'per_page': 100
        }
        response_h_h = requests.get(url, params=params)
        return response_h_h.json()




    def write_data_hh(self,data_hh):
        with open('data_hh.json', 'w', encoding='utf-8') as f:
            json.dump(data_hh, f, ensure_ascii=False)


    def modify_data_hh(self):
        """Метод modify_data работает с пришедшими данными HeadHunter.json, конвертирует в единый формат данных,
        приводит к единому формализованному формату и создает файл HeadHunter_formalized.json"""

        with open('data_hh.json', encoding='utf8') as f:
            json_text = f.read()
            json_obj = json.loads(json_text)

            new_str = []
            for v in json_obj['items']:
                name = v['name']
                salary_from = v['salary']['from']
                salary_to = v['salary']['to']
                requirement = v['snippet']['requirement']
                responsibility = v['snippet']['responsibility']
                organization = v['employer']['name']
                experience = v['experience']['name']
                if isinstance(salary_to, int):
                    salary_to = salary_to
                else:
                    salary_to = 0

                if isinstance(salary_from, int):
                    salary_from = salary_from
                else:
                    salary_from = 0

                formalized_dict = {
                    'name_vacancies': name,
                    'organization': organization,
                    'salary_from': salary_from,
                    'salary_to': salary_to,
                    'experience': experience,
                    'requirement': requirement,
                    'responsibility': responsibility,
                    'api': 'HeadHunter'
                }

                new_str.append(formalized_dict)

            filename_dict = 'HeadHunter_formalized.json'

            with open(filename_dict, mode='w', encoding='utf8') as f:
                json.dump(new_str, f, ensure_ascii=False, indent=4, separators=(",", ":"))
            return new_str


    def summ_data_hh(self):
        with open('Sum_data.json', 'a', encoding='utf-8') as f:
            json.dump(modify_data_hh, f, ensure_ascii=False, indent=4, separators=(",", ":"))


class SuperJobAPI(AbstractVacancyAPI):
    def __init__(self):
        self.api_key ='v3.r.137598910.32afcd3d9ac651efbf0b0b18c82bfb7ae33ee357.87c90ee967f7c532fe9790505571dbb571862463'

    def get_vacancies(self,search_text,area):
        url = f"https://api.superjob.ru/2.0/vacancies/"
        params = {'town': area.title(),
                  'count': 100,
                  'keyword': search_text,
                  'no_agreement': 1
                  }
        headers = {"X-Api-App-Id": self.api_key}
        response = requests.get(url, params, headers=headers)
        return response.json()


    def write_data_sj(self,data_super_job):
        with open('data_sj.json', 'w', encoding='utf-8') as f:
            json.dump(data_super_job, f, ensure_ascii=False)


    def modify_data_sj(self):
        """Метод modify_data работает с пришедшими данными SuperJob.json, конвертирует в единый формат данных,
        приводит к единому формализованному формату и создает файл SuperJob_formalized.json"""


        with open('data_sj.json', encoding='utf8') as f:
            json_text = f.read()
            json_obj = json.loads(json_text)
            new_str = []
            for v in json_obj["objects"]:
                name = v['profession']
                salary_from = v['payment_from']
                salary_to = v['payment_to']
                requirement = v['vacancyRichText']
                responsibility = v['candidat']
                organization = v['firm_name']
                experience = v['experience']['title']

                formalized_dict = {
                    'name_vacancies': name,
                    'organization': organization,
                    'salary_from': salary_from,
                    'salary_to': salary_to,
                    'experience': experience,
                    'requirement': requirement,
                    'responsibility': responsibility,
                    'api': 'SuperJob'
                    }

                new_str.append(formalized_dict)
            filename_dict = 'SuperJob_formalized.json'
            with open(filename_dict, mode='w', encoding='utf8') as f:
                json.dump(new_str, f, ensure_ascii=False, indent=4, separators=(",", ":"))
            return new_str


    def summ_data_sj(self):
        with open('Sum_data.json', 'a', encoding='utf-8') as f:
            json.dump(modify_data_sj, f, ensure_ascii=False, indent=4, separators=(",", ":"))






search_text = input("Введите поисковый запрос: ")
area = (input('Введите город для поиска вакансий Город  ')).title()


# def search_area_hh(area):
#     with open('areas.json', encoding='utf8') as f:
#         areas_text = f.read()
#         areas_ = json.loads(areas_text)
#         for v in areas_:
#             if area == v[3]:
#                 area_hh = int(v[2])
#                 return area_hh
#         else:
#             return 'Город не найден'

api_sj = SuperJobAPI()
api_hh = HHAPI()


area_hh = api_hh.search_area_hh(area)

data_super_job = api_sj.get_vacancies(search_text, area)
data_hh = api_hh.get_vacancies(search_text, area_hh)


api_hh.write_data_hh(data_hh)
api_sj.write_data_sj(data_super_job)


modify_data_hh = api_hh.modify_data_hh()
modify_data_sj = api_sj.modify_data_sj()

api_hh.summ_data_hh()
api_sj.summ_data_sj()




