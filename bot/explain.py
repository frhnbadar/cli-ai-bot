class ReasoningTrace:
    def __init__(self):
        self.steps = []

    def add(self, step):
        self.steps.append(step)

    def clear(self):
        self.steps = []

    def show(self):
        return "\n".join(f"- {s}" for s in self.steps)
