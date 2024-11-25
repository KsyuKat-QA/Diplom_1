import pytest
from praktikum.database import Database

@pytest.fixture
def database():
    return Database()

class TestDatabase:
    def test_available_buns(self, database):
        buns = database.available_buns()

        assert buns[0].get_name() == "black bun"
        assert buns[1].get_name() == "white bun"
        assert buns[2].get_name() == "red bun"

    def test_available_ingredients(self, database):
        ingredients = database.available_ingredients()

        assert ingredients[0].get_name() == "hot sauce"
        assert ingredients[1].get_name() == "sour cream"
        assert ingredients[2].get_name() == "chili sauce"
        assert ingredients[3].get_name() == "cutlet"
        assert ingredients[4].get_name() == "dinosaur"
        assert ingredients[5].get_name() == "sausage"