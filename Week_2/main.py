from app_data import AppData
from abstract_demo import Dog, Cat, Trex, LandBird, FlyBird
from heroes import HumanHero, Batman
from heroes import HumanHero, Spiderman


print(AppData.APP_VERSION)

dog = Dog("Alfie")
cat = Cat("Bianca")
dog1 = Dog("Fido")
trex = Trex("Tayto")

brian = LandBird("Brian")
fly_bird = FlyBird("Sky")

print(f"Trex {trex.describe()}")
print(f"dog {dog.describe()}")
print(f"cat {cat.describe()}")
print(f"bird {brian.describe()}")
print(f"Brian Jumps {brian.jump()}")
print(f"Sky Jumps {fly_bird.jump()}")
print(f"cat Jumps {cat.jump()}")
print(f"Trex Jumps {trex.jump()}")

human_hero = HumanHero()

batman = Batman()
spiderman = Spiderman()

batman.fly()
batman.land()
spiderman.fight()