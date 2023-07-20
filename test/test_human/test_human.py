import pytest

from test.human import Human


class TestHuman:
    def test_initialization(self):
        human = Human(name='John', age=32, gender='male')

        assert human.age == 32
        assert human.gender == 'male'

    def test_grow(self):
        human = Human(name='John', age=30, gender='male')
        human.grow()
        assert human.age == 31

    def test_change_gender(self):
        human = Human(name='John', age=30, gender='male')
        human.change_gender('female')
        assert human.gender == 'female'

    def test_change_gender_same_as_before(self):
        human = Human(name='John', age=30, gender='male')
        with pytest.raises(Exception):
            human.change_gender('male')

    def test_change_gender_invalid_gender(self):
        human = Human(name='John', age=30, gender='male')
        with pytest.raises(Exception):
            human.change_gender('invalid')

    def test_get_age(self):
        human = Human(name='John', age=30, gender='male')
        assert human.age == 30

    def test_get_gender(self):
        human = Human(name='John', age=30, gender='male')
        assert human.gender == 'male'
