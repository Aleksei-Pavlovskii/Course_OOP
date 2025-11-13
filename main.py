from src.head_hunter_api import HeadHunterAPI
from src.json import JSON
from src.utils import (filter_vacancies, get_top_vacancies, get_user_time, get_vacancies_by_salary, sort_vacancies,
                       sort_vacancies_city)
from src.vacancy import Vacancy


def user_interaction() -> None:
    """Функция для взаимодействия с пользователем"""

    print(get_user_time())

    hh_api = HeadHunterAPI()

    keyword = input("Введите ключевое слово для поиска вакансий: ")
    hh_vacancies = hh_api.get_vacancies(keyword)

    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    json_file = JSON()

    while True:
        user_city_answer = input("Отсортировать по городу да/нет ")

        if user_city_answer == "да":
            city = input("Введите город: ")
            sort_city = sort_vacancies_city(vacancies_list, city.lower())
            break
        elif user_city_answer == "нет":
            sort_city = vacancies_list
            break
        else:
            print("Неверный ввод")

    filter_words = input("Введите ключевые слова для фильтрации вакансий через пробел: ").split()
    salary_range = input('Введите диапазон зарплат через "-": ')  # Пример: 100000 - 150000

    filtered_vacancies = filter_vacancies(sort_city, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    vacancies_sort = sort_vacancies(ranged_vacancies)

    while True:
        user_top = input("Введите количество, сколько отобразить вакансий: ")
        if user_top.isdigit():
            top_vacancies = get_top_vacancies(vacancies_sort, int(user_top))
            break
        else:
            print("Нужно ввести число")

    while True:
        user_clear = input("Очистить файл перед отображением да/нет ")
        if user_clear.lower() == "да":
            json_file.clear_file()
            json_file.save_to_file(top_vacancies)
            break
        elif user_clear.lower() == "нет":
            json_file.save_to_file(top_vacancies)
            break
        else:
            print("Неверный ввод")

    for vacancy in top_vacancies:
        print(vacancy)


if __name__ == "__main__":
    user_interaction()
