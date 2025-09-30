import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from praktikum.database import Database as DB
from src.test_data import BunData as BD, IngredientData as ID
import allure


@pytest.fixture
@allure.step("Создаём булку")
def make_bun():
    return Bun(BD.BUN_NAME, BD.BUN_PRICE)


@pytest.fixture
@allure.step("Создаём ингредиент")
def make_ingredient():
    return Ingredient(ID.INGREDIENT_TYPE, ID.INGREDIENT_NAME, ID.INGREDIENT_PRICE)


@pytest.fixture
@allure.step("Создаём бургер")
def burger():
    return Burger()


@pytest.fixture
@allure.step("Создаём бургер с одним ингредиентом")
def burger_with_ingredient(make_bun, make_ingredient):
    burger = Burger()
    burger.set_buns(make_bun)
    burger.add_ingredient(make_ingredient)
    return burger


@pytest.fixture
@allure.step("Создаём бургер с тремя ингредиентами")
def burger_with_three_ingredients(burger, make_bun):
    burger.set_buns(make_bun)
    for ingredient in ID.INGREDIENTS_TEST_DATA:
        burger.add_ingredient(ingredient)
    return burger


@pytest.fixture
@allure.step("Создаём базу данных")
def db():
    return DB()
