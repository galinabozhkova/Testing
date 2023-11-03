from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Bruno", "tiger", "uaaa")

    def test_init_mammal(self):
        self.assertEqual("Bruno", self.mammal.name)
        self.assertEqual("tiger", self.mammal.type)
        self.assertEqual("uaaa", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_sound_of_mammal(self):
        self.assertEqual("uaaa", self.mammal.sound)
        sound = self.mammal.make_sound()
        self.assertEqual("Bruno makes uaaa", sound)

    def test_mammal_kingdom_function(self):
        kingdom = self.mammal.get_kingdom()
        self.assertEqual("animals", kingdom )

    def test_info_function_of_mammal(self):
        info = self.mammal.info()
        self.assertEqual("Bruno is of type tiger", info)


if __name__ == "__main__":
    main()

