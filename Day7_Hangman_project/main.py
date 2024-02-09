import random
import hangman_words
import hangman_art

stages = hangman_art.stages

end_of_game = False
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

print(hangman_art.logo)

#Create blanks "_"
display = []
for _ in range(word_length):
    display+="_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life!")
        lives-=1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    print(f"{''.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You won!")

    print(stages[lives])