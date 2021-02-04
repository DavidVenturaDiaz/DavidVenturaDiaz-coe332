import random
import json

#Open the "animals.json" file, read it, and store its contents in bizarre_animals
with open('animals.json', 'r') as f:
        bizarre_animals = json.load(f)

#Choose a random animal from "bizarre_animals" and print out its information
animal_num = random.randint(0,19)
print('The details of animal number ' + str(animal_num+1) +  ' are:')
print(bizarre_animals['animals'][animal_num])
