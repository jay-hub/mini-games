import pyttsx3
from openai import OpenAI
import const as const

from game_base import GameBase


class StoryTeller(GameBase):
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 90)
        self.client = OpenAI(api_key=const.OPEN_API_KEY)

    def generate_story(self, topic):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": f"Generate a kids friendly short story that relates to {topic}"
                }
            ]
        )
        return completion.choices[0].message.content

    def start_game(self):
        self.engine.say('Let me tell you a story')
        read_input = input('I will tell you a story about a topic of your choice, so tell me what you want to hear? ')
        story = self.generate_story(read_input)
        print(f'story is {story}')
        self.engine.say(story)
        self.engine.runAndWait()
