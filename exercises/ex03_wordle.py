"""Structured Wordle- getting even closer to the real thing!"""

___author___ = 730477270

def contains_char(secret_word: str, char: chr) -> bool:
    """Function that scans the secret word for the presence of the guessed character. """
    assert len(char) == 1
    index_counter: int = 0
    char_indicator: bool = False
    alternate_indices: int = 0
    while char_indicator is False and alternate_indices < len(secret_word):
        if secret_word[alternate_indices] == char[index_counter]:
            char_indicator = True
        else:
            alternate_indices = alternate_indices + 1
    if char_indicator is True:
        return True
    else:
        return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess_word: str, secret_word: str) -> str:
    """Returns emoji chain based on the result of contains_char."""
    assert len(guess_word) == len(secret_word)
    result_emoji: str = ""
    index_counter2: int = 0
    while index_counter2 < len(secret_word):
        if secret_word[index_counter2] == guess_word[index_counter2]:
            # if the character at that index equals that same index in the guess word
            result_emoji = result_emoji + GREEN_BOX
        else:
            if contains_char(secret_word, guess_word[index_counter2]) is True:
                result_emoji = result_emoji + YELLOW_BOX
            else: 
                result_emoji = result_emoji + WHITE_BOX
        index_counter2 = index_counter2 + 1
    return result_emoji


def input_guess(expected_length: int) -> str:
    """Obtains guess of user (which is "expected length" long). If not expected length, prompts user for another guess. If expected length, returns guess of correct length."""
    guess: str = input(f"Enter a { expected_length } character word: ")
    counter: int = 0
    while len(guess) != expected_length and counter < expected_length:
        guess = input(f"That wasn't { expected_length } chars! Try again: ")
        counter = counter + 1
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    # This function combines all the previous ones and actually runs the game
    secret_word: str = "codes"
    length: int = len(secret_word)
    turn: int = 1
    won: bool = False
    while turn <= 6 and not won:
        # while the user still has turns left and they have not yet won
        print(f"=== Turn { turn }/6 ===")
        guess = (input_guess(length))
        print(emojified(guess, secret_word) ) 
        if guess == secret_word:
            won = True
            print(f"You won in { turn}/6 turns!" )
        if turn == 6 and secret_word != guess:
            print("X/6 - Sorry, try again tomorrow!" )
        turn = turn + 1


if __name__ == "__main__":
    main()

    
