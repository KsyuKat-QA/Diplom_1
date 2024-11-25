import pytest
from praktikum.bun import Bun

class TestBun:
    @pytest.mark.parametrize("name, price", [
        ("Bugrer 1", 100),
        ("Bugrer 2", 66.6),
        ("Bugrer 3", 332)
    ])

    def test_init(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price