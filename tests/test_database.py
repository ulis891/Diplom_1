from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
import allure


@allure.feature("Тестирование базы данных")
class TestDatabase:

    @allure.story("Тестирование доступных булочек")
    def test_available_buns(self, db: Database):
        buns = db.available_buns()
        assert isinstance(buns, list)
        for bun in buns:
            assert isinstance(bun, Bun)

    @allure.story("Тестирование доступных ингредиентов")
    def test_avalible_ingredients(self, db: Database):
        ingredients = db.available_ingredients()
        assert isinstance(ingredients, list)
        for ingredient in ingredients:
            assert isinstance(ingredient, Ingredient)
