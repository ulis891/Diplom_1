from unittest.mock import Mock
import allure


@allure.step("Создаем мок булки")
def make_mock_bun(name, price):
    mock_bun = Mock()
    mock_bun.get_name.return_value = name
    mock_bun.get_price.return_value = price
    return mock_bun


@allure.step("Создаем мок ингредиента")
def make_mock_ingredient(type, name, price):
    mock_ingredient = Mock()
    mock_ingredient.get_name.return_value = name
    mock_ingredient.get_price.return_value = price
    mock_ingredient.get_type.return_value = type
    return mock_ingredient
