from abc import ABC, abstractmethod
import requests

class AbstractVacancyAPI(ABC):
    @abstractmethod
    def get_vacancies(self, search_text):
        pass

class HHAPI(AbstractVacancyAPI):

    def __init__(self, search_text=None):
        self.url = f"https://api.hh.ru/vacancies"

    def get_vacancies(self, search_text):
        url = self.url
        params = {"User-Agent": "ParserVacancyRA (a.a.renkos@gmail.com)", "text": search_text.lower()}
        responseHH = requests.get(url, params=params)
        return responseHH.json()





search_text = input("Введите поисковый запрос: ")

api = HHAPI()

vacancies = api.get_vacancies(search_text)




# class SuperJobVacancyAPI(AbstractVacancyAPI):
#     def __init__(self, api_key):
#         self.api_key = api_key
#
#     def get_vacancies(self, search_text):
#         url = f"https://api.superjob.ru/2.0/vacancies/?keyword={search_text}&count=100"
#         headers = {"X-Api-App-Id": self.api_key}
#         response = requests.get(url, headers=headers)
#         return response.json()
