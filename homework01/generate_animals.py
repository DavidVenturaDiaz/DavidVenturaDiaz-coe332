import random
import json
import petname

#The following function creates a definition of an animal and returns it.
def create_animal():
        anim_head = ['snake', 'bull', 'lion', 'raven', 'bunny']
        animal = {}
        #Choose a head for the animal randomly from the "anim_head" list
        animal['head'] = anim_head[random.randint(0,4)]
        #Using the petname library, construct a body made up of two random animals
        animal_body = petname.name() + '-' + petname.name()
        animal['body'] = animal_body
        #Random number of arms, which is an even number from 2 to 10
        num_arms = random.randrange(2,11,2)
        animal['arms'] = num_arms
        #Random number of legs, which is a multiple of three from 3 to 12
        num_legs = random.randrange(3,13,3)
        animal['legs'] = num_legs
        #The tail number is equal to the number of arms plus the number of legs
        animal['tail'] = num_arms + num_legs
        return animal

#Declare an empty list to store definitions of an animal
animals_list = []
#Loop 20 times to add twenty animal definitions to the animals_list
for x in range(20):
        animals_list.append(create_animal())
#Create a definition that stores all the animals in a list
bizarre_animals = {'animals': animals_list}

#Dump the data structure "bizarre_animals" to a json file named "animals.json"
with open('animals.json', 'w') as out:
        json.dump(bizarre_animals, out, indent=2)
