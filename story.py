import random

class Player:
    def __init__(self, name, player_class):
        self.name = name
        self.player_class = player_class
        self.stats = {'intelligence': 0, 'strength': 0, 'dexterity': 0, 'luck': 0}
        self.inventory = []
        self.set_stats()
        self.explored_areas = []

    def set_stats(self):
        if self.player_class == "Wizard":
            self.stats['intelligence'] = 8
        elif self.player_class == "Warrior":
            self.stats['strength'] = 8
        elif self.player_class == "Performer":
            self.stats['dexterity'] = 8
        elif self.player_class == "Fool":
            self.stats['luck'] = 8

    def get_advantage(self):
        return max(self.stats, key=lambda key: self.stats[key])

    def add_to_inventory(self, item):
        print(f"\n*{item} has been added to your inventory.*")
        self.inventory.append(item)

    def has_item(self, item):
        return item in self.inventory
    
    def change_stat(self, stat, value):
        print(f"\n*Your {stat} has increased by {value}.*")
        self.stats[stat] += value


def choose_class():
    print("Choose your class:")
    print("1. Wizard")
    print("2. Warrior")
    print("3. Performer")
    choice = input("Enter the number of your choice: ")
    if choice == "1":
        return "Wizard"
    elif choice == "2":
        return "Warrior"
    elif choice == "3":
        return "Performer"
    else:
        print("Invalid choice. You must be lucky, you are now the Fool!")
        return "Fool"

def explore_village(player):
    print("\nAs you walk through the village, you can explore different areas:")
    print("1. Visit the tavern to gather information from the locals.")
    print("2. Investigate the mysterious forest at the edge of the village.")
    print("3. Sneak into the abandoned mansion rumored to be haunted.")
    if player.explored_areas.count("tavern") > 0:
        print("4. Enter the catacombs beneath the village.")
    choice = input("\nEnter the number of the area you want to explore: ")
    
    if choice == "1":
        explore_tavern(player)
    elif choice == "2":
        explore_forest(player)
        
        if player.player_class in ["Fool"] and not player.has_item("torch"):
            print("You discover hidden pathways and stumble upon a torch.")
            player.add_to_inventory("torch")
    elif choice == "3":
        print("\nYou approach the decrepit mansion, its windows boarded up and ivy creeping up the walls.")
        print("You cautiously step inside, wary of what you might find.")
        
        if player.player_class in ["Fool"]:
            if not player.has_item("torch"):
                print("You search the dusty rooms and find another torch.")
                player.add_to_inventory("torch")
    elif choice == "4" and player.explored_areas.count("tavern") > 0:
        explore_catacombs(player)
        
                
    else:
        print("\nYou wander aimlessly and find yourself in a field of wildflowers.")

def explore_catacombs(player):
    while True:
        if not player.has_item("rusty key"):
            print("\nYou approach the entrance to the catacombs, but it is locked.")
            print("You need a key to unlock the door and enter the catacombs.")
            choice = input("Do you want to go back and find one? (yes/no): ").lower()
            if choice == "yes":
                explore_village(player)
            else:
                print("You decide to end your adventure here.")
                return
            
        if not player.has_item("torch"):
            print("\nYou need a torch to navigate the dark catacombs.")
            choice = input("Do you want to go back and find one? (yes/no): ").lower()
            if choice == "yes":
                explore_village(player)
            else:
                print("You decide to end your adventure here.")
                return
        else:
            print("\nInside the catacombs, you encounter various obstacles:")
            print("1. A locked door barring your path.")
            print("2. A dark and narrow corridor filled with traps.")
            print("3. A group of hostile creatures lurking in the shadows.")

            choice = input("\nHow do you want to proceed? (1/2/3): ")
            if choice == "1":
                print("\nYou use your wits to pick the lock and continue forward.")
            elif choice == "2":
                print("\nYou cautiously navigate through the corridor, using your torch to illuminate the way.")
            elif choice == "3":
                print("\nYou prepare for battle and confront the creatures head-on.")
            
            choice = input("\nDo you want to continue exploring the catacombs? (yes/no): ").lower()
            if choice != "yes":
                print("You decide to end your adventure in the catacombs.")
                return

