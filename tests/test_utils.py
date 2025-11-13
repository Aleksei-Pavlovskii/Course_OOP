from unittest.mock import Mock, patch

from src.utils import get_user_time, sort_vacancies_city


@patch("src.utils.datetime")
def test_get_user_time_morning(mock_datetime: Mock) -> None:
    mock_now = Mock()
    mock_now.hour = 9
    mock_datetime.now.return_value = mock_now
    assert get_user_time() == "Доброе утро"


@patch("src.utils.datetime")
def test_get_user_time_day(mock_datetime: Mock) -> None:
    mock_now = Mock()
    mock_now.hour = 14
    mock_datetime.now.return_value = mock_now
    assert get_user_time() == "Добрый день"


@patch("src.utils.datetime")
def test_get_user_time_evening(mock_datetime: Mock) -> None:
    mock_now = Mock()
    mock_now.hour = 20
    mock_datetime.now.return_value = mock_now
    assert get_user_time() == "Добрый вечер"


@patch("src.utils.datetime")
def test_get_user_time_night(mock_datetime: Mock) -> None:
    mock_now = Mock()
    mock_now.hour = 1
    mock_datetime.now.return_value = mock_now
    assert get_user_time() == "Доброй ночи"


def test_sort_vacancies_city(sample_vacancies):
    """Тест фильтрации по городу"""

    moscow_vacancies = sort_vacancies_city(sample_vacancies, "москва")

    assert len(moscow_vacancies) == 1
    assert moscow_vacancies[0].city == "Москва"
