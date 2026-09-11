import random

def get_word(prompt):
    return input(prompt + ": ")

def hospital_story():
    number = get_word("Type a Number")
    time_measure = get_word("Type a Measure of Time")
    transport = get_word("Type a Mode of Transportation")
    adjective = get_word("Type an Adjective")
    adjective2 = get_word("Type an Adjective")
    noun = get_word("Type a Noun")
    color = get_word("Type a Color")
    body_part = get_word("Type a Part of the Body")
    verb = get_word("Type a Verb")
    number2 = get_word("Type a Number")
    noun2 = get_word("Type a Noun")
    noun3 = get_word("Type a Noun")
    body_part2 = get_word("Type a Part of the Body")
    verb2 = get_word("Type a Verb")
    noun4 = get_word("Type a Noun")
    adjective3 = get_word("Type an Adjective")
    silly_word = get_word("Type a Silly Word")

    story = (
        f"It was about {number} {time_measure} ago when I arrived at the hospital in a {transport}. "
        f"The hospital is a/an {adjective} place, there are a lot of {adjective2} {noun} here. "
        f"There are nurses here who have {color} {body_part}. "
        f"If someone wants to come into my room I told them that they have to {verb} first. "
        f"I've decorated my room with {number2} {noun2}. "
        f"Today I talked to a doctor and they were wearing a {noun3} on their {body_part2}. "
        f"I heard that all doctors {verb2} {noun4} every day for breakfast. "
        f"The most {adjective3} thing about being in the hospital is the {silly_word} {noun}!"
    )
    return story

def camping_story():
    person = get_word("Type a Proper Noun (Person's Name)")
    noun = get_word("Type a Noun")
    feeling = get_word("Type an Adjective (Feeling)")
    verb = get_word("Type a Verb")
    feeling2 = get_word("Type an Adjective (Feeling)")
    animal = get_word("Type an Animal")
    verb2 = get_word("Type a Verb")
    color = get_word("Type a Color")
    verbing = get_word("Type a Verb ending in ing")
    number = get_word("Type a Number")
    time_measure = get_word("Type a Measure of Time")
    adverb = get_word("Type an Adverb ending in ly")
    color2 = get_word("Type a Color")
    animal2 = get_word("Type an Animal")
    number2 = get_word("Type a Number")
    silly_word = get_word("Type a Silly Word")
    noun2 = get_word("Type a Noun")

    story = (
        f"This weekend I am going camping with {person}. "
        f"I packed my lantern, sleeping bag, and {noun}. "
        f"I am so {feeling} to {verb} in a tent. "
        f"I am {feeling2} we might see a(n) {animal}, I hear they're kind of dangerous. "
        f"While we're camping, we are going to hike, fish, and {verb2}. "
        f"I have heard that the {color} lake is great for {verbing}. "
        f"Then we will {adverb} hike through the forest for {number} {time_measure}. "
        f"If I see a {color2} {animal2} while hiking, I am going to bring it home as a pet! "
        f"At night we will tell {number2} {silly_word} stories and roast {noun2} around the campfire!!"
    )
    return story

def castle_story():
    person = get_word("Type a Proper Noun (Person's Name)")
    adjective = get_word("Type an Adjective")
    color = get_word("Type a Color")
    animal = get_word("Type an Animal")
    place = get_word("Type a Place")
    adjective2 = get_word("Type an Adjective")
    creature = get_word("Type a Magical Creature (Plural)")
    adjective3 = get_word("Type an Adjective")
    creature2 = get_word("Type a Magical Creature (Plural)")
    room = get_word("Type a Room in a House")
    noun = get_word("Type a Noun")
    noun2 = get_word("Type a Noun")
    noun_plural3 = get_word("Type a Noun (Plural)")
    adjective4 = get_word("Type an Adjective")
    noun_plural4 = get_word("Type a Noun (Plural)")
    number = get_word("Type a Number")
    time_measure = get_word("Type a Measure of Time")
    verbing = get_word("Type a Verb ending in ing")
    adjective5 = get_word("Type an Adjective")
    noun5 = get_word("Type a Noun")

    story = (
        f"Dear {person}, I am writing to you from a {adjective} castle in an enchanted forest. "
        f"I found myself here one day after going for a ride on a {color} {animal} in {place}. "
        f"There are {adjective2} {creature} and {adjective3} {creature2} here! "
        f"In the {room} there is a pool full of {noun}. "
        f"I fall asleep each night on a {noun2} of {noun_plural3} and dream of {adjective4} {noun_plural4}. "
        f"It feels as though I have lived here for {number} {time_measure}. "
        f"I hope one day you can visit, although the only way to get here now is {verbing} on a {adjective5} {noun5}."
    )
    return story

def main():
    print("Choose a story template:")
    print("1. Hospital")
    print("2. Camping")
    print("3. Castle")
    choice = input("Type 1, 2, or 3: ")

    if choice == "1":
        story = hospital_story()
    elif choice == "2":
        story = camping_story()
    elif choice == "3":
        story = castle_story()
    else:
        choice = random.choice(["1", "2", "3"])
        print("Invalid choice, picking a random template for you...")
        if choice == "1":
            story = hospital_story()
        elif choice == "2":
            story = camping_story()
        else:
            story = castle_story()

    print("\nHere is your story:\n")
    print(story)

main()
