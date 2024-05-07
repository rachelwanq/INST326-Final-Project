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
        self.happiness = random.randint(50, 100)  
        self.cleanliness = random.randint (50, 100) 
        self.hunger = random.randint(50, 100) 
        self.tiredness = random.randint(50, 100)
    
    def update_stats(self, stats):
        self.health += int(stats[0])
        self.happiness += int(stats[1])
        self.cleaniness += int(stats[2])
        self.hunger += int(stats[3])
        self.tiredness += int(stats[4])
        
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
        """Read and parse a list of foods and their associated health bonuses 
        from a text file.

        Args:
            file_name (str, optional): The name of the text file containing the 
                list of foods and health bonuses. Defaults to 
                "list_of_foods.txt".

        Returns:  
            tuple: A tuple containing two elements:
                - dict: A dictionary where keys are food names and values are 
                    their corresponding health bonuses.
                - list: A list of food names extracted from the file.
    
        Note:
            The text file should have each line formatted as 
            "food,health_bonus", where 'food' is the name of the food and 
            'health_bonus' is its associated health bonus.
            Example: "carrot,+2"
        """
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
    menu_options = {
        "1": "Feed",
        "2": "Clean",
        "3": "Hug",
        "4": "Play",
        "5": "Water",
        "6": "Nap",
        "7": "Pet",
        "8": f"See {pet.name}'s stats",
        "9": "Cancel"
    }
    while True:
        for key, value in menu_options.items():
            print(f"{key}, {value}")
        random_behavior("random_behavior.txt", pet)
        choice = input("Please select an option: ")
        if choice.lower() == "cancel":
            break
        action = menu_options.get(choice)
        if action:
            if action == "Feed":
                food_dict, food_options = pet.read_food_list()
                print("Available food options:", ", ".join(food_options))
                food = input("What food would you like to feed your pet? ")
                result = eat(pet,food)
                print(result)
            elif action == "Clean":
                clean(pet)
            elif action == "Hug":
                hug_pet(pet)
            elif action == "Play":
                print("Playing with pet...")
            elif action == "Water":
                water_pet(pet)
            elif action == "Nap":
                nap_pet(pet)
            elif action == "Pet":
                pet_pet(pet)
            elif action.startswith("See"):
                wellbeing_pet(pet)
                pet.pet_emotion()
            else:
                print("Invalid option. Please select a valid option.")
        continue       
        
def nap_pet(pet):
    pet.tiredness += 10
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

def eat(pet, food, file_name="list_of_foods.txt"):
    """Feed a pet with a specific food and update its health accordingly.

    Args:
        pet (Pet): The pet object to feed.
        food (str): The name of the food to feed the pet.
        file_name (str, optional): The name of the text file containing the list 
            of foods and health bonuses. Defaults to "list_of_foods.txt".

    Returns:
        str: A message indicating the outcome of feeding the pet. If the pet 
            eats the food, it returns a message confirming the health gained. 
            If the pet rejects the food, it returns a rejection message.

    Note:
        The 'pet' parameter should be an instance of the Pet class or a subclass 
        with a 'read_food_list' method, which reads and parses a list of foods 
        and their associated health bonuses from the text file 
        "list_of_foods.txt". The 'food' parameter should be a string 
        representing the name of the food to feed the pet. The text file should 
        have each line formatted as "food,health_bonus", where 'food' is the 
        name of the food and 'health_bonus' is its associated health bonus.
        Example: "carrot,+2"
    """
    food_dict, food_options = pet.read_food_list(file_name)
    food = food.lower()
    
    if food in food_dict:
        pet.health += food_dict[food]
        return f"{pet.name} enjoyed the {food} and gained {food_dict[food]}"\
                " health!"
                
    return f"Sorry, {pet.name} doesn't want to eat {food}."

def clean(pet):
    
    clean_amount = 20
    
    pet.cleanliness = min(pet.cleanliness + clean_amount, 100)
    
    pet.happiness = max(pet.happiness - 5, 0)
    
    pet.tiredness = max(pet.tiredness - 5, 0)
    
    
    print(f"{pet.name} has now been cleaned. Cleanliness score is now at {pet.cleanliness}.")
    
    print(f"Hapiness is now at {pet.happiness} and tiredness is now {pet.tiredness}.")
    
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
    pet.cleaniness -= 1
    random_num = random.randint(0,1)
    print (f"{pet_name} hugged you back!" if random_num == 0 else f"You hugged {pet_name} but {pet_name} did not hug you back.")
    
        
def wellbeing_pet(pet):
    pet_stats = [pet.health, pet.happiness, pet.cleanliness, pet.hunger, pet.tiredness]
   
    unhappy_stats = [attr for attr in pet_stats if attr <= 40]

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
