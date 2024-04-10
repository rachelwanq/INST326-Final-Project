import random

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
#     random_behavior("randompet.txt", dog)
#     print(dog.cleaniness)