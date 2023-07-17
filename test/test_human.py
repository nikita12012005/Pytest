import unittest

from Pytest.human import Human


class TestHuman(unittest.TestCase):
    def setUp(self):
        self.human = Human("John", 30, "male")

    def test_grow(self):
        self.human.grow()
        self.assertEqual(self.human.age, 31)

    def test_grow_past_age_limit(self):
        self.human._Human__age = 100
        self.human.grow()
        self.assertEqual(self.human.age, 100)
        self.assertEqual(self.human._Human__status, "dead")

    def test_change_gender(self):
        self.human.change_gender("female")
        self.assertEqual(self.human.gender, "female")

    def test_change_gender_same_as_current(self):
        with self.assertRaises(Exception) as context:
            self.human.change_gender("male")
        self.assertEqual(str(context.exception), "John already has gender 'male'")

    def test_change_gender_invalid(self):
        with self.assertRaises(Exception) as context:
            self.human.change_gender("invalid")
        self.assertEqual(str(context.exception), "Not correct name of gender")

    def test_is_alive(self):
        self.assertTrue(self.human._Human__is_alive())

    def test_is_not_alive(self):
        self.human._Human__status = "dead"
        with self.assertRaises(Exception) as context:
            self.human._Human__is_alive()
        self.assertEqual(str(context.exception), "John is already dead...")

if __name__ == '__main__':
    unittest.main()
