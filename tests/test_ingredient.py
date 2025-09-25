import pytest
from src.test_data import IngredientData as ID


class TestIngredient:
    def test_ingredient_get_type(self, make_ingredient):
        assert make_ingredient.get_type() == ID.INGREDIENT_TYPE

    def test_ingredient_get_name(self, make_ingredient):
        assert make_ingredient.get_name() == ID.INGREDIENT_NAME

    def test_ingredient_get_price(self, make_ingredient):
        assert make_ingredient.get_price() == ID.INGREDIENT_PRICE
