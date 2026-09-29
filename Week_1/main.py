#print("Hello, World!")
from superhero import SuperHero


# --------------------------------------------------
# BASIC PYTHON EXAMPLES
# --------------------------------------------------

greeting = "Hello, World!"
my_name = "Juan Huetle"
age = 30

print(greeting)

print(f"{greeting} Dorset Calling")

print(
    f"Your name is {my_name} "
    f"and you are {age} years old"
)


# --------------------------------------------------
# BEFORE OOP
# --------------------------------------------------

# We could store superhero information
# using many separate variables.

superhero_name_1 = "Peter Parker"
superhero_name_2 = "Tony Stark"
superhero_name_3 = "Bruce Banner"

superhero_alias_1 = "Spiderman"
superhero_alias_2 = "Iron Man"
superhero_alias_3 = "The Hulk"

print()
print("WITHOUT OOP")

print(f"{superhero_name_1}: {superhero_alias_1}")
print(f"{superhero_name_2}: {superhero_alias_2}")
print(f"{superhero_name_3}: {superhero_alias_3}")


# --------------------------------------------------
# USING OBJECT-ORIENTED PROGRAMMING
# --------------------------------------------------

print()
print("USING OOP")


# Create the first SuperHero object.
superhero1 = SuperHero()

# Assign values to the object's attributes.
superhero1.name = "Peter Parker"
superhero1.alias = "Spiderman"
superhero1.special_skill = "Web Slinging"


# Create another SuperHero object.
superhero2 = SuperHero()

superhero2.name = "Tony Stark"
superhero2.alias = "Iron Man"
superhero2.special_skill = "Flying"


# Python commonly passes the values directly
# to the constructor.
superhero3 = SuperHero(
    "Bruce Banner",
    "The Hulk",
    "Strength"
)


# --------------------------------------------------
# ACCESSING OBJECT ATTRIBUTES
# --------------------------------------------------

print()

print(
    f"Hero: {superhero1.name}: "
    f"{superhero1.alias}"
)

print(
    f"Hero: {superhero2.name}: "
    f"{superhero2.alias}"
)

print(
    f"Hero: {superhero3.name}: "
    f"{superhero3.alias}"
)


# --------------------------------------------------
# PRINTING OBJECTS
# --------------------------------------------------

print()
print("PRINTING OBJECTS")

# Python automatically calls __str__()
# when the object is passed to print().

print(superhero1)
print(superhero2)
print(superhero3)


# --------------------------------------------------
# LIST OF STRINGS
# --------------------------------------------------

print()
print("LIST OF NAMES")

names = [
    "Peter Parker",
    "Tony Stark",
    "Bruce Banner"
]


# A for loop goes through every item in the list.
for name in names:
    print(name)


# --------------------------------------------------
# LIST OF SUPERHERO OBJECTS
# --------------------------------------------------

print()
print("LIST OF SUPERHERO OBJECTS")

superheroes = [
    superhero1,
    superhero2,
    superhero3
]


for hero in superheroes:
    print(hero)


# --------------------------------------------------
# CREATE OBJECTS DIRECTLY INSIDE A LIST
# --------------------------------------------------

print()
print("DC HEROES")

dc_heroes = [
    SuperHero(
        "Bruce Wayne",
        "Batman",
        "Detective Skills"
    ),

    SuperHero(
        "Clark Kent",
        "Superman",
        "Flying"
    ),

    SuperHero(
        "Diana Prince",
        "Wonder Woman",
        "Speed"
    )
]


for hero in dc_heroes:
    print(hero)