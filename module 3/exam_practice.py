"""
7. Для Warrior сделать метод, который будет менять стойку, всего у него их 2 - это "атакующая" и "защитная"
		- Если у Warrior защитная стойка - входящий урон снижается на 20%
		- Если у Warrior атакующая стойка - исходящий урон повышается на 15%
"""


class Hero:
    def __init__(self, name, health):
        self.name = name
        self.__health = health
        self.still_alive = True

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, amount):
        self.__health = amount
        if self.__health <= 0:
            self.still_alive = False

    def take_damage(self, damage):
        if damage > 0:
            self.health -= damage
        else:
            raise ValueError('Damage can not be < 0')

    def attack(self, target, damage):
        target.take_damage(damage)


class Warrior(Hero):

    def __init__(self, name, health, stance_damage='защитная'):
        super().__init__(name, health)
        self.stance_damage = stance_damage

    def take_damage(self, damage):
        if self.stance_damage == 'защитная':
            damage *= 0.8
            super().take_damage(damage)
        else:
            super().take_damage(damage)

    def attack(self, target, damage):
        if self.stance_damage == 'атакующая':
            damage *= 1.15
            super().attack(target, damage)
        else:
            super().attack(target, damage)

    def switch_stance(self, stance):
        self.stance_damage = stance


class Mage(Hero):
    def __init__(self, name, health, magic_shield):
        super().__init__(name, health)
        self.magic_shield = magic_shield

    def take_damage(self, damage):
        damage *= 1 - self.magic_shield
        super().take_damage(damage)


hero = Hero('Ivan', 200)
warrior = Warrior("warrior", 100)
mage = Mage('mage', 85, 0.7)
hero.take_damage(20)
# assert hero.health == 80
hero.take_damage(80)
# assert hero.health == 0
# print(hero.still_alive)

hero.attack(mage, 10)
# print(mage.health)
# assert mage.health == 70

print(warrior.health)
warrior.take_damage(20)
print(warrior.health)

print(mage.health)
warrior.switch_stance('атакующая')
print(mage.health)
warrior.attack(mage, 20)
print(mage.health)
