import random

class Character:
    def __init__(self):
        self.inventory = []
        self.explored = []
        self.memory = []

class Game:
    def __init__(self):
        self.character = Character()

    def start(self):
        print("You awaken mysteriously, unsure of where you are.")
        
        # Random chance to find the photograph upon waking
        if random.random() < 0.5:
            print("You notice an old photograph nearby. It looks like a family photograph, there is a man and a woman embracing a dog. You can't remember who they are.")
            self.character.inventory.append("photograph")
            self.character.memory.append("photograph")
        else:
            print("Your head is foggy.")
        
        choice = input("What will you do? 1) Look around 2) Start panicking: ")
        
        if choice == "1":
            self.explore()
        elif choice == "2":
            self.panic()
        else:
            print("Invalid choice. Please try again.")
            self.start()

    def explore(self):
        event = random.choice(["dusty", "crowbar"])
        if event == "dusty":
            print("You walk around the room. It is a large entrance hall with not a lot of furniture. The room is dusty and the air is stale.")
            self.memory_event()
        elif event == "crowbar":
            print("You find a crowbar. This could be useful.")
            self.character.inventory.append("crowbar")
            self.explore_house()

    def memory_event(self):
        if "photograph" in self.character.inventory:
            print("You have a sudden flashback of a dog bouncing through the entrance hall out of the door. You see a flash of light and then nothing.")
            self.character.memory.append("dog")
        else:
            print("Everything is so familiar, your head hurts.")

        self.explore_house()

    def panic(self):
        event = random.choice(["die", "remember"])
        if event == "die":
            print("You succumb to anxiety and die. Game over.")
            return
        elif event == "remember":
            print("You frantically try to remember something.")
            if "photograph" in self.character.inventory:
                print("You remember the man in the photograph. He was your father. You remember him playing with the dog in the photograph. You remember the dog's name was Max.")
                self.character.memory.append("father")
            else:
                print("You struggle to remember anything concrete.")
        
        self.explore_house()

    def explore_house(self):
        if len(self.character.explored) == 4:
            print("You have explored the entire house.")
            print("You feel a sense of dread and confusion.")
            print("You can't shake the feeling that something is missing.")
            self.explore_outside()
            
        else:
            print("You start exploring the house further.")
            print("You can explore: 1) Downstairs 2) Upstairs")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.explore_downstairs()
            elif choice == "2":
                self.explore_upstairs()
            else:
                print("Invalid choice. Please try again.")
                self.explore_house()

    def explore_downstairs(self):
        print("You decide to explore the first floor.")
        print("Looking around, you see a living room and a study.")
        print("nYou can explore: 1) Living room 2) Study 3) Go back")

        choice = input("Enter your choice: ")
        if choice == "1":
            self.explore_living_room()
        elif choice == "2":
            self.explore_study()
        elif choice == "3":
            self.explore_house()
        else:
            print("Invalid choice. Please try again.")
            self.explore_downstairs()

    def explore_living_room(self):
        if "living room" in self.character.explored:
            print("You have already explored the living room.")
            self.explore_house()
            return
        self.character.explored.append("living room")
        print(f"{self.character.explored}")
        print("You enter the living room. It is dimly lit and the furniture is covered in dust.")
        print("The room is eerily quiet, except for the sound of the wind outside.")
        print("You take a look around. All you can see is a dusty old sofa, a television and a fireplace.")
        print("There are imprints on the sofa where someone has been sitting, disturbing the dust.")
        print("On the mantlepiece, you see an old video tape.")

        choice = input("What will you do? 1) Examine the video tape 2) Go back: ")

        if choice == "1":
            self.examine_video_tape()
        elif choice == "2":
            self.explore_house()    
        else:
            print("Invalid choice. Please try again.")
            self.explore_living_room()

    def examine_video_tape(self):
        print("You pick up the old video tape and examine it.")
        print("Do you want to try the video tape on the TV? (Y/N)")
        choice = input().strip().lower()

        if choice == "y":
            if random.random() < 0.5:  # Random chance of tape working
                print("You insert the video tape into the VCR.")
                print("The tape starts playing. It's a home video of a family playing in the garden. You remember being in the garden, searching for something.")
                self.character.memory.append("video tape")
            else:
                print("You insert the video tape into the VCR, but it doesn't seem to work. Obviously, the tape is too old.")
        elif choice == "n":
            print("You decide not to try the video tape for now.")
        else:
            print("Invalid choice.")

        self.explore_house()

    def explore_study(self):
        if "study" in self.character.explored:
            print("You have already explored the study.")
            self.explore_house()
            return
        self.character.explored.append("study")
        print(f"{self.character.explored}")

        print("You enter the study.")
        event = random.choice(["trip", "computer"])
        if event == "trip":
            print("You trip over an old rug and fall to the ground.")
            print("You notice a piece of paper sticking out from under the rug.")
            print("You pick up the paper and see that it has a password written on it.")
            print("The password is: 'MAX'")
            print("Would you like to try the password on the computer? (Y/N)")
            choice = input().strip().lower()
            
            if choice == "y":
                print("You walk over to the computer and enter the password 'MAX'.")
                print("The computer unlocks and you see a folder named 'Top secret'.")
                print("You open the folder and find a document with information about a secret project.")
                print("It is heavily redacted, but you can make out some details about reported sightings and missing people.")
                self.character.inventory.append("files")
            elif choice == "n":
                print("You decide not to try the password for now.")
            else:
                print("Invalid choice.")
        elif event == "computer":
            print("You see a computer on the desk.")
            print("Would you like to try to access the computer? (Y/N)")
            choice = input().strip().lower()
            
            if choice == "y":
                print("You try to access the computer, but it is password protected.")
            elif choice == "n":
                print("You decide not to try the computer for now.")
            else:
                print("Invalid choice.")
                
            
        self.explore_house()

    def explore_upstairs(self):
        print("You head upstairs.")
        print("You can explore: 1) Bedroom 2) Attic room 3) Go back")

        choice = input("Enter your choice: ")
        if choice == "1":
            self.explore_bedroom()
        elif choice == "2":
            self.explore_attic_room()
        elif choice == "3":
            self.explore_house()
        else:
            print("Invalid choice. Please try again.")
            self.explore_upstairs()


    def explore_bedroom(self):
        if "bedroom" in self.character.explored:
            print("You've already explored the bedroom.")
            self.explore_house()
            return

        if "crowbar" in self.character.inventory:
            print("You use the crowbar to pry open the bedroom door.")
        else:
            if random.random() < 0.5:  # Random chance of being able to kick the door in
                print("You kick the bedroom door with all your strength and it swings open.")
            else:
                print("The bedroom door seems to be stuck. You need something to pry it open.")
                self.explore_house()
                return
        self.character.explored.append("bedroom")
        print(f"{self.character.explored}")

        print("Inside, you find a room full of crime scene tape.")
        if "files" in self.character.inventory:
            print("Seeing the crime scene tape jogs a memory...")
            print("You remember a man and a woman in the bedroom, laughing with open arms as you run to greet them on a sunny morning.")
            # Optionally, add more story/gameplay for finding the ID badge
        else:
            print("You look around the room but find nothing of significance.")
        choice = input("Would you like to explore the room further? (Y/N)").strip().lower()
        if choice == "y":
            self.explore_bedroom_further()
        elif choice == "n":
            self.explore_house()
        else:
            print("Invalid choice.")
            self.explore_bedroom()

        self.character.inventory.append("bedroom")

    def explore_bedroom_further(self):
        print("You explore the bedroom further.")
        # Add more story/gameplay for further exploration
        # Optionally, reveal the memory of finding the ID badge
        print("You find a government ID badge with a woman's photo on it.")
        print("As you look at the badge, a memory flashes in your mind...")
        print("You remember the woman in the photo as your mother.")
        self.character.memory.append("mother")
        self.explore_house()


    def explore_attic_room(self):
        if "attic room" in self.character.explored:
            print("You have already explored the attic room.")
            self.explore_house()
            return

        self.character.explored.append("attic room")
        print("You enter the attic room.")
        print(f"{self.character.explored}")


        event = random.randint(1, 3)
        if event == 1:
            print("Suddenly, a cat jumps out from behind a stack of boxes, scaring you!")
            choice = input("Do you want to explore the attic further? (Y/N): ").strip().lower()
            if choice == "y":
                self.explore_attic_further()
            elif choice == "n":
                self.explore_house()
            else:
                print("Invalid choice. Please try again.")
                self.explore_attic_room()
        elif event == 2:
            print("You suddenly gain a vivid memory of waking up on a surgery table, surrounded by shadows, in great pain.")
            print("You quickly leave the attic.")
            self.character.memory.append("surgery memory")
            self.explore_house()
        elif event == 3:
            print("You find a dusty photo album tucked away in a corner. Inside, there are photos of a little girl on various birthdays. She has blonde hair, blue eyes, and a mole on her left cheek.")
            print("You feel a sense of nostalgia and curiosity. ")
            self.character.memory.append("photo album")
            self.explore_house()

    def explore_attic_further(self):
        print("You decide to explore the attic further.")
        # Add more story/gameplay for further exploration
        # Optionally, add more items to inventory or encounters
        print("You find old boxes filled with various items and keepsakes.")
        print("You find a dusty photo album tucked away in a corner. Inside, there are photos of a little girl on various birthdays. She has blonde hair, blue eyes, and a mole on her left cheek.")
        print("You feel a sense of nostalgia and curiosity. ")
        self.character.memory.append("photo album")
        self.explore_house()
    
    def explore_outside(self):
        print("You head back to the entrance hall.")
        all_memories = {"dog", "father", "video tape", "mother", "surgery memory", "photo album"}
        if set(self.character.memory) == all_memories:
            self.ending_1()
        elif {"dog", "father", "video tape", "mother", "surgery memory"}.issubset(set(self.character.memory)):
            self.ending_2()
        elif {"dog", "father", "video tape", "mother"}.issubset(set(self.character.memory)):
            self.ending_3()
        elif {"dog", "father", "video tape"}.issubset(set(self.character.memory)):
            self.ending_4()
        elif {"dog", "father"}.issubset(set(self.character.memory)):
            self.ending_5()
        else:
            self.ending_6()

    def ending_1(self):
        print("You feel dizzy and disoriented.")
        print("You remember everything.")
        print("You recall the memory of Max, your dog, running out of the house.")
        print("You follow in his footsteps, opening the door and stepping outside.")
        print("**********")
        print("You are outside, the sun is shining, you are looking for Max. He just came out here?")
        print("'Where are you Max?' You call out.")
        print("You are a little girl, you remember now.")
        print("You see a blinding flash of light. There is something in the sky")
        print("You scream as loud as you can for your mother and father.")
        print("**********")
        print("You remember the day you were taken.")
        print("You begin to cry. How long have you been gone?")
        print("You are home now.")
        print("The end.")

    def ending_2(self):
        pass

    def ending_3(self):
        pass

    def ending_4(self):
        pass

    def ending_5(self):
        pass

    def ending_6(self):
        pass


if __name__ == "__main__":
    game = Game()
    game.start()
