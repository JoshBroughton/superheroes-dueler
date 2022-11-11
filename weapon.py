import random
from ability import Ability

class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        min_damage = self.max_damage // 2
        return random.randint(min_damage, self.max_damage)