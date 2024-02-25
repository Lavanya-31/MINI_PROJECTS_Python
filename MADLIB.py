def madlib():
    # Get input from the user
    adjective = input("Adjective: ").strip()
    animal = input("Animal: ").strip()
    verb_past_tense = input("Verb (past tense): ").strip()
    place = input("Place: ").strip()
    food = input("Food: ").strip()
    emotion = input("Emotion: ").strip()
    number = input("Number: ").strip()
    adjective2 = input("Another Adjective: ").strip()

    # Input validation
    if any(not word for word in [adjective, animal, verb_past_tense, place, food, emotion, number, adjective2]):
        print("Please provide input for all prompts.")
        return

    # Create the madlib story
    madlib = f"One {adjective} day, a curious {animal} decided to {verb_past_tense} to the {place}. " \
             f"It brought along a basket filled with {food} to share. As it reached the {place}, " \
             f"it noticed a group of {number} {adjective2} {animal}s having a party. " \
             f"The atmosphere was filled with {emotion}, and everyone enjoyed the tasty {food} together."

    print(madlib)

# Call the function
madlib()
