from typing import Optional


class Vacancy:
    """Класс для работы с вакансиями"""

    __slots__ = ("name", "url", "salary", "experience", "requirement", "city", "id")

    def __init__(
        self, name: str, url: str, salary: int, experience: str, requirement: str, city: str, id: int
    ) -> None:

        self.name = name
        self.url = url
        self.salary = self.__validate_salary(salary)
        self.experience = experience
        self.requirement = requirement
        self.city = city
        self.id = id

    def __validate_salary(self, salary: Optional[int]) -> int:
        """Валидация зарплаты"""
        if isinstance(salary, int) and salary > 0:
            return salary
        return 0

    def __str__(self) -> str:
        """Возвращает строковое представление объекта"""
        return (
            f"Название вакансии: {self.name}\nURL вакансии: {self.url}\nЗарплата: {self.salary}\nОпыт работы:"
            f" {self.experience}\nТребования: {self.requirement}\nГород: {self.city}\nID вакансии: {self.id}\n"
        )

    def __lt__(self, other) -> bool:
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary < other.salary

    def __eq__(self, other) -> bool:
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary == other.salary

    @classmethod
    def cast_to_object_list(cls, hh_vacancies: list[dict]) -> list["Vacancy"]:
        """Преобразование набора данных из JSON в список объектов"""
        list_vacancies = []
        for vacancy in hh_vacancies:
            name = vacancy.get("name")  # Название вакансии
            url = vacancy.get("alternate_url")  # url вакансии
            if not vacancy.get("salary") or not vacancy.get("salary").get("from"):  # Если salary отсутствует
                salary = 0  # Зарплата = 0
            else:
                salary = vacancy.get("salary").get("from")  # Зарплата
            experience = vacancy.get("experience").get("name")  # Опыт работы
            requirement = vacancy.get("snippet").get("requirement")  # Требования
            city = vacancy.get("area").get("name")  # Город
            id = vacancy.get("id")  # ID вакансии
            list_vacancies.append(Vacancy(name, url, salary, experience, requirement, city, id))

        return list_vacancies  # Возвращаем список вакансий
