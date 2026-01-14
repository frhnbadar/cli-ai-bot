import json
from datetime import datetime

class AuditLog:
    def __init__(self):
        self.entries = []

    def log(self, user, ai):
        self.entries.append({
            "time": datetime.now().isoformat(),
            "user": user,
            "ai": ai
        })

    def save(self, filename="session.log"):
        with open(filename, "w") as f:
            json.dump(self.entries, f, indent=2)

    def replay(self):
        return "\n".join(
            f"[{e['time']}]\nYou: {e['user']}\nAI: {e['ai']}\n"
            for e in self.entries
        )
