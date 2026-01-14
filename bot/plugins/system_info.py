import platform

INFO = "System information plugin"

def run(_):
    return (
        f"OS: {platform.system()}\n"
        f"Version: {platform.version()}\n"
        f"Machine: {platform.machine()}"
    )
