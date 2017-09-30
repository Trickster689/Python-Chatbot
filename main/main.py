from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

print('Setting up bot...')

training_data =  [
         './chatterbot_corpus/data/bot/bot.yml',
         './chatterbot_corpus/data/english/botprofile.yml',
         './chatterbot_corpus/data/english/conversations.yml',
         './chatterbot_corpus/data/english/gossip.yml',
         './chatterbot_corpus/data/english/ai.yml',
         './chatterbot_corpus/data/english/movies.yml',
         './chatterbot_corpus/data/english/drugs.yml',
         './chatterbot_corpus/data/english/greetings.yml',
         './chatterbot_corpus/data/english/food.yml',
         './chatterbot_corpus/data/english/humor.yml'
        ]

bot = ChatBot("Fred",
logic_adapters=[
"chatterbot.logic.MathematicalEvaluation",
#"chatterbot.logic.TimeLogicAdapter",
"chatterbot.logic.BestMatch"
],
storage_adapter='chatterbot.storage.SQLStorageAdapter',
database='./database.sqlite3',
input_adapter="chatterbot.input.TerminalAdapter",
output_adapter="chatterbot.output.TerminalAdapter",
trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

bot.set_trainer(ChatterBotCorpusTrainer)
bot.train(training_data)


print("Hello I'm Fred, ask me anything...")
# The following loop will execute each time the user enters input
while True:
    try:
        # We pass None to this method because the parameter
        # is not used by the TerminalAdapter
        bot_input = bot.get_response(None)
        # Press ctrl-c, ctrl-z or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
