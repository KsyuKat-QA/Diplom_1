import pytest
from praktikum.ingredient import Ingredient

class TestIngredient:
    @pytest.mark.parametrize("type, name, price", [
        ("Cream", "Ingr 1", 100),
        ("Mayo", "Ingr 2", 66.6),
        ("Ketchup", "Ingr 3", 332)
    ])

    def test_init(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_type() == type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price