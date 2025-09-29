import pytest
from src.test_data import IngredientData as ID
from src.test_data import BurgerData
from src.moks import *
import allure


@allure.feature("Тестирование класса Burger")
class TestBurger:

    @allure.story("Тестирование метода set_buns")
    def test_set_buns(self, burger, make_bun):
        burger.set_buns(make_bun)
        assert burger.bun == make_bun

    @allure.story("Тестирование метода add_ingredient")
    def test_add_ingredients(self, burger, make_ingredient):
        burger.add_ingredient(make_ingredient)
        assert make_ingredient in burger.ingredients

    @allure.story("Тестирование метода remove_ingredient")
    def test_remove_ingredient(self, burger_with_ingredient):
        burger_with_ingredient.remove_ingredient(0)
        assert len(burger_with_ingredient.ingredients) == 0

    @allure.story("Тестирование метода move_ingredient")
    def test_move_ingredient(self, burger_with_three_ingredients):
        original_ingredients = burger_with_three_ingredients.ingredients.copy()
        original_ingredients.insert(2, original_ingredients.pop(0))
        burger_with_three_ingredients.move_ingredient(0, 2)
        for i in range(3):
            assert original_ingredients[i] == burger_with_three_ingredients.ingredients[i]

    @allure.story("Тестирование метода get_price")
    @pytest.mark.parametrize("test_burger", BurgerData.TEST_BURGERS)
    def test_get_price(self, burger, test_burger):
        bun_name = test_burger["bun"][0]
        bun_price = test_burger["bun"][1]
        mock_bun = make_mock_bun(bun_name, bun_price)
        for i in test_burger["ingredients"]:
            ingredient_type = i[0]
            ingredient_name = i[1]
            ingredient_price = i[2]
            mock_ingredient = make_mock_ingredient(ingredient_type, ingredient_name, ingredient_price)
            burger.add_ingredient(mock_ingredient)
        burger.set_buns(mock_bun)
        expected_price = test_burger["price"]
        assert burger.get_price() == expected_price

    @allure.story("Тестирование метода get_receipt")
    def test_get_receipt(self, burger_with_ingredient):
        receipt = burger_with_ingredient.get_receipt()
        assert isinstance(receipt, str)
        assert ID.INGREDIENT_TYPE.lower() in receipt
        assert ID.INGREDIENT_NAME in receipt
        assert "Price:" in receipt
