# 🧠 Offline CLI AI Agent (Python)

An **offline, CLI-based AI agent** built entirely in Python.  
The system demonstrates **symbolic reasoning, tool/function calling, explainability, and runtime learning**, without using any external APIs or internet access.

This project was built under strict hackathon constraints:
- CLI only
- Python only
- Offline execution
- Code-first evaluation

---

## ✨ Features

- ✅ Fully **offline** (no APIs, no internet)
- ✅ **CLI-only** interaction
- ✅ **Python-only** implementation
- ✅ Intent detection & rule-based reasoning
- ✅ Agent-style **tool / function calling**
- ✅ **Plugin-based architecture**
- ✅ **Explainable AI** using `/explain`
- ✅ **Runtime learning** using `/learn`
- ✅ Safe fallback (no hallucination)

---

## 🧠 What Kind of AI Is This?

This project implements a **symbolic, rule-based AI agent**.

It follows the classical AI loop:

| AI Capability | Implementation |
|--------------|----------------|
| Perception | Input normalization & intent detection |
| Reasoning | Rule-based decision logic |
| Action | Autonomous tool selection & execution |
| Learning | User-defined rules at runtime |
| Explainability | Step-by-step reasoning trace |

> This is **not** a Large Language Model.  
> It is a **transparent, inspectable AI system** designed for reliability and explainability.

---

## 🏗 Architecture Overview

main.py
└── ChatBot (CLI loop)
└── OfflineAIEngine (AI logic)
├── Intent detection
├── Rule-based reasoning
├── Learning & memory
├── Tool selection
└── Explainability
└── Tools (plugins)
└── bot/plugins/*.py


### Why this matters
- Core AI logic is isolated
- Tools are modular and extensible
- New capabilities can be added without changing the engine


## 🔌 Tool / Plugin System

Tools are implemented as **independent plugins** inside:
bot/plugins/

Each plugin defines:>>

INFO = "Tool description"

def run(arg):
    ...
Tools are automatically discovered at runtime.

## Included tools
calc → Safe math evaluation

time → Current system time

system_info → OS & Python details

Use:

/tool help
to list all available tools.

## 🧠 Runtime Learning (Symbolic Learning)
The AI can learn new rules during execution:

/learn exam All the best for your exam
exam
Output:

All the best for your exam

This demonstrates:
>Knowledge acquisition
>Adaptive behavior
>Deterministic learning
>Explainable memory usage

## 🔍 Explainability

/explain

The system prints a reasoning trace, showing:

-Input interpretation
-Intent detection
-Rule or tool selection
-Final response decision

This avoids black-box behavior and hallucinations.

## 📜 Supported Commands
Command	------------------Description
hi	                        Greeting
/skills	                    List AI capabilities
/tool help	                List all tools
/tool <name> [arg]	        Execute a tool
/learn <key> <response>	    Teach the AI
/explain	                Show reasoning trace
/exit	                    Quit

## ▶️ How to Run----

python main.py


No dependencies.
No setup.
No API keys.

🎯 Why This Qualifies as AI
-Uses symbolic reasoning, a classical AI paradigm
-Autonomously selects actions based on interpreted input
-Supports learning and adaptation
-Fully explainable decision-making
-Operates as an AI agent, not a script

Machine learning is not mandatory for AI.
Reasoning, autonomy, and explainability are.

### 👤 Author
Md. Farhan Badar
GitHub: https://github.com/frhnbadar