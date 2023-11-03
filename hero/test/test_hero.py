from unittest import TestCase, main

from project.hero import Hero



class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero("Dagger", 15, 165.5, 25.5)

    def test_init_hero(self):
        self.assertEqual("Dagger", self.hero.username)
        self.assertEqual(15, self.hero.level)
        self.assertEqual(165.5, self.hero.health)
        self.assertEqual(25.5, self.hero.damage)

    def test_battle_with_enemy_name_equal_to_hero_name(self):
        self.assertEqual("Dagger", self.hero.username)
        self.enemy_hero = Hero("Dagger", 15, 125, 16)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_if_hero_health_is_negative(self):
        self.heroNeg = Hero("MAx", 15, -16, 7)
        self.enemy_hero = Hero("Dagger", 15, 125, 16)
        with self.assertRaises(ValueError) as ex:
            self.heroNeg.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_if_raises_Value_error_hero_health_is_zero(self):
        self.heroNeg = Hero("MAx", 15, 0, 7)
        self.enemy_hero = Hero("Dagger", 15, 125, 16)
        with self.assertRaises(ValueError) as ex:
            self.heroNeg.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_if_raises_when_enemyhealth_neg(self):
        self.enemy_hero = Hero("Wizard", 15, -6, 16)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)
        self.assertEqual("You cannot fight Wizard. He needs to rest", str(ex.exception))

    def test_if_raises_when_enemyhealth_isZero(self):
        self.enemy_hero = Hero("Wizard", 15, 0, 16)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)
        self.assertEqual("You cannot fight Wizard. He needs to rest", str(ex.exception))


    def test_heroes_in_battle(self):
        self.enemy_hero = Hero("Wizard", 5, 140, 20)
        self.heroDag = Hero("Dag", 5, 200, 25)
        res = self.heroDag.battle(self.enemy_hero)
        self.assertEqual(100, self.heroDag.health)
        self.assertEqual(20, self.enemy_hero.health)
        self.assertEqual(6, self.enemy_hero.level)
        self.assertEqual(25, self.enemy_hero.damage)
        self.assertEqual("You lose", res)

    def test_heroes_and_enemy_in_battle_neg_health(self):
        self.enemy_hero = Hero("Wizard", 7, 140, 30)
        self.heroDag = Hero("Dag", 10, 200, 25)
        res = self.heroDag.battle(self.enemy_hero)
        self.assertEqual("Draw", res)

    def test_heroes_and_enemy_in_battle_zero_health(self):
        self.enemy_hero = Hero("Wizard", 10, 140, 20)
        self.heroDag = Hero("Dag", 7, 200, 20)
        res = self.heroDag.battle(self.enemy_hero)
        self.assertEqual("Draw", res)

    def test_enemy_after_battle_neg_health(self):
        self.enemy_hero = Hero("Wizard", 7, 140, 10)
        self.heroDag = Hero("Dag", 10, 200, 25)
        res = self.heroDag.battle(self.enemy_hero)
        self.assertEqual("You win", res)
        self.assertEqual(11, self.heroDag.level)
        self.assertEqual(135, self.heroDag.health)
        self.assertEqual(30, self.heroDag.damage)

    def test_enemy_after_battle_zero_health(self):
        self.enemy_hero = Hero("Wizard", 7, 140, 10)
        self.heroDag = Hero("Dag", 7, 200, 20)
        res = self.heroDag.battle(self.enemy_hero)
        self.assertEqual("You win", res)
        self.assertEqual(8, self.heroDag.level)
        self.assertEqual(135, self.heroDag.health)
        self.assertEqual(25, self.heroDag.damage)

    def test_str_method_hero(self):
        self.assertEqual("Hero Dagger: 15 lvl\nHealth: 165.5\nDamage: 25.5\n", self.hero.__str__())



if __name__ == "__main__":
    main()

    main()

