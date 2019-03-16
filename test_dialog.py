# Imports
# -----------
from rasa_core import run
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter


def run_bot(serve_forever=True):
    interpreter = RasaNLUInterpreter('./models/nlu/default/chat')
    agent = Agent.load('./models/dialogue', interpreter=interpreter)
    run.serve_application(agent, channel='cmdline')
    return agent


# Run bot
# ------------
if __name__ == '__main__':
    run_bot()
