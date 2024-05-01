import random
import re
import matplotlib.pyplot as plt

class Pet():
    def __init__(self, name):
        self.name = name
        self.health = 0
        self.happiness = 0
        self.cleaniness = 0
        self.hunger = 0
        self.tiredness = 0
        self.pet_attributes()
        
    def pet_attributes(self):
        self.health = random.randint(50, 100) 
        self.happiness = random.randint(0, 100)  
        self.cleanliness = random.randint (0, 100) 
        self.hunger = random.randint(0, 100) 
        self.tiredness = random.randint(0, 100)
    
    def update_stats(self, stats):
        self.health = int(stats[0])
        self.happiness = int(stats[1])
        self.cleaniness = int(stats[2])
        self.hunger = int(stats[3])
        self.tiredness = int(stats[4])
        
    def pet_emotion(self):
        
        attributes = ['Health', 'Happiness', 'Cleanliness', 'Hunger','Tiredness']
        values = [self.health, self.happiness, self.cleaniness, self.hunger,
                  self.tiredness]
        
        plt.figure(figsize=(10,5))
        plt.bar(attributes, values, color = ['blue', 'pink', 'orange', 'yellow', 
                                             'purple'])
        plt.title(f"{self.name}'s Emotions")
        plt.xlabel('Attributes')
        plt.ylabel('Values')
        plt.show()  
    
    def __str__(self):
        return (f"Pet: {self.name}, Health: {self.health}, Happiness: {self.happiness},"
                f"Cleaniness: {self.cleaniness}, Hunger: {self.hunger}, "
                f"Tiredness: {self.tiredness} ")
     
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

def menu(pet):
    print("Welcome to the virtual pet menu!")
    print("1. Feed")
    print("2. Clean")
    print("3. Hug")
    print("4. Play")
    print("5. Water")
    print("6. Nap")
    print("7. Pet")
    print(f"8. See {pet_name}'s stats")
    random_behavior("random_behavior.txt", pet)
    choice = input("Please select an option: ")
    if choice == "1":
        food_dict, food_options = pet.read_food_list()
        print("Available food options:", ", ".join(food_options)) 
        food = input("What food would you like to feed your pet? ")
        result = eat(pet, food)
        print(result)
    elif choice == "2":
        print("Cleaning pet...")
    elif choice == "3":
        print("Hugging pet...")
        hug_pet(pet)
    elif choice == "4":
        print("Playing with pet...")
    elif choice == "5":
        print("Watering pet...")
        water_pet(pet)
    elif choice == "6":
        nap_pet(pet)
    elif choice == "7":
        pet_pet(pet)
    elif choice == "8":
        pet.pet_emotion()
    else:
        print("Invalid choice. Please select a valid option.")
        
def nap_pet(pet):
    pet.tiredness -= 10
    print(f"{pet.name} is now in bed and resting. ")
        
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

def clean(pet, self):
    
    clean_amount = 20
    
    self.cleanliness = min(self.cleanliness + clean_amount, 100)
    
    
    self.happiness = max(self.happiness - 5, 0)
    
    
    self.tiredness = max(self.tiredness - 5, 0)
    
    
    print(f"{self.name} has now been cleaned. Cleanliness score is now at {self.cleanliness}.")
    
    print(f"Hapiness is now at {self.happiness} and tiredness is now {self.tiredness}.")
    
def pet_pet(pet):
    pet.happiness += 10
    pet.tiredness -= 7
    
    print(f"{pet.name} is happy! ")
    
def water_pet(pet):
    pet.health += 2
    pet.hunger += 3
    print(f"{pet.name} drank some water!")

def hug_pet(pet):
    pet.happiness += 10
    pet.cleaniness -= 3
    random_num = random.randint(0,1)
    print (f"{pet_name} hugged you back!" if random_num == 0 else f"{pet_name} did not hug you back")
    
        
def wellbeing_pet(pet):
    pet_stats = [pet.health, pet.happiness, pet.cleanliness, pet.hunger, pet.tiredness]
   
    unhappy_stats = [attr for attr in pet_stats if attr <= 60]

    if len(unhappy_stats) >= 4:
        print(f"{pet.name} needs care.")
    elif len(unhappy_stats) >= 2 and len(unhappy_stats) <= 3:
        print(f"{pet.name} is feeling ok.")
    else:
        print(f"{pet.name} is happy!")

# testing
if __name__ == "__main__":
    pet_name = input("Please input a name for your pet!\n")
    curr_pet = Pet(pet_name)
    menu(curr_pet)
