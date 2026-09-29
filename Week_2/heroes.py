from abc import ABC
from interfaces import IFly
from interfaces import IFight


class Being(ABC):
    pass


class SuperHero(Being):
    pass


class HumanHero(SuperHero):
    pass


class Batman(HumanHero, IFly):
    def fly(self):
        print("I am flying with my bat wings")

    def land(self):
        print("I am landing with my bat wings")
        


class Spiderman(HumanHero, IFight):
    def fight(self):
        print("I am fighting and punching")