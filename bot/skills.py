from bot.tools import list_tools

SKILLS = {
    "core": "Offline reasoning and intent detection",
    "plugins": "Dynamically loaded AI skills"
}

def list_skills():
    return (
        "Core Skills:\n"
        + "\n".join(f"- {v}" for v in SKILLS.values())
        + "\n\nLoaded Plugins:\n"
        + list_tools()
    )
