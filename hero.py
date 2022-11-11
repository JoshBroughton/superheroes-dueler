# hero.py
import random

class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        '''Instance properties:
        name: String
        starting_health: Integer
        current_health: Integer
        '''
        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health

    def fight(self, opponent):
        fighters = [self.name, opponent.name]
        power_levels = [self.current_health, opponent.current_health]
        winner = random.choices(fighters, power_levels)[0]
        winner_index = fighters.index(winner)
        if winner_index == 0:
            loser = fighters[1]
        else:
            loser = fighters[0]
        print(f'{winner} defeats {loser}!')
        return winner

if __name__ == "__main__":
    my_hero = Hero('Grace Hopper', 200)
    print(my_hero.name)
    print(my_hero.current_health)
    new_hero = Hero('Saitama', 1000)
    my_hero.fight(new_hero)
    count = 0
    grace_wins = 0
    saitama_wins = 0

    while count < 1000:
        if my_hero.fight(new_hero) == 'Grace Hopper':
            grace_wins += 1
        else:
            saitama_wins += 1
        count += 1
    print(f'Grace won {grace_wins}, saitama won {saitama_wins}')
