import json
from abc import ABC, abstractmethod
import requests


class SiteVacancyAPI(ABC):
    """Абстрактный класс для работы с API сайтов с вакансиями"""

    @abstractmethod
    def get_vacancies(self):
        pass


class HhApi(SiteVacancyAPI):
    """Класс, для работы с HeadHanter. Получение вакансий по API"""

    def __init__(self, search_text: str, area: str):
        self.url = "https://api.hh.ru/vacancies"
        self.search_text = search_text
        self.area = area
        self.area_hh = None

    def search_area_hh(self):
        """Метод, определяющий значение, соответствующее введенному городу. Значение необходимо для отправки
         запроса к API. Берет данные городов из файла areas.json."""
        with open('areas.json', encoding='utf8') as f:
            areas_text = f.read()
            areas_ = json.loads(areas_text)
            for v in areas_:
                if self.area == v[3]:
                    self.area_hh = int(v[2])
                    return self.area_hh
            else:
                return 'Город не найден'

    def get_vacancies(self):
        """Метод, отправляющий запрос к API HeadHunter.\n
        Отправляет, запрос, получает список вакансий, записывает в файл data_hh.json\n
        для отправки использует введенный пользователем поисковый запрос и город.
        """
        url = self.url
        data_hh = []
        for i in range(10):

            headers = {"User-Agent": "ParserVacancyAR (a.a.renkos@gmail.com)"}
            params = {
                'text': self.search_text,
                'only_with_salary': True,
                'area': self.search_area_hh(),
                'page': i,
                'per_page': 100
            }

            response = requests.get(url, headers=headers, params=params)
            response_hh = response.json()
            if list(response_hh.keys())[0] == 'errors':
                break

            else:
                data_hh += response_hh['items']
        with open('data_hh.json', 'w', encoding='utf-8') as file_vacancy_hh:
            json.dump(data_hh, file_vacancy_hh, ensure_ascii=False)
            file_vacancy_hh.close()
        print('Вакансии HeadHunter загружены')


class SuperJobAPI(SiteVacancyAPI):
    """Метод, отправляющий запрос к API SuperJob.\n
    Отправляет, запрос, получает список вакансий, записывает в файл data_hh.json\n
    для отправки использует введенный пользователем поисковый запрос и город.
    """
    def __init__(self, search_text: str, area: str):
        self.api_key = 'v3.r.137598910.32afcd3d9ac651efbf0b0b18c82bfb7ae33ee357.87c9' \
                       '0ee967f7c532fe9790505571dbb571862463'
        self.search_text = search_text
        self.area = area

    def get_vacancies(self):
        data_sj = []
        for i in range(10):

            url = "https://api.superjob.ru/2.0/vacancies/"
            params = {'town': self.area,
                      'keyword': self.search_text,
                      'no_agreement': 1,
                      'page': i
                      }
            headers = {"X-Api-App-Id": self.api_key}

            response = requests.get(url, params, headers=headers)
            response_sj = response.json()
            if list(response_sj.keys())[0] == 'errors':
                break

            else:
                data_sj += response_sj['objects']
        with open('data_sj.json', 'w', encoding='utf-8') as file_vacancy_sj:
            json.dump(data_sj, file_vacancy_sj, ensure_ascii=False)
            file_vacancy_sj.close()
        print('Вакансии SuperJob загружены')
