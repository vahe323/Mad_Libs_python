import random

def mad_libs():
    print("--- Welcome to Mad Libs ---")
    print("Choose a template number:")
    print("1. Hospital Visit")
    print("2. Camping Trip")
    print("3. Enchanted Castle")
    
    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        # Inputs for Template 1
        num1 = input("Type a number: ")
        time_measure = input("Type a measure of time: ")
        transport = input("Type a mode of transportation: ")
        adj1 = input("Type an adjective: ")
        adj2 = input("Type another adjective: ")
        noun1 = input("Type a noun: ")
        color1 = input("Type a color: ")
        body_part1 = input("Type a part of the body: ")
        verb1 = input("Type a verb: ")
        num2 = input("Type another number: ")
        noun2 = input("Type another noun: ")
        noun3 = input("Type a third noun: ")
        body_part2 = input("Type another part of the body: ")
        verb2 = input("Type another verb: ")
        noun4 = input("Type a fourth noun: ")
        adj3 = input("Type a third adjective: ")
        silly = input("Type a silly word: ")

        print("\n--- Your Story ---")
        print(f"It was about {num1} {time_measure} ago when I arrived at the hospital in a {transport}. "
              f"The hospital is a/an {adj1} place, there are a lot of {adj2} {noun1} here. "
              f"There are nurses here who have {color1} {body_part1}. If someone wants to come into my room "
              f"I told them that they have to {verb1} first. I’ve decorated my room with {num2} {noun2}. "
              f"Today I talked to a doctor and they were wearing a {noun3} on their {body_part2}. "
              f"I heard that all doctors {verb2} {noun4} every day for breakfast. "
              f"The most {adj3} thing about being in the hospital is the {silly} {noun1}!")

    elif choice == "2":
        # Inputs for Template 2
        name = input("Type a person's name: ")
        noun1 = input("Type a noun: ")
        feel1 = input("Type an adjective (feeling): ")
        verb1 = input("Type a verb: ")
        feel2 = input("Type another adjective (feeling): ")
        animal1 = input("Type an animal: ")
        verb2 = input("Type another verb: ")
        color1 = input("Type a color: ")
        verb_ing = input("Type a verb ending in 'ing': ")
        adverb = input("Type an adverb ending in 'ly': ")
        num1 = input("Type a number: ")
        time_measure = input("Type a measure of time: ")
        color2 = input("Type another color: ")
        animal2 = input("Type another animal: ")
        num2 = input("Type another number: ")
        silly = input("Type a silly word: ")
        noun2 = input("Type another noun: ")

        print("\n--- Your Story ---")
        print(f"This weekend I am going camping with {name}. I packed my lantern, sleeping bag, and {noun1}. "
              f"I am so {feel1} to {verb1} in a tent. I am {feel2} we might see a(n) {animal1}, I hear they’re kind of dangerous. "
              f"While we’re camping, we are going to hike, fish, and {verb2}. I have heard that the {color1} lake is great "
              f"for {verb_ing}. Then we will {adverb} hike through the forest for {num1} {time_measure}. "
              f"If I see a {color2} {animal2} while hiking, I am going to bring it home as a pet! "
              f"At night we will tell {num2} {silly} stories and roast {noun2} around the campfire!!")

    elif choice == "3":
        # Inputs for Template 3
        name = input("Type a person's name: ")
        adj1 = input("Type an adjective: ")
        color1 = input("Type a color: ")
        animal1 = input("Type an animal: ")
        place = input("Type a place: ")
        adj2 = input("Type another adjective: ")
        magical1 = input("Type a magical creature (plural): ")
        adj3 = input("Type a third adjective: ")
        magical2 = input("Type another magical creature (plural): ")
        room = input("Type a room in a house: ")
        noun1 = input("Type a noun: ")
        noun2 = input("Type another noun: ")
        noun_pl1 = input("Type a plural noun: ")
        adj4 = input("Type a fourth adjective: ")
        noun_pl2 = input("Type another plural noun: ")
        num = input("Type a number: ")
        time_measure = input("Type a measure of time: ")
        verb_ing = input("Type a verb ending in 'ing': ")
        adj5 = input("Type a fifth adjective: ")
        noun3 = input("Type a third noun: ")

        print("\n--- Your Story ---")
        print(f"Dear {name}, I am writing to you from a {adj1} castle in an enchanted forest. "
              f"I found myself here one day after going for a ride on a {color1} {animal1} in {place}. "
              f"There are {adj2} {magical1} and {adj3} {magical2} here! In the {room} there is a pool full of {noun1}. "
              f"I fall asleep each night on a {noun2} of {noun_pl1} and dream of {adj4} {noun_pl2}. "
              f"It feels as though I have lived here for {num} {time_measure}. I hope one day you can visit, "
              f"although the only way to get here now is {verb_ing} on a {adj5} {noun3}!!")
    
    else:
        print("Invalid selection. Please run the program again.")

# Run the program
mad_libs()