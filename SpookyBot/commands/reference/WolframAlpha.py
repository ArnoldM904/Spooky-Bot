# Python 3.6.4
import wolframalpha
from command import Command

import configparser
config = configparser.ConfigParser()
config.read('config.ini')

class WolframAlpha(Command):
    def __init__(self, client):
        super().__init__(client)
        self.name = 'answer'
        self.description = 'Answer any question Wolfram Alpha is capable of.'

    async def run(self, message, args):
        # Feeds the user input into Wolfram Alpha for an answer.
        if not args:
            await self.client.send_message(message.channel, 'Please ask a question Wolfram Alpha can answer!')
        try:
            question = ' '.join(args)
            await self.client.send_message(message.channel, self.solve(question))
        except Exception as e:
            print(f'User generated the error {e} after entering: "{args}"')
            await self.client.send_message(message.channel, "I couldn't find an answer for that, sorry. :(")

    def solve(self, question):
        app_id = config['WolframAlpha']['appID']
        wolf = wolframalpha.Client(app_id)
        data = wolf.query(question)
        return next(data.results).text
