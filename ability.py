'''
Defines an Ability class to use with Hero objects.
'''
import random

class Ability:
    def __init__(self, name, max_damage):
        '''
        Initialize the values passed into this
        method as instance variables.
        '''
        # Assign the "name" and "max_damage"
        # for a specific instance of the Ability class
        self.name = name
        self.max_damage = int(max_damage)

    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''
        # Pick a random value between 0 and self.max_damage
        attack_damage = random.randint(0, self.max_damage)
        return attack_damage



if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())