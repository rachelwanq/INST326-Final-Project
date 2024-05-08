import random
import re
import matplotlib.pyplot as plt
import argparse

class Pet():
    """ The class for the user's pet
    
    Attributes:
        name (str): The name of the pet
        health (int): The health of the pet
        happiness (int): The pets happiness
        cleaniness (int): The pets cleaniness
        hunger (int): The pets hunger
        tiredness (int): The pets tiredness
    
    """
    def __init__(self, name):
        """ Initalizes the pet class
        
        Args:
            name (str): The name of the pet
            health (int): The health of the pet
            happiness (int): The pets happiness
            cleaniness (int): The pets cleaniness
            hunger (int): The pets hunger
            tiredness (int): The pets tiredness
            
        Side effects:
            Initalizes the pets and calls the pet_attributes function
            
        """
        self.name = name
        self.health = 0
        self.happiness = 0
        self.cleaniness = 0
        self.hunger = 0
        self.tiredness = 0
        self.pet_attributes()
        
    def pet_attributes(self):
        """
        Initialize attributes for the pet object.

        This method sets various attributes for the pet object, such as health, 
        happiness, cleanliness, hunger, and tiredness.The attributes are randomly 
        assigned values within a range of 50 to 100, so when the pet is created,
        its attributes will not be zero.

        Args:
            self: The pet object.

        Returns:
            None
        """
        self.health = random.randint(50, 100) 
        self.happiness = random.randint(50, 100)  
        self.cleanliness = random.randint (50, 100) 
        self.hunger = random.randint(50, 100) 
        self.tiredness = random.randint(50, 100)
    
    def update_stats(self, stats):
        """ 
        Updates the stats of the pet from the provided list
        
        Args:
            stats (list of ints or strings): The stats of the pet
            
        Side effects:
            Adds the stats into it's intended attribute. Also changes strings into ints
            if needed
            
        """
        self.health += int(stats[0])
        self.happiness += int(stats[1])
        self.cleaniness += int(stats[2])
        self.hunger += int(stats[3])
        self.tiredness += int(stats[4])
        
    def pet_emotion(self):
        
        """
        This method visualizes the emotional state of the pet object. A bar plot
        is created to show the emotional attributes of each pet, including health,
        happiness, cleanliness, hunger, and tiredness. Each attribute on the bar plot
        is represented by a color to help keep the plots organized and readable
        
        Args:
            self: The pet object
            
        Returns: 
            A box plot that shows the stats of each attribute stat for that pet object.
            We can see how the attributes scores have either increased or decreased 
            after each action that the pet does.    
        """
        
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
        """Return a string representation of the Pet object.

        Returns:
            str: A string containing the name and attributes of the pet.
        """
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
    """
    Display a menu for interacting with a virtual pet

    Args:
        pet (Pet): The virtual pet object to interact with.
        
        This function presents a menu with various options for interacting with the 
        virtual pet. 
        The user can select options such as feeding, cleaning, playing, and checking
        the pet's stats.
    
    Side effects:
        - Prints messages and interacts with the pet object based on user input.
        - May modify the attributes of the pet object based on user actions.
    """
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
    
    [print(f"{key}, {value}") for key, value in menu_options.items()]
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
    """
    Allows the pet to nap
    
    Args:
        pet (Pet): The pet object
        
    Side effects:
        Prints out the pets name along with the resting line. Increases
        the pet tiredness by 10.
        
    """
    pet.tiredness += 10
    print(f"{pet.name} is now in bed and resting. ")
        
def random_behavior(filename, pet):
    """
    Randomly chooses an action for the pet to do
    
    Args:
        filename (str): The name of the file provided
        pet (Pet): The pet object
        
    Side effects:
        Goes through the file and chooses a random action for the pet to do.
        Changes it's stats based on the action. Prints the list of stats.
        
    """
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

    """
    This function cleans the pet and modifies the cleanliness score. 
    It also adjusts the pet's happiness and tiredness attribute scores because
    being cleaned has the ability to make these attributes of the pet decrease.
    
    Args: 
        pet (Pet): The pet object that is being cleaned
        
    Side Effects:
        updates the cleanliness, happiness, and tiredness attribute scores
        for the pet object. Then it prints a message indicating the cleaning
        action and the resulting changes that were made to the attributes score.
    """

    clean_amount = 20
    
    pet.cleanliness = min(pet.cleanliness + clean_amount, 100)
    
    pet.happiness = max(pet.happiness - 5, 0)
    
    pet.tiredness = max(pet.tiredness - 5, 0)
    
    
    print(f"{pet.name} has now been cleaned. Cleanliness score is now at {pet.cleanliness}.")
    
    print(f"Hapiness is now at {pet.happiness} and tiredness is now {pet.tiredness}.")
    
def pet_pet(pet):
    """
    The petting action increases the happiness attribute of the pet object by 10
    and decreases the tiredness attribute by 7.

    Args:
        pet: The pet object to be petted.
    
    Side Effects:
        Prints a message saying the pet is happy.


    """
    pet.happiness += 10
    pet.tiredness -= 7
    
    print(f"{pet.name} is happy! ")
    
def water_pet(pet):
    """
    Allows the user to let the pet drink
    
    Args:
        pet (Pet): The pet object
        
    Side effects:
        Prints out the pet drank water. Adds 2 to the health and 3 to the hunger
        for the pet
        
    """
    pet.health += 2
    pet.hunger += 3
    print(f"{pet.name} drank some water!")

def hug_pet(pet):
    """
    Allows the user to hug the pet
    
    Args:
        pet (Pet): The pet object
        
    Side effects:
        Uses a random number to determine if the pet will hug the user back. Will
        print out the results. Also adds 10 to the happiness of the pet and 
        decreases cleaniness by 1.
    """
    pet.happiness += 10
    pet.cleaniness -= 1
    print (f"{pet_name} hugged you back!" if random.choice([True, False]) else f"You hugged {pet_name} but {pet_name} did not hug you back.")
    
        
def wellbeing_pet(pet):
    """
    Check the wellbeing status of the pet object based on its health, happiness, 
    cleanliness, hunger, and tiredness attributes. 

    Args:
        pet: The pet object to check its wellbeing.

    Side Effects:
        Prints a message stating the pet's wellbeing status.

    """
    pet_stats = [pet.health, pet.happiness, pet.cleanliness, pet.hunger, pet.tiredness]
   
    unhappy_stats = [attr for attr in pet_stats if attr <= 40]

    if len(unhappy_stats) >= 4:
        print(f"{pet.name} needs care.")
    elif len(unhappy_stats) >= 2 and len(unhappy_stats) <= 3:
        print(f"{pet.name} is feeling ok.")
    else:
        print(f"{pet.name} is happy!")

def parse_arguments():
    """Parse command-line arguments
    
    Returns: 
        Namespace: The parsed arguments as a namespace boject.
    """
    parser = argparse.ArgumentParser(description = "Virtual Pet Simulator")
    parser.add_argument("name", type=str, help="The name of the pet")
    return parser.parse_args()
#testing
if __name__ == "__main__":
    args = parse_arguments()
    pet_name = Pet(args.name)
    menu(pet_name)