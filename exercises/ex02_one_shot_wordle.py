"""A step above Chardle- an actual game of wordle!"""
__author__ = "730477270"

secret_word: str = "python"
length: int = len(secret_word)
guess: str = input(f"What is your { length }-letter guess? ")
counter: int = 0
while len(guess) != length and counter < length:
    guess = input(f"That was not { length } letters! Try again: ")
    counter = counter + 1

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

index_counter: int = 0
result_emoji: str = ""
while index_counter < len(secret_word):
    if secret_word[index_counter] == guess[index_counter]:
        result_emoji = result_emoji + GREEN_BOX
    else:
        yellow_indicator: bool = False
        alternate_indices: int = 0
        while yellow_indicator is False and alternate_indices < len(secret_word):
            if secret_word[alternate_indices] == guess[index_counter]:
                yellow_indicator = True
            else:
                alternate_indices = alternate_indices + 1
        if yellow_indicator is True:
            result_emoji = result_emoji + YELLOW_BOX
        else:
            result_emoji = result_emoji + WHITE_BOX
    index_counter = index_counter + 1
print(result_emoji)

if len(guess) == length and guess != secret_word:
    print("Not quite. Play again soon! ")
if guess == secret_word:
    print("Woo! You got it! ")
