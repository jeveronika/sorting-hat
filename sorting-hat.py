## this code determines, which Hogwarts house you belong to:


import random
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
random_house = random.choice(houses).upper()

name = input("Enter your name: ")

print(f"The sorting hat has decided, you {name}, you belong to {random_house}!!!")