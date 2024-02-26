from openai import OpenAI
import const as const
from game_base import GameBase


class HangMan(GameBase):
    def __init__(self):
        self.client = OpenAI(api_key=const.OPEN_API_KEY)

    def prompt_word_and_description(self):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": "Give a word between 3 and 6 letters long, "
                               "with a hint about what the word is, separate the word and hint with a semicolon"
                }
            ]
        )
        return completion.choices[0].message.content

    def start_game(self):
        word_and_hint = self.prompt_word_and_description()
        word, hint = word_and_hint.split(';')
        word = word.lower()
        masked_word: str = '_' * len(word)
        print(f"Your word is {len(word)} letters long, here's a hint to your word: {hint}")
        attempts = 6
        current_attempt = 1
        while attempts > current_attempt and '_' in masked_word:
            print('Guess a letter')
            guess = input().lower()
            if guess in word:
                print('Correct !!')
                for index, letter in enumerate(word):
                    if letter == guess:
                        masked_word = masked_word[0: index] + letter + masked_word[index + 1:]
            else:
                print(f'Sorry try again, you have {current_attempt} of {attempts}')
            current_attempt += 1
            print(masked_word)
            if current_attempt == attempts and '_' in masked_word:
                print(f'Oops, hanged to DEATH !!!')

        print(('Better luck next time !' if '_' in masked_word else 'Congrats ! You solved the puzzle')
              + f' the word was {word}')
