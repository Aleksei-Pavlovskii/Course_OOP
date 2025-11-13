import os
import shutil
import tempfile
from typing import Generator

import pytest

from src.json import JSON
from src.vacancy import Vacancy


@pytest.fixture
def sample_vacancy() -> Vacancy:
    """Фикстура с тестовой вакансией"""
    return Vacancy(
        name="Python Developer",
        url="https://hh.ru/vacancy/123",
        salary=100000,
        experience="1-3 года",
        requirement="Знание Python, Django",
        city="Москва",
        id=123,
    )


@pytest.fixture
def vacancies() -> tuple[Vacancy, Vacancy, Vacancy]:
    """Фикстура с несколькими тестовыми вакансиями"""
    vacancy1 = Vacancy(
        name="Python Developer",
        url="https://hh.ru/vacancy/123",
        salary=100000,
        experience="1-3 года",
        requirement="Знание Python, Django",
        city="Москва",
        id=123,
    )

    vacancy2 = Vacancy(
        name="Data Scientist",
        url="https://hh.ru/vacancy/124",
        salary=150000,
        experience="3-6 лет",
        requirement="ML, Python, SQL",
        city="Санкт-Петербург",
        id=124,
    )

    vacancy3 = Vacancy(
        name="Junior Developer",
        url="https://hh.ru/vacancy/125",
        salary=0,
        experience="без опыта",
        requirement="Базовые знания Python",
        city="Новосибирск",
        id=125,
    )

    return vacancy1, vacancy2, vacancy3


@pytest.fixture
def vacancies_data() -> list[dict]:
    return [
        {
            "name": "Backend Developer",
            "alternate_url": "https://hh.ru/vacancy/200",
            "salary": {"from": 120000, "to": 180000, "currency": "RUR"},
            "experience": {"name": "3-6 лет"},
            "snippet": {"requirement": "Python, FastAPI, PostgreSQL"},
            "area": {"name": "Москва"},
            "id": 200,
        },
        {
            "name": "Frontend Developer",
            "alternate_url": "https://hh.ru/vacancy/201",
            "salary": None,
            "experience": {"name": "1-3 года"},
            "snippet": {"requirement": "JavaScript, React, TypeScript"},
            "area": {"name": "Санкт-Петербург"},
            "id": 201,
        },
    ]


@pytest.fixture
def temp_dir() -> Generator:
    """Фикстура для временной директории"""
    test_dir = tempfile.mkdtemp()
    yield test_dir
    # Очистка после теста
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)


@pytest.fixture
def json_handler(temp_dir) -> JSON:
    """Фикстура для создания экземпляра JSON"""
    test_file = os.path.join(temp_dir, "vacancies.json")
    return JSON(test_file)


@pytest.fixture
def sample_vacancies() -> list[Vacancy]:
    """Фикстура с тестовыми вакансиями"""
    vacancy1 = Vacancy(
        "Python developer",
        "https://hh.ru/vacancy/126968140",
        {"from": 120000, "to": 180000, "currency": "RUR"},
        "От 3 до 6 лет",
        "Знание <highlighttext>Python</highlighttext>. Понимание ООП. Знание CI/CD. "
        "Умение работать с чужим кодом. Понимание работы <highlighttext>Python</highlighttext> "
        "и умение использовать различные типы...",
        "Москва",
        126968140,
    )
    vacancy2 = Vacancy(
        "Backend-разработчик PHP, Python (работа из офиса в г. Самара)",
        "https://hh.ru/vacancy/127194150",
        None,
        "От 3 до 6 лет",
        "Понимание front-end части (JS, React/Vue) на уровне интеграции с API. Опыт "
        "с <highlighttext>Python</highlighttext> (Django / Flask) для аналитики или...",
        "Самара",
        127194150,
    )
    return [vacancy1, vacancy2]


@pytest.fixture
def duplicate_vacancy() -> Vacancy:
    """Фикстура с вакансией-дубликатом"""
    return Vacancy(
        "Backend Developer",
        "https://hh.ru/vacancy/200",
        {"from": 120000, "to": 180000, "currency": "RUR"},
        "3-6 лет",
        "Python, FastAPI, PostgreSQL",
        "Знание Python",
        200,
    )
