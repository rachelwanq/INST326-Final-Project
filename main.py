import random
import re

class Pet():
    def __init__(self, name):
        self.name = name
        self.health = 0
        self.happiness = 0
        self.cleaniness = 0
        self.hunger = 0
        self.tiredness = 0
        
    def update_stats(self, stats):
        self.health = int(stats[0])
        self.happiness = int(stats[1])
        self.cleaniness = int(stats[2])
        self.hunger = int(stats[3])
        self.tiredness = int(stats[4])
        
    def read_food_list(self, file_name="list_of_foods.txt"):
        foods = {}
        food_options = []
        
        with open(file_name, "r") as file:
            for line in file:
                line = line.strip()
                if line: 
                    split_line = re.split(r',\s*', line)
                    if len(split_line) == 2:
                        food, health_bonus = split_line
                        foods[food] = int(health_bonus)
                        food_options.append(food)
            
        return foods, food_options

def random_behavior(filename, pet):
    final_choice = ""
    with open(filename, "r", encoding = "utf-8") as file:
        lines = file.readlines()
        final_choice = random.choice(lines).strip()
    
    list_of_stats = final_choice.split(",")
    updating = list_of_stats[1:6]
    pet.update_stats(updating)
    print(list_of_stats[0])
    
# if __name__ == "__main__":
#     dog = Pet("Harry")
#     print(dog.cleaniness)
#     random_behavior("random_behavior.txt", dog)
#     print(dog.cleaniness)

def eat(pet, food, file_name="list_of_foods.txt"):
    food_dict, food_options = pet.read_food_list(file_name)
    food = food.lower()
    
    if food in food_dict:
        pet.health += food_dict[food]
        return f"{pet.name} enjoyed the {food} and gained {food_dict[food]}"\
                " health!"
                
    return f"Sorry, {pet.name} doesn't want to eat {food}."

# Testing
# if __name__ == "__main__":
#     dog = Pet("Buddy")
#     foods, food_options = dog.read_food_list()
#     # print("Available food options:", ", ".join(food_options))
#     print("Initial health:", dog.health)
#     message = eat(dog, "orange")
#     print(message)
#     print("New health:", dog.health)