import random
import ascii_art
import hangman_word_list as wl


lives = 6
end_of_game = False
chosen_word = random.choice(wl.word_list)
word_length = len(chosen_word)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
  
    guess = input("Guess a letter: ").lower()
    print(ascii_art.stages[lives])
  
    if guess in chosen_word:
    #Check guessed letter
      for position in range(word_length):
          letter = chosen_word[position]
          if letter == guess:
              display[position] = letter
    else:
      lives = lives - 1
      print(ascii_art.stages[lives])

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win.")
    elif lives == 0:
      end_of_game = True
      print("You lose.")