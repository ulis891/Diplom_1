import allure
from src.test_data import BunData as BD


@allure.feature("Тестирование класса Bun")
class TestBun:

    @allure.story("Тестирование инициализации класса Bun")
    def test_init_bun(self, make_bun):
        assert make_bun.name == BD.BUN_NAME
        assert make_bun.price == BD.BUN_PRICE

    @allure.story("Тестирование метода get_name класса Bun")
    def test_get_bun(self, make_bun):
        assert make_bun.get_name() == BD.BUN_NAME

    @allure.story("Тестирование метода get_price класса Bun")
    def test_get_bun_price(self, make_bun):
        assert make_bun.get_price() == BD.BUN_PRICE
