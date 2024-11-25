import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from typing import List

class TestBurger:
    @pytest.fixture # создаем экземпляр (объект) класса Burger
    def burger(self):
        return Burger()

    @pytest.fixture # создаем экземпляр (объект) класса Bun (начинка)
    def bun(self):
        bun = Bun("Some bun", 50)
        return bun

    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun == bun

    @pytest.fixture
    def ingredient(self):
        ingredient = Ingredient("FILLING", "Some ingr1", 50)
        return ingredient

    @pytest.fixture
    def ingredient2(self):
        ingredient2 = Ingredient("SAUCE", "Some ingr2", 35)
        return ingredient2

    def test_add_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    def test_remove_ingredient(self, burger, ingredient):
        assert len(burger.ingredients)==0
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients)==1
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, burger, ingredient,ingredient2):
        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0,1)
        assert burger.ingredients[0]==ingredient2 and burger.ingredients[1]==ingredient

    def test_get_price(self, burger, bun, ingredient):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        assert burger.get_price()==bun.price*2+ingredient.get_price()

    def test_get_receipt(self, burger, bun, ingredient):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        receipt: List[str] = [f'(==== {bun.get_name()} ====)']
        receipt.append(f'= {str(ingredient.get_type()).lower()} {ingredient.get_name()} =')
        receipt.append(f'(==== {bun.get_name()} ====)\n')
        receipt.append(f'Price: {bun.price*2+ingredient.get_price()}')
        assert burger.get_receipt()=='\n'.join(receipt)