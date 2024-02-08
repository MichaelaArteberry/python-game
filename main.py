# Print a welcome message

print("Welcome to the Haunted Mansion!")
print("You are a distant relative to a rich family member that passed away and left you his estate.")
print("As the new owner, you decided to go pay a visit to your new mansion.")
print("The house is dated, creaky, and falling apart. You start at the front door, and walk inside.")
print("Do you want to enter the living room, or the dining room?")

# Prompt user for choice

roomChoice = input("> ")

if(roomChoice == "living room"):
    print("You  entered the living room.")
    print("As you walk in in, you notice a sleeping dog guarding some jewelry.")
    print("Do you want to steal the jewelry from the dog?")

    stealChoice = input("> ")

    if(stealChoice == "yes"):
        print("You attempt to steal the jewelry from the dog, but he wakes up and rips you to shreds.")
        print("YOU ARE DEAD.")

    elif(stealChoice == "no"):
        print("You decided not to steal.")
        print("You turn around and leave the house safely.")

    else:
        print("Invalid. Please enter yes or no.")

elif(roomChoice == "dining room"):
    print("You  entered the dining room.")
    print("As you walk in you notice a creepy portrait on the wall.")
    print("Do you want to go look at the portrait more closely?")

    portraitChoice = input("> ")

    if(portraitChoice == "yes"):
        print("You walk up to the portrait to get a better look.")
        print("Looking at it, the portraits face distorts into a creepy smiling face and freaks you out.")
        print("Do you scream, or do you run?")

        lastChoice = input("> ")

        if(lastChoice == "scream"):
            print("YOU ARE DEAD.")
        elif(lastChoice == "run"):
            print("You made it out of the mansion, and you decide to sell it, its too creepy for you.")
            print("You Survived!")
        else:
            print("Invalid. Please enter scream or run.")

else:
    print("Invalid. Please enter living room or dining room.")
