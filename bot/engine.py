from bot.tools import TOOLS
from bot.tools import TOOL_INFO
from bot.explain import ReasoningTrace
from bot.skills import list_skills

class OfflineAIEngine:
    def __init__(self):
        self.trace = ReasoningTrace()

    def respond(self, user_input):
        self.trace.clear()
        text = user_input.strip()
        lower = text.lower()

        self.trace.add("Input received and normalized")

        # --- COMMANDS ---
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

            # --- TOOL HELP ---
            if tool.lower() == "help":
                self.trace.add("Tool help requested")
                if not TOOL_INFO:
                    return "No plugins loaded."
                return "\n".join(f"{name}: {desc}" for name, desc in TOOL_INFO.items())

            # --- EXECUTE TOOL ---
            if tool in TOOLS:
                self.trace.add(f"Executing tool: {tool}")
                return TOOLS[tool](arg)

            return f"Tool '{tool}' not found."

        # --- INTENT DETECTION ---
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
                "/tool <name> – execute a tool\n"
                "/tool help – list all tools with description\n"
                "/explain – show reasoning trace\n"
                "/replay – replay session\n"
                "/exit – quit"
            )

        if "time" in lower:
            self.trace.add("Time-related query detected")
            if "time" in TOOLS:
                return TOOLS["time"]("")
            else:
                return "Time tool not loaded."

        if any(word in lower for word in ["calculate", "calc", "+", "-", "*", "/"]):
            self.trace.add("Math intent detected")
            return "Use: /tool calc <expression>"

        # --- SAFE FALLBACK ---
        self.trace.add("No intent matched, safe fallback used")
        return (
            "I understand your input, but I don't have a specific skill for it yet.\n"
            "Type /skills or /help to see available actions."
        )

    def explain(self):
        return self.trace.show()