def explore_tavern(player):
    
    if player.explored_areas.count("tavern") > 0:
        print("\nYou have already explored the tavern and gathered information.")
        print("You decide to leave the area and return to the village.")
        explore_village(player)
    player.explored_areas.append("tavern") # Add tavern to explored areas    
    print("\nYou enter the bustling tavern and strike up conversations with the locals.")
    while True:
        print("What would you like to do?")
        print("\n1. Listen to the rumors and gossip.")
        print("2. Look around for any useful items.")
        print("3. Leave the tavern and explore the village further.")
        if player.stats[player.get_advantage()] > 5:
            print("4. [DEX] Attempt to steal from the patrons.")
            
        choice = input("Enter the number of your choice: ")
        if choice == "1":
            print("------------------------------------------")
            print(f"\nThe townsfolk are distressed and tell you about the catacombs beneath the village.")
            print("\nThey warn you of the dangers lurking below and the secrets that lie within.")
            print("\nYou can't help but feel drawn to the catacombs...This could finally satisfy your ego.")
            print("------------------------------------------")
        elif choice == "2":
            print("\nYou search the tavern and find a few useful items.")
            if player.player_class in ["Wizard", "Warrior", "Performer", "Fool"] and not player.has_item("torch"):
                print("You find a torch left behind by a weary traveler and add it to your inventory.")
                player.add_to_inventory("torch")
        elif choice == "3":
            print("\nYou exit the tavern.")
            explore_village(player)
        elif choice == "4" and player.stats[player.get_advantage()] > 5:
                print("\nYou scout around looking for pockets to pick.")
                print("You manage to steal a few coins and a shiny object.")
                player.add_to_inventory("shiny object")
                print("There is a drunken man slouched over the bar. He has a rusty key on a chain.")
                print("This could be risky, what do you do?")
                print("\n1. [DEX] Attempt to steal the key.")
                print("\n2. [DEX] Attempt to cause a distraction and take the key.")
                choice = input("Enter the number of your choice: ")
                if choice == "1":
                    print("\nYou attempt to snatch the key")
                    print("\nYou fail miserably")
                    print("\nYou are donked on the head. That is the end of your adventure.")
                    return
                elif choice == "2":
                    print("\nYou deftly cause a distraction by tripping a nearby patron.")
                    print("\nYou grab the key and pocket it.")
                    player.add_to_inventory("rusty key")
                else:
                    print("\nYou decide to leave the tavern and explore the village further.")
                    explore_village(player)
                    
        else:
            print("\nYou decide to leave the tavern and explore the village further.")
            explore_village(player)
            
            
    
    
    
                               
                                           
def explore_forest(player):
    print("\nYou venture into the dark and ominous forest. Very dark.")
    print("You hear strange noises and feel like you are being watched.")
    print("You stumble upon a hidden clearing with a mysterious altar in the center.")
    
    # Check if player is the Fool and does not have a torch
    if player.player_class == "Fool" and not player.has_item("torch"):
        print("You discover hidden pathways and stumble upon a torch.")
        player.add_to_inventory("torch")
    choice = input("\nDo you want to investigate the altar? (yes/no): ").lower()
    
    # Check if player has already explored the forest
    if player.explored_areas.count("forest") > 0:
        print("\nYou have already explored the forest and found the altar.")
        print("You decide to leave the area and return to the village.")
        explore_village(player)
        
    # Check if player wants to investigate the altar
    if choice == "yes":
        player.explored_areas.append("forest") # Add forest to explored areas
        print("\nYou approach the altar and see strange symbols carved into the stone.")
        print("You feel a strange energy emanating from the altar.")
        
        # Check player class to determine outcome
        if player.player_class == "Wizard":
            print("You recognize the symbols as ancient runes and decipher their meaning.")
            print("You gain a deeper understanding of the magic that permeates the forest.")
            print("You feel a surge of power and your magical abilities are enhanced.")
            player.change_stat("intelligence", 2)
        elif player.player_class == "Warrior":
            print("You sense a dark presence surrounding the altar and prepare for battle.")
            print("You feel a surge of adrenaline and power, you hit the altar with your sword.")
            print("You feel silly, obviously that was not the right thing to do.")
        elif player.player_class == "Performer":
            print("You feel inspired by the mysterious aura of the altar and decide to put on a show.")
            print("You perform a captivating dance that enchants the creatures of the forest.")
            print("On second thought, you realize that was not the best idea.")
            print("You retreat in a hurry, hoping to avoid any unwanted attention.")
        else:
            print("You feel a sense of mischief and decide to play a prank on the altar.")
            print("You make funny faces and rude gestures, hoping to provoke a reaction.")
            print("You hear a low rumbling sound and the ground begins to shake.")
            print("The altar must be super impressed, you become infinitely more powerful.")
            player.change_stat("intelligence", 2)
            player.change_stat("strength", 2)
            player.change_stat("dexterity", 2)
            player.change_stat("luck", 2)
            print("You also find a shiny object on the ground and add it to your inventory. Winning!")
            player.add_to_inventory("shiny object")
            print("You feel a sense of unease and decide to leave the area.")
        
        print("You feel a sense of unease and decide to leave the area.")
        
        explore_village(player)
        
    # If player decides not to investigate the altar    
    else:
        print("\nYou have decided to ignore the only interesting thing in the forest.")
        print("\nLet's hope you find something more interesting in the village.")
        explore_village(player)
        

        
def main():
    print("Welcome to the Choose Your Own Adventure game!")
    name = input("Enter your character's name: ")
    player_class = choose_class()
    player = Player(name, player_class)

    print(f"\nWelcome, {player.name}, the {player.player_class}!\n")

    print("You are on a journey and decide to take shelter in a nearby village.")
    print("The village is strange and makes you uneasy.")

    explore_village(player)
    
    choice = input("\nDo you want to explore the catacombs? (yes/no): ").lower()
    if choice == "yes":
        print("\nYou decide to enter the catacombs...")
        explore_catacombs(player)
    else:
        print("\nYou resist the pull to the catacombs and continue exploring the village.")

if __name__ == "__main__":
    main()
