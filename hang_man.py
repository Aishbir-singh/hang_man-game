import random

class Hangman:
    def __init__(self, word_list):
        self.word_list = word_list
        self.secret_word = self.choose_word()
        self.guesses_left = 6
        self.guessed_letters = set()

    def choose_word(self):
        return random.choice(self.word_list).upper()

    def display_word(self):
        display = ''
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                display += letter + ' '
            else:
                display += '_ '
        return display.strip()

    def make_guess(self, guess):
        guess = guess.upper()
        if guess.isalpha() and len(guess) == 1:
            if guess in self.guessed_letters:
                return "You already guessed that letter!"
            elif guess in self.secret_word:
                self.guessed_letters.add(guess)
                if self.check_win():
                    return "Congratulations! You guessed the word: {}".format(self.secret_word)
                return "Good guess! Current word: {}".format(self.display_word())
            else:
                self.guessed_letters.add(guess)
                self.guesses_left -= 1
                if self.guesses_left == 0:
                    return "Game over! The word was: {}".format(self.secret_word)
                return "Incorrect guess. Guesses left: {}. Current word: {}".format(self.guesses_left, self.display_word())
        else:
            return "Invalid guess. Please enter a single letter."

    def check_win(self):
        return set(self.secret_word).issubset(self.guessed_letters)

# Example usage
if __name__ == "__main__":
    word_list = ["python", "hangman", "programming", "challenge", "game"]
    hangman_game = Hangman(word_list)

    print("Welcome to Hangman!")
    print("Current word:", hangman_game.display_word())

    while not hangman_game.check_win() and hangman_game.guesses_left > 0:
        user_guess = input("Enter your guess: ")
        result = hangman_game.make_guess(user_guess)
        print(result)

    if hangman_game.check_win():
        print("Congratulations! You won!")
    else:
        print("Sorry, you lost. The correct word was: {}".format(hangman_game.secret_word))
