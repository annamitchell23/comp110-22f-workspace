"""EX01- Chardle- A cute step toward Wordle."""

_author_ = "730477270"

chosen_word: str = input("Enter a 5-chatacter word: ")
if len(chosen_word)!= 5:
    print("Error: Word must contain 5 characters")
    exit()
else:
    chosen_character: str = input("Enter a single character: ")
    if len(chosen_character)!= 1:
        print("Error: Character must be a single character")
        quit()
    else: print("Searching for " + chosen_character + " in " + chosen_word)
instance_counter: str = 0
if chosen_character == chosen_word[0]:
    print(chosen_character + " found at index 0 ")
    instance_counter += 1
else:
    pass
if chosen_character == chosen_word[1]:
    print(chosen_character + " found at index 1 ")
    instance_counter += 1
else:
    pass
if chosen_character == chosen_word[2]:
    print(chosen_character + " found at index 2 ")
    instance_counter += 1
else:
    pass
if chosen_character == chosen_word[3]:
    print(chosen_character + " found at index 3 ")
    instance_counter += 1
else:
    pass
if chosen_character == chosen_word[4]:
     print(chosen_character + " found at index 4 ")
     instance_counter += 1
else:
    pass


if instance_counter == 0:
    print("No instances of " + chosen_character + " found in " + chosen_word)
elif instance_counter == 1:
    print("1 instance of " + chosen_character + " found in " + chosen_word)
elif instance_counter == 2:
    print("2 instances of " + chosen_character + " found in " + chosen_word)
elif instance_counter == 3:
    print("3 instances of " + chosen_character + " found in " + chosen_word)
elif instance_counter == 4:
    print("4 instances of " + chosen_character + " found in " + chosen_word)
else:
    print("5 instances of " + chosen_character + " found in " + chosen_word)