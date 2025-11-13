import json
import os
from abc import ABC, abstractmethod

from src.vacancy import Vacancy


class WorkingWithFiles(ABC):
    @abstractmethod
    def save_to_file(self, data: list[dict]):
        ...

    @abstractmethod
    def load_from_file(self):
        ...

    @abstractmethod
    def clear_file(self):
        ...


class JSON(WorkingWithFiles):
    """Класс для работы с файлами JSON"""

    def __init__(self, file_name: str = "data/vacancies.json") -> None:
        """Инициализация файла"""
        self.__file_name = file_name

    def save_to_file(self, vacancies_list: list[Vacancy]) -> None:
        """Сохранение данных в файл"""
        try:
            existing_data = self.load_from_file()  # Загрузка существующих данных
            existing_ids = {
                item.get("id") for item in existing_data if item.get("id")
            }  # Получение ID существующих вакансий
        except FileNotFoundError:  # Если файла нет, создаем пустой список
            existing_data = []
            existing_ids = set()  # Создаём пусто множество уникальных ID
        data = []
        for vacancy in vacancies_list:
            if vacancy.id in existing_ids:  # Если ID вакансии уже существует
                continue
            vacancy_dict = {
                "name": vacancy.name,
                "url": vacancy.url,
                "salary": vacancy.salary,
                "experience": vacancy.experience,
                "requirement": vacancy.requirement,
                "city": vacancy.city,
                "id": vacancy.id,
            }
            data.append(vacancy_dict)
        all_data = existing_data + data  # Объединение существующих данных и новых вакансий

        os.makedirs("data", exist_ok=True)  # Создаем папку если она не существует
        with open(self.__file_name, "w", encoding="utf-8") as file:
            json.dump(all_data, file, indent=4, ensure_ascii=False)

    def load_from_file(self) -> list[dict]:
        """Загрузка данных из файла"""
        with open(self.__file_name, "r", encoding="utf-8") as file:
            return json.load(file)

    def delete_from_file(self) -> None:
        """Удаление файла"""
        os.remove("data/vacancies.json")

    def clear_file(self) -> None:
        """Очищение файла"""
        os.makedirs("data", exist_ok=True)  # Создаем папку если она не существует
        with open(self.__file_name, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4, ensure_ascii=False)
