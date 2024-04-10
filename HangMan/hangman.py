import random
from hangman_words import word_list
from HangMan.hangman_art import logo, stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(logo)

display = ["_" for _ in range(word_length)]

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    is_guess_correct = False

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            is_guess_correct = True

    if not is_guess_correct:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was: {''.join(chosen_word)}")
            break

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
        break

    print(stages[lives])
