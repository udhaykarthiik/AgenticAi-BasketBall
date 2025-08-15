# 🏀 Agentic AI - Basketball Log Analyzer

This project uses multiple AI agents powered by LangChain and Gemini (Google Generative AI) to analyze basketball game logs.

## 🔧 Technologies Used
- Python 3.13
- Django 5.2.4
- LangChain
- Gemini 1.5 Flash / 2.0 Flash via Google Generative AI
- dotenv for environment variable management

## 🚀 What the App Does

You can paste in a basketball game log and the system will run 5 AI agents on the input:

1. 📥 **Data Collector Agent** – Extracts final score, winner, fast breaks, and 3-pointers.
2. 🔍 **Pattern Analyzer Agent** – Analyzes player log patterns.
3. 📈 **Pattern Finder Agent** – Detects patterns in fast break plays over 7 games.
4. ⚙️ **Pattern Improvement Agent** – Checks which players are improving or declining.
5. 🎯 **Team Strategy Agent** – Gives strategic advice for team improvement.

All agent outputs are combined and displayed in a structured view.

## 🛠️ How to Run

1. Clone the repository:
