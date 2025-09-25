import pytest
from src.test_data import IngredientData as ID, BumData as BD


class TestBurger:

    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredients(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    def test_remove_ingredient(self, burger_with_ingredient):
        burger_with_ingredient.remove_ingredient(0)
        assert len(burger_with_ingredient.ingredients) == 0

    def test_move_ingredient(self, burger_with_three_ingredients):
        original_ingredients = burger_with_three_ingredients.ingredients.copy()
        original_ingredients.insert(2, original_ingredients.pop(0))
        burger_with_three_ingredients.move_ingredient(0, 2)
        for i in range(3):
            assert original_ingredients[i] == burger_with_three_ingredients.ingredients[i]

    def test_get_price(self, burger, mock_ingredient, mock_bun):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == BD.BUM_PRICE * 2 + ID.INGREDIENT_PRICE

    def test_get_receipt(self, burger_with_ingredient):
        receipt = burger_with_ingredient.get_receipt()
        assert isinstance(receipt, str)
        assert ID.INGREDIENT_TYPE.lower() in receipt
        assert ID.INGREDIENT_NAME in receipt
        assert "Price:" in receipt
