import random
import re

# What to ask the player for each type of word
PROMPTS = {
    "number": "a Number",
    "time": "a Measure of Time",
    "transport": "a Mode of Transportation",
    "adjective": "an Adjective",
    "noun": "a Noun",
    "plural": "a Noun (Plural)",
    "color": "a Color",
    "bodypart": "a Part of the Body",
    "verb": "a Verb",
    "verbing": "a Verb ending in -ing",
    "adverb": "an Adverb ending in -ly",
    "silly": "a Silly Word",
    "name": "a Person's Name",
    "feeling": "an Adjective (Feeling)",
    "animal": "an Animal",
    "creature": "a Magical Creature (Plural)",
    "room": "a Room in a House",
    "place": "a Place",
}

# Words the computer can pick when the player wants a random word
RANDOM_WORDS = {
    "number": ["7", "42", "1000", "13", "3"],
    "time": ["minutes", "days", "centuries", "seconds", "weeks"],
    "transport": ["skateboard", "submarine", "hot air balloon", "tractor", "rocket"],
    "adjective": ["squishy", "enormous", "sparkly", "grumpy", "invisible"],
    "noun": ["banana", "trombone", "umbrella", "pickle", "robot"],
    "plural": ["socks", "pancakes", "clouds", "spoons", "dinosaurs"],
    "color": ["purple", "neon green", "orange", "turquoise", "pink"],
    "bodypart": ["elbow", "nose", "knee", "ear", "toe"],
    "verb": ["juggle", "sneeze", "dance", "whistle", "wiggle"],
    "verbing": ["skipping", "yodeling", "floating", "snoring", "rolling"],
    "adverb": ["quickly", "sleepily", "loudly", "gracefully", "clumsily"],
    "silly": ["bazinga", "flibbertigibbet", "wobble", "kerfuffle", "zoinks"],
    "name": ["Aram", "Mariam", "Gagik", "Lilit", "Narek"],
    "feeling": ["excited", "nervous", "sleepy", "thrilled", "confused"],
    "animal": ["penguin", "llama", "octopus", "hamster", "giraffe"],
    "creature": ["dragons", "unicorns", "goblins", "fairies", "trolls"],
    "room": ["kitchen", "bathroom", "attic", "garage", "basement"],
    "place": ["Paris", "the moon", "Yerevan", "the desert", "Antarctica"],
}

# Each story is a template. {adjective_1} means "first adjective".
# The part before the underscore tells us which type of word to ask for.
STORIES = {
    "Hospital": (
        "It was about {number_1} {time_1} ago when I arrived at the hospital in a {transport_1}. "
        "The hospital is a/an {adjective_1} place, there are a lot of {adjective_2} {noun_1} here. "
        "There are nurses here who have {color_1} {bodypart_1}. "
        "If someone wants to come into my room I told them that they have to {verb_1} first. "
        "I've decorated my room with {number_2} {noun_2}. "
        "Today I talked to a doctor and they were wearing a {noun_3} on their {bodypart_2}. "
        "I heard that all doctors {verb_2} {noun_4} every day for breakfast. "
        "The most {adjective_3} thing about being in the hospital is the {silly_1} {noun_1}!"
    ),
    "Camping": (
        "This weekend I am going camping with {name_1}. "
        "I packed my lantern, sleeping bag, and {noun_1}. "
        "I am so {feeling_1} to {verb_1} in a tent. "
        "I am {feeling_2} we might see a(n) {animal_1}, I hear they're kind of dangerous. "
        "While we're camping, we are going to hike, fish, and {verb_2}. "
        "I have heard that the {color_1} lake is great for {verbing_1}. "
        "Then we will {adverb_1} hike through the forest for {number_1} {time_1}. "
        "If I see a {color_2} {animal_2} while hiking, I am going to bring it home as a pet! "
        "At night we will tell {number_2} {silly_1} stories and roast {noun_2} around the campfire!!"
    ),
    "Castle": (
        "Dear {name_1}, I am writing to you from a {adjective_1} castle in an enchanted forest. "
        "I found myself here one day after going for a ride on a {color_1} {animal_1} in {place_1}. "
        "There are {adjective_2} {creature_1} and {adjective_3} {creature_2} here! "
        "In the {room_1} there is a pool full of {noun_1}. "
        "I fall asleep each night on a {noun_2} of {plural_1} and dream of {adjective_4} {plural_2}. "
        "It feels as though I have lived here for {number_1} {time_1}. "
        "I hope one day you can visit, although the only way to get here now is "
        "{verbing_1} on a {adjective_5} {noun_3}."
    ),
}


def ask_choice(question, options):
    """Keep asking until the player picks one of the valid options."""
    while True:
        answer = input(question).strip().lower()
        if answer in options:
            return answer
        print("Sorry, that's not a valid choice. Please try again.\n")


def get_word(word_type):
    """Ask for a word. The player can type 'r' to get a random one."""
    while True:
        answer = input(f"Type {PROMPTS[word_type]} (or r for a random word): ").strip()
        if answer.lower() == "r":
            word = random.choice(RANDOM_WORDS[word_type])
            print(f"  -> The computer picked: {word}")
            return word
        if answer:
            return answer
        print("  You didn't type anything, please try again.")


def choose_story():
    """Let the player pick a story, or let the computer pick one."""
    names = list(STORIES.keys())
    print("Choose a story template:")
    for number, name in enumerate(names, start=1):
        print(f"{number}. {name}")
    print(f"{len(names) + 1}. Surprise me (random story)")

    options = [str(n) for n in range(1, len(names) + 2)]
    choice = ask_choice(f"Type a number from 1 to {len(names) + 1}: ", options)

    if int(choice) == len(names) + 1:
        name = random.choice(names)
        print(f"\nThe computer picked: {name}")
    else:
        name = names[int(choice) - 1]
    return name


def build_story(template):
    """Ask for every word in the template and fill the story in."""
    # Find the blanks in order, without repeating any
    blanks = []
    for blank in re.findall(r"\{(\w+)\}", template):
        if blank not in blanks:
            blanks.append(blank)

    words = {}
    for blank in blanks:
        word_type = blank.split("_")[0]
        words[blank] = get_word(word_type)

    return template.format(**words)


def main():
    print("=== Welcome to Mad Libs! ===\n")
    while True:
        name = choose_story()
        print()
        story = build_story(STORIES[name])

        print("\nHere is your story:\n")
        print(story)

        again = ask_choice("\nPlay again? (y/n): ", ["y", "n"])
        if again == "n":
            print("Thanks for playing!")
            break
        print()


main()
