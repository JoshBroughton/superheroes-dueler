"""
Defines a team class that manages a team of superheroes
"""
import random

class Team:
    """
    Team class, which manages a list of Hero objects
    """

    def __init__(self, name):
        ''' Initialize your team with its team name and an empty list of heroes
        '''
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        found_hero = False
        # loop through each hero in our list
        for hero in self.heroes:
            # if we find them, remove them from the list
            if hero.name == name:
                self.heroes.remove(hero)
                # set our indicator to True
                found_hero = True
        # if we looped through our list and did not find our hero,
        # the indicator would have never changed, so return 0
        if not found_hero:
            return 0

    def view_all_heroes(self):
        """Prints out all heroes in the list to the console"""
        for hero in self.heroes:
            print(f'Hero Name: {hero.name}')

    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
        self.heroes.append(hero)

    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            if hero.deaths > 0:
                kill_death_ratio = hero.kills / hero.deaths
                print(f"{hero.name} Kill/Deaths:{kill_death_ratio}")
            else:
                print(f'{hero.name} has {hero.kills} kills and has not died!')

    def revive_heroes(self):
        ''' Reset all heroes health to starting_health'''
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        ''' Battle each team against each other.'''

        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents)> 0:
            fighter = random.choice(living_heroes)
            opponent = random.choice(living_opponents)

            fighter.fight(opponent)

            if not fighter.is_alive():
                living_heroes.remove(fighter)
            
            if not opponent.is_alive():
                living_opponents.remove(opponent)