import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from praktikum.database import Database as DB
from src.test_data import BumData as BD, IngredientData as ID
from unittest.mock import Mock


@pytest.fixture
def make_bun():
    return Bun(BD.BUM_NAME, BD.BUM_PRICE)


@pytest.fixture
def make_ingredient():
    return Ingredient(ID.INGREDIENT_TYPE, ID.INGREDIENT_NAME, ID.INGREDIENT_PRICE)


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def burger_with_ingredient(mock_bun, mock_ingredient):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)
    return burger


@pytest.fixture
def burger_with_three_ingredients(burger, mock_bun):
    burger.set_buns(mock_bun)
    for ingredient in ID.INGREDIENTS_TEST_DATA:
        burger.add_ingredient(ingredient)
    return burger


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_price.return_value = BD.BUM_PRICE
    bun.get_name.return_value = BD.BUM_NAME
    return bun


@pytest.fixture
def mock_ingredient():
    ingredient = Mock()
    ingredient.get_price.return_value = ID.INGREDIENT_PRICE
    ingredient.get_name.return_value = ID.INGREDIENT_NAME
    ingredient.get_type.return_value = ID.INGREDIENT_TYPE
    return ingredient


@pytest.fixture
def db():
    return DB()
