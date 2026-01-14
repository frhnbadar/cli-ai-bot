from bot.engine import OfflineAIEngine
from bot.streamer import stream_text
from bot.tokenizer import TokenCounter
from bot.audit import AuditLog
from bot.eval import confidence_score

class ChatBot:
    def __init__(self):
        self.engine = OfflineAIEngine()
        self.tokens = TokenCounter()
        self.audit = AuditLog()

    def handle(self, user_input):
        self.tokens.count(user_input)
        response = self.engine.respond(user_input)
        self.tokens.count(response)

        self.audit.log(user_input, response)

        stream_text(response)
        print(f"\n[confidence: {confidence_score(response)}]")
