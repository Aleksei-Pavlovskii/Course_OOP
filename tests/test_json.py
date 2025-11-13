import json
import os

from src.json import JSON
from src.vacancy import Vacancy


def test_initialization() -> None:
    """Тест инициализации с файлом по умолчанию"""
    json_handler = JSON()
    assert json_handler._JSON__file_name == "data/vacancies.json"


def test_save_to_file_new_file(json_handler: JSON, sample_vacancies: list[Vacancy]) -> None:
    """Тест сохранения в новый файл"""
    # Сохраняем вакансии
    json_handler.save_to_file(sample_vacancies)

    # Проверяем, что файл создан
    assert os.path.exists(json_handler._JSON__file_name)

    # Проверяем содержимое файла
    with open(json_handler._JSON__file_name, "r", encoding="utf-8") as file:
        data = json.load(file)

    assert len(data) == 2
    assert data[0]["id"] == 126968140
    assert data[0]["name"] == "Python developer"
    assert data[1]["id"] == 127194150
    assert data[1]["name"] == "Backend-разработчик PHP, Python (работа из офиса в г. Самара)"


def test_save_to_file_duplicate_ids(json_handler: JSON, sample_vacancies: list[Vacancy],
                                    duplicate_vacancy: Vacancy) -> None:
    """Тест сохранения вакансий с дублирующимися ID"""
    # Сохраняем первую вакансию
    json_handler.save_to_file([sample_vacancies[0]])

    # Пытаемся сохранить вакансию с тем же ID
    json_handler.save_to_file([duplicate_vacancy])

    # Проверяем, что дубликат не добавлен
    with open(json_handler._JSON__file_name, "r", encoding="utf-8") as file:
        data = json.load(file)

    assert len(data) == 2
    assert data[0]["name"] == "Python developer"


def test_load_from_file_success(json_handler: JSON, sample_vacancies: list[Vacancy]) -> None:
    """Тест успешной загрузки данных из файла"""
    # Сначала сохраняем данные
    json_handler.save_to_file(sample_vacancies)

    # Загружаем данные
    loaded_data = json_handler.load_from_file()

    assert len(loaded_data) == 2
    assert loaded_data[0]["name"] == "Python developer"
    assert loaded_data[1]["name"] == "Backend-разработчик PHP, Python (работа из офиса в г. Самара)"
