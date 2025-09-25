import pytest
from praktikum.bun import Bun
from src.test_data import TestData


@pytest.fixture
def make_bun():
    return Bun(TestData.BUM_NAME, TestData.BUM_PRICE)
