import pytest


from src.vacancy import Vacancy


def test_initialization(sample_vacancy: Vacancy) -> None:
    """Тест инициализации объекта"""
    assert sample_vacancy.name == "Python Developer"
    assert sample_vacancy.url == "https://hh.ru/vacancy/123"
    assert sample_vacancy.salary == 100000
    assert sample_vacancy.experience == "1-3 года"
    assert sample_vacancy.requirement == "Знание Python, Django"
    assert sample_vacancy.city == "Москва"
    assert sample_vacancy.id == 123


@pytest.mark.parametrize(
    "salary_input,expected",
    [
        (50000, 50000),  # Нормальная зарплата
        (1, 1),  # Минимальная зарплата
        (0, 0),  # Нулевая зарплата
        (-1000, 0),  # Отрицательная зарплата
        (None, 0),  # None зарплата
        ("invalid", 0),  # Неверный тип
    ],
)
def test_validate_salary(salary_input: int | None, expected: int) -> None:
    """Параметризованный тест валидации зарплаты"""
    vacancy = Vacancy("Test", "url", salary_input, "exp", "req", "city", 1)
    assert vacancy.salary == expected


def test_str_method(sample_vacancy: Vacancy) -> None:
    """Тест строкового представления вакансии"""
    result = str(sample_vacancy)

    assert "Python Developer" in result
    assert "https://hh.ru/vacancy/123" in result
    assert "100000" in result
    assert "1-3 года" in result
    assert "Знание Python, Django" in result
    assert "Москва" in result
    assert "123" in result


def test_lt_operator(vacancies: tuple[Vacancy, Vacancy, Vacancy]) -> None:
    """Тест оператора меньше"""
    vacancy1, vacancy2, vacancy3 = vacancies

    assert vacancy1 < vacancy2  # 100000 < 150000
    assert vacancy3 < vacancy1  # 0 < 100000
    assert not vacancy2 < vacancy1  # 150000 не < 100000


def test_lt_operator_invalid_type(sample_vacancy: Vacancy) -> None:
    """Тест оператора меньше с неверным типом"""
    with pytest.raises(TypeError):
        _ = sample_vacancy < "not a vacancy"


def test_eq_operator(vacancies: tuple[Vacancy, Vacancy, Vacancy]) -> None:
    """Тест оператора равенства"""
    vacancy1, vacancy2, _ = vacancies

    same_salary_vacancy = Vacancy(
        name="Different Job",
        url="https://hh.ru/vacancy/126",
        salary=100000,
        experience="1-3 года",
        requirement="Different requirements",
        city="Москва",
        id=126,
    )

    assert vacancy1 == same_salary_vacancy  # Зарплаты равны
    assert not vacancy1 == vacancy2  # Зарплаты разные


def test_eq_operator_invalid_type(sample_vacancy: Vacancy) -> None:
    """Тест оператора равенства с неверным типом"""

    result = sample_vacancy == "not a vacancy"
    assert result is False


def test_cast_to_object_list_valid_data(vacancies_data: list[dict]) -> None:
    """Тест преобразования валидных JSON данных в объекты"""
    vacancies = Vacancy.cast_to_object_list(vacancies_data)

    assert len(vacancies) == 2
    assert all(isinstance(v, Vacancy) for v in vacancies)

    # Проверка первой вакансии
    assert vacancies[0].name == "Backend Developer"
    assert vacancies[0].url == "https://hh.ru/vacancy/200"
    assert vacancies[0].salary == 120000
    assert vacancies[0].experience == "3-6 лет"
    assert vacancies[0].requirement == "Python, FastAPI, PostgreSQL"
    assert vacancies[0].city == "Москва"
    assert vacancies[0].id == 200

    # Проверка второй вакансии (без зарплаты)
    assert vacancies[1].name == "Frontend Developer"
    assert vacancies[1].salary == 0
    assert vacancies[1].city == "Санкт-Петербург"
