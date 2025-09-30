import allure
from src.test_data import IngredientData as ID


@allure.epic("Тестирование stellarburgers")
@allure.feature("Тестирование класса Ingredient")
class TestIngredient:

    @allure.step("Создание ингредиента")
    def test_ingredient_get_type(self, make_ingredient):
        assert make_ingredient.get_type() == ID.INGREDIENT_TYPE

    @allure.step("Получение имени ингредиента")
    def test_ingredient_get_name(self, make_ingredient):
        assert make_ingredient.get_name() == ID.INGREDIENT_NAME

    @allure.step("Получение цены ингредиента")
    def test_ingredient_get_price(self, make_ingredient):
        assert make_ingredient.get_price() == ID.INGREDIENT_PRICE
