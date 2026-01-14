from bot.chat import ChatBot
from bot.tools import load_plugins

load_plugins()

bot = ChatBot()

print("AI CLI System (Offline, Inspectable)")
print("Commands: /skills /tool /explain /replay /exit\n")

while True:
    user = input("You > ")

    if user == "/exit":
        print("Total tokens:", bot.tokens.stats())
        bot.audit.save()
        break

    if user == "/explain":
        print(bot.engine.explain())
        continue

    if user == "/replay":
        print(bot.audit.replay())
        continue

    bot.handle(user)
