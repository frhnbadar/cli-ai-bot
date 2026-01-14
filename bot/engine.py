from bot.tools import TOOLS, TOOL_INFO
from bot.explain import ReasoningTrace
from bot.skills import list_skills


class OfflineAIEngine:
    def __init__(self):
        self.trace = ReasoningTrace()
        self.learned_rules = {}

    def respond(self, user_input):
        self.trace.clear()
        text = user_input.strip()
        lower = text.lower()

        self.trace.add("Input received and normalized")

        # ---------- LEARNING ----------
        if lower.startswith("/learn"):
            self.trace.add("Learning new rule")
            parts = text.split(maxsplit=2)

            if len(parts) < 3:
                return "Usage: /learn <keyword> <response>"

            key, value = parts[1].lower(), parts[2]
            self.learned_rules[key] = value
            return f"Learned new rule: {key}"

        # ---------- COMMANDS ----------
        if lower == "/skills":
            self.trace.add("User requested skill list")
            return list_skills()

        if lower.startswith("/tool"):
            self.trace.add("Tool invocation detected")
            parts = text.split(maxsplit=2)

            if len(parts) < 2:
                return "Usage: /tool <tool_name> [argument]"

            tool = parts[1]
            arg = parts[2] if len(parts) > 2 else ""

            if tool.lower() == "help":
                self.trace.add("Tool help requested")
                if not TOOL_INFO:
                    return "No plugins loaded."
                return "\n".join(f"{name}: {desc}" for name, desc in TOOL_INFO.items())

            if tool in TOOLS:
                self.trace.add(f"Executing tool: {tool}")
                return TOOLS[tool](arg)

            return f"Tool '{tool}' not found."

        # ---------- LEARNED MEMORY ----------
        if lower in self.learned_rules:
            self.trace.add("Matched learned rule")
            return self.learned_rules[lower]

        # ---------- INTENT DETECTION ----------
        if any(greet in lower for greet in ["hi", "hello", "hey"]):
            self.trace.add("Greeting intent detected")
            return (
                "Hello. I am an offline, inspectable AI system.\n"
                "Type /skills to see what I can do."
            )

        if "who are you" in lower or "your name" in lower:
            self.trace.add("Identity intent detected")
            return "I am an offline CLI-based AI designed for explainability and reliability."

        if "help" in lower:
            self.trace.add("Help intent detected")
            return (
                "Available commands:\n"
                "/skills – list AI capabilities\n"
                "/learn <key> <response> – teach the AI\n"
                "/tool <name> – execute a tool\n"
                "/tool help – list tools\n"
                "/explain – show reasoning trace\n"
                "/exit – quit"
            )

        if "time" in lower and "time" in TOOLS:
            self.trace.add("Time-related query detected")
            return TOOLS["time"]("")

        if any(word in lower for word in ["calculate", "calc", "+", "-", "*", "/"]):
            self.trace.add("Math intent detected")
            return "Use: /tool calc <expression>"

        # ---------- FALLBACK ----------
        self.trace.add("No intent matched, safe fallback used")
        return (
            "I understand your input, but I don't have a specific skill for it yet.\n"
            "Type /skills or /help to see available actions."
        )

    def explain(self):
        return self.trace.show()
