import json
from abc import ABC, abstractmethod
import requests

class AbstractVacancyAPI(ABC):
    @abstractmethod
    def get_vacancies(self, search_text):
        pass

class HHAPI(AbstractVacancyAPI):

    def __init__(self):
        self.url = f"https://api.hh.ru/vacancies"

    def get_vacancies (self, search_text, area):
        url = self.url
        params = {
            "User-Agent": "ParserVacancyRA (a.a.renkos@gmail.com)",
            'text': search_text,
            'only_with_salary': True,
            'area': area,
            'per_page': 100
        }
        response_h_h = requests.get(url, params=params)

        return response_h_h.json()


class SuperJobAPI(AbstractVacancyAPI):
    def __init__(self):
        self.api_key ='v3.r.137598910.32afcd3d9ac651efbf0b0b18c82bfb7ae33ee357.87c90ee967f7c532fe9790505571dbb571862463'

    def get_vacancies(self, search_text, town):
        url = f"https://api.superjob.ru/2.0/vacancies/?keyword={search_text}&count=100"
        params = {'town': town,
                  'count': 100,
                  'keyword': search_text
                  }
        headers = {"X-Api-App-Id": self.api_key}
        response = requests.get(url, params, headers=headers)
        return response.json()


#
# search_text = input("Введите поисковый запрос: ")
#
# api = SuperJobAPI()
# data = api.get_vacancies(search_text)
# print(data)

# with open('areas.json', 'w', encoding='utf-8') as outfile:
#     json.dump(data, outfile, ensure_ascii=False)


