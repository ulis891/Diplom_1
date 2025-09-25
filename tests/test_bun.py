import pytest
from src.test_data import TestData


class TestBun:

    def test_get_bun(self, make_bun):
        assert make_bun.get_name() == TestData.BUM_NAME

    def test_get_bun_price(self, make_bun):
        assert make_bun.get_price() == TestData.BUM_PRICE
