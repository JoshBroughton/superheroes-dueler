# hero.py
import random
from ability import Ability
from armor import Armor
from weapon import Weapon


class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        '''Instance properties:
        abilities: List
        armors: List
        name: String
        starting_health: Integer
        current_health: Integer
        '''
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

    # def fight(self, opponent):
    #     fighters = [self.name, opponent.name]
    #     power_levels = [self.current_health, opponent.current_health]
    #     winner = random.choices(fighters, power_levels)[0]
    #     winner_index = fighters.index(winner)
    #     if winner_index == 0:
    #         loser = fighters[1]
    #     else:
    #         loser = fighters[0]
    #     print(f'{winner} defeats {loser}!')
    #     return winner

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        # We use the append method to add ability objects to our list.
        self.abilities.append(ability)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
            return: total_damage:Int
        '''

        # start our total out at 0
        total_damage = 0
        # loop through all of our hero's abilities
        for ability in self.abilities:
            # add the damage of each attack to our running total
            total_damage += ability.attack()
        # return the total damage
        return total_damage

    def add_armor(self, armor):
        '''Add armor to self.armors
            Armor: Armor Object
        '''
        self.armors.append(armor)

    def defend(self):
        '''Calculate the total block amount from all armor blocks.
            return: total_block:Int
        '''
        total_blocked = 0
        for armor in self.armors:
            total_blocked += armor.block()
        if self.current_health == 0:
            total_blocked = 0

        return total_blocked

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        damage -= self.defend()
        if damage > 50:
            print('Ouch')
        elif damage > 25:
            print('Wowza')
        elif damage > 10:
            print('hmm')
        elif damage > 5:
            print('Pathetic')
        elif damage > 0:
            print('Huh?')
        else:
            print('I am impenetrable')

        if damage > 0:
            self.current_health -= damage
        if self.current_health <= 0:
            print('I am slain')

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.
        '''
        return self.current_health >= 0

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        if not self.abilities and not opponent.abilities:
            print('Draw')
            return

        while self.is_alive() and opponent.is_alive():
            opponent.take_damage(self.attack())
            self.take_damage(opponent.attack())
            if not opponent.is_alive() and self.is_alive():
                print(f'{self.name} has won!')
                opponent.add_death(1)
                self.add_kill(1)
            elif not self.is_alive() and opponent.is_alive():
                print(f'{opponent.name} has won!')
                self.add_death(1)
                opponent.add_kill(1)
            elif not self.is_alive() and not opponent.is_alive():
                print('Mutual destruction has occured')
                opponent.add_death(1)
                self.add_kill(1)
                self.add_death(1)
                opponent.add_kill(1)

    def add_weapon(self, weapon):
        """Add weapon to self.abilities"""
        self.abilities.append(weapon)

    def add_kill(self, num_kills):
        ''' Update self.kills by num_kills amount'''
        self.kills += num_kills

    def add_death(self, num_deaths):
        ''' Update deaths with num_deaths'''
        self.deaths += num_deaths


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.
    # ability = Ability("Great Debugging", 50)
    # another_ability = Ability("Smarty Pants", 90)
    # hero = Hero("Grace Hopper", 200)
    # hero.add_ability(ability)
    # hero.add_ability(another_ability)
    # armor_1 = Armor('Plate', 25)
    # armor_2 = Armor('Chain', 15)
    # hero.add_armor(armor_1)
    # hero.add_armor(armor_2)
    # print(hero.defend())
    # hero = Hero("Grace Hopper", 200)
    # hero.take_damage(150)
    # print(hero.is_alive())
    # hero.take_damage(15000)
    # print(hero.is_alive())
    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")
    # ability1 = Ability("Super Speed", 300)
    # ability2 = Ability("Super Eyes", 130)
    # ability3 = Ability("Wizard Wand", 300)
    # ability4 = Ability("Wizard Beard", 20)
    # armor_1 = Armor('Wizard Hat', 100)
    # hero1.add_ability(ability1)
    # hero1.add_ability(ability2)
    # hero2.add_ability(ability3)
    # hero2.add_ability(ability4)
    # hero2.add_armor(armor_1)
    # hero1.fight(hero2)
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
