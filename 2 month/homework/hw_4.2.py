from enum import Enum
from random import randint, choice


class SuperAbility(Enum):
    HEAL = 1
    BOOST = 2
    CRITICAL_DAMAGE = 3
    BLOCK_AND_REVERT = 4
    REVIVE = 5
    HACK = 6
    BOOM = 7
    SHIELD = 8


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        GameEntity.__init__(self, name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        random_hero = choice(heroes)
        self.__defence = random_hero.ability

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                if type(hero) == Berserk and self.defence != SuperAbility.BLOCK_AND_REVERT:
                    hero.blocked_damage = choice([5, 10])
                    hero.health -= (self.damage - hero.blocked_damage)
                else:
                    hero.health -= self.damage

                if hero.health <= 0 and type(hero) == Bomber:
                    hero.apply_super_power(self, heroes)

    def __str__(self):
        return 'BOSS ' + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        GameEntity.__init__(self, name, health, damage)
        self.__ability = ability
        self.original_damage = damage

    @property
    def ability(self):
        return self.__ability

    def __str__(self):
        return super().__str__() + f' ability: {self.__ability.name}'

    def attack(self, boss):
         boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coef = randint(2, 5)  # 2,3,4
        boss.health -= coef * self.damage
        print(f'Warrior {self.name} hits boss critically: {coef * self.damage}')


class Magic(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.BOOST)
        self.rounds = 0

    def apply_super_power(self, boss, heroes):
        if self.health > 0 and self.rounds < 4:
            boost = randint(1, 10)
            print(f"Magic {self.name} boosts all heroes' damage by: {boost}")
            for hero in heroes:
                if hero.health > 0:
                    hero.damage += boost
        else:
            for hero in heroes:
                if hero.health > 0:
                    hero.damage = hero.original_damage

        self.rounds += 1



class Berserk(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.BLOCK_AND_REVERT)
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def apply_super_power(self, boss, heroes):
        boss.health -= self.__blocked_damage
        print(f'Berserk {self.name} reverted damage to boss: {self.__blocked_damage}')


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        Hero.__init__(self, name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.health += self.__heal_points

class Witcher(Hero):
    def __init__(self, name, health):
        super().__init__(name, health, 0, SuperAbility.REVIVE)

    def attack(self, boss):
        pass

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health <= 0:
                hero.health = hero.health + self.health
                self.health = 0
                print(f'Witcher {self.name} revived {hero.name} and die')
                break

class Hacker(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.HACK)
        self.rounds = 0

    def apply_super_power(self, boss, heroes):
        if self.rounds % 2 == 0:
            hack_health = randint(5, 15)
            boss.health -= hack_health
            random_hero1 = choice(heroes)
            random_hero1.health += hack_health
            print(f"Hacker {self.name} hack boss health: {hack_health} and health {random_hero1.name}")
        self.rounds += 1

class Bomber(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.BOOM)

    def apply_super_power(self, boss, heroes):
        if self.health <= 0 < boss.health:
            boss.health -= 100
            print(f"Bomber {self.name} died and damage boss by 100")

class Angel(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.SHIELD)

    def apply_super_power(self, boss, heroes):
        if all(hero.health <= 0 for hero in heroes if isinstance(hero, Medic)):
            for hero1 in heroes:
                if hero1.health > 0 and hero1 != self:
                    health_hero = round(hero1.health * 0.4, 2)
                    hero1.health += health_hero
                    print(f'Angel {self.name} health {hero1.name} by {health_hero}')


round_number = 0


def show_statistics(boss, heroes):
    print(f'ROUND: {round_number} -------------')
    print(boss)
    for hero in heroes:
        print(hero)


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if hero.health > 0 and boss.health > 0 and boss.defence != hero.ability:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)
    show_statistics(boss, heroes)


def is_game_over(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
        return True
    return False


def start_game():
    boss = Boss('Vladislav', 1700, 50)

    warrior_1 = Warrior('Mario', 280, 10)
    warrior_2 = Warrior('Sonic', 270, 15)
    magic = Magic('Maga', 220, 10)
    berserk = Berserk('Berserkbek', 250, 5)
    doc = Medic('Watson', 200, 5, 15)
    assistant = Medic('Yunga', 280, 5, 5)
    witcher = Witcher('Vedi', 220)
    hacker = Hacker('pirate', 190, 5)
    bomber = Bomber('Dynamite', 170, 5)
    angel = Angel('Postecoglou', 300, 1)
    heroes_list = [warrior_1, assistant, warrior_2, magic, berserk, doc, witcher, hacker, bomber, angel]

    show_statistics(boss, heroes_list)

    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)


start_game()