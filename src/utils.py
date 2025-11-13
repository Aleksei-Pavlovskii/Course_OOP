from datetime import datetime

from src.vacancy import Vacancy


def get_user_time() -> str:
    """Получение времени пользователя"""
    user_data_hour = datetime.now().hour  # Получение текущего часа
    if 5 <= user_data_hour < 11:
        return "Доброе утро"
    elif 11 <= user_data_hour < 17:
        return "Добрый день"
    elif 17 <= user_data_hour < 23:
        return "Добрый вечер"
    else:
        return "Доброй ночи"


def filter_vacancies(vacancies_list: list[Vacancy], filter_words: list[str]) -> list[Vacancy]:
    """Фильтрация вакансий по ключевым словам"""
    vacancies_set = set()  # Множество для хранения ID вакансий
    vacancies = []
    for vacancy in vacancies_list:
        for word in filter_words:
            if word.lower() in vacancy.name.lower():
                vacancies_set.add(id(vacancy))  # Добавление ID вакансии в множество
    for vacancy in vacancies_list:
        if id(vacancy) in vacancies_set:  # Проверка наличия ID вакансии в множестве
            vacancies.append(vacancy)  # Добавление вакансии в список
    return vacancies


def get_vacancies_by_salary(vacancies_list: list[Vacancy], salary_range: str) -> list[Vacancy]:
    """Фильтрация вакансий по диапазону зарплаты"""
    vacancies = []
    salary_range = salary_range.replace(" ", "").split("-")
    for vacancy in vacancies_list:
        if int(salary_range[0]) <= vacancy.salary <= int(salary_range[1]):
            vacancies.append(vacancy)
    return vacancies


def sort_vacancies_city(vacancies_list: list[Vacancy], city: str) -> list[Vacancy]:
    """Фильтрация вакансий по городу"""
    return [vacancy for vacancy in vacancies_list if vacancy.city.lower() == city]


def sort_vacancies(vacancies_list: list[Vacancy]) -> list[Vacancy]:
    """Фильтрация вакансий по зарплате в порядке убывания"""
    return sorted(vacancies_list, key=lambda x: x.salary, reverse=True)


def get_top_vacancies(vacancies_list: list[Vacancy], top_n: int) -> list[Vacancy]:
    """Вывод топ вакансий"""
    return vacancies_list[:top_n]
