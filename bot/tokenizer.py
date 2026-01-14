class TokenCounter:
    def __init__(self):
        self.total_tokens = 0

    def count(self, text):
        tokens = len(text.split())
        self.total_tokens += tokens
        return tokens

    def stats(self):
        return self.total_tokens
