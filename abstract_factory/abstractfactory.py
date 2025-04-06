from abc import ABC, abstractmethod
import random

class Enemy(ABC):
    @abstractmethod
    def attack(self):
        pass

class Boss(ABC):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def special_attack(self):
        pass

class DesertEnemy(Enemy):
    def attack(self):
        print("Ataca Enemigo con una lanza -5")

class WaterEnemy(Enemy):
    def attack(self):
        print("Ataca Enemigo con chorro de agua -5")

class DesertBoss(Boss):
    def attack(self):
        print("Ataca Jefe con espada -15")

    def special_attack(self):
        print("Ataca Jefe con lluvia de arena -50")

class WaterBoss(Boss):
    def attack(self):
        print("Ataca Jefe con aleta -20")

    def special_attack(self):
        print("Ataca Jefe con remolino de agua -60")

class EnemiesFactory(ABC):
    @abstractmethod
    def create_enemy(self) -> Enemy:
        pass

    @abstractmethod
    def create_boss(self) -> Boss:
        pass

class DesertEnemiesFactory(EnemiesFactory):
    def create_enemy(self) -> Enemy:
        return DesertEnemy()
    
    def create_boss(self) -> Boss:
        return DesertBoss()
    
class WaterEnemiesFactory(EnemiesFactory):
    def create_enemy(self) -> Enemy:
        return WaterEnemy()

    def create_boss(self) -> Boss:
        return WaterBoss()
    
class Game:
    def __init__(self, factory: EnemiesFactory):
        self.__factory = factory
        self.__enemy1 = self.__factory.create_enemy()
        self.__enemy2 = self.__factory.create_enemy()
        self.__boss = self.__factory.create_boss()

    def enemy_attack(self):
        who_attack = random.randint(1, 4)

        match who_attack:
            case 1:
                self.__enemy1.attack()
            case 2:
                self.__enemy1.attack()
            case 3:
                self.__boss.attack()
            case 4:
                self.__boss.special_attack()

# Aplicación
game = Game(WaterEnemiesFactory())      
game.enemy_attack()
game.enemy_attack()
game.enemy_attack()
game.enemy_attack()
game.enemy_attack()
game.enemy_attack()
game.enemy_attack()
game.enemy_attack()    
