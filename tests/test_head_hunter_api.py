from unittest.mock import MagicMock, patch

import requests

from src.head_hunter_api import HeadHunterAPI

api = HeadHunterAPI()


@patch("src.head_hunter_api.requests.get")
def test_connect_to_api_success(mock_get: MagicMock) -> None:
    """Тест успешного подключения к API"""
    mock_response = MagicMock()
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result = api._connect_to_api()

    assert result is True
    mock_get.assert_called_once_with("https://api.hh.ru/vacancies")


@patch("src.head_hunter_api.requests.get")
def test_connect_to_api_failure(mock_get: MagicMock) -> None:
    """Тест неудачного подключения к API"""
    mock_get.side_effect = requests.exceptions.RequestException("Connection error")

    result = api._connect_to_api()

    assert result is False
