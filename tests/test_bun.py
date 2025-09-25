import pytest
from src.test_data import BumData


class TestBun:

    def test_get_bun(self, make_bun):
        assert make_bun.get_name() == BumData.BUM_NAME

    def test_get_bun_price(self, make_bun):
        assert make_bun.get_price() == BumData.BUM_PRICE
