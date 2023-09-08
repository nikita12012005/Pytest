import pytest

from test.human import Human

class TestHuman:
    def test_initialization(self):
        human = Human(name='John', age=32, gender='male')

        assert human.age == 32, "Age should be 32"
        assert human.gender == 'male', "Gender should be male"

    def test_grow(self):
        human = Human(name='John', age=30, gender='male')
        human.grow()
        assert human.age == 31, "Age should increase by 1"

    def test_change_gender(self):
        human = Human(name='John', age=30, gender='male')
        human.change_gender('female')
        assert human.gender == 'female', "Gender should change to female"

    def test_change_gender_same_as_before(self):
        human = Human(name='John', age=30, gender='male')
        with pytest.raises(Exception) as excinfo:
            human.change_gender('male')
        assert str(excinfo.value) == "Cannot change to the same gender", "Exception message should match"

    def test_change_gender_invalid_gender(self):
        human = Human(name='John', age=30, gender='male')
        with pytest.raises(Exception) as excinfo:
            human.change_gender('invalid')
        assert str(excinfo.value) == "Invalid gender specified", "Exception message should match"

    def test_get_age(self):
        human = Human(name='John', age=30, gender='male')
        assert human.age == 30, "Age should be 30"

    def test_get_gender(self):
        human = Human(name='John', age=30, gender='male')
        assert human.gender == 'male', "Gender should be male"
