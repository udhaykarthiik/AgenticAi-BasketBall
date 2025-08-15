# 🏀 Agentic AI Basketball Coach

An interactive Django web app that uses **LangChain + Google Gemini** agents to act as a virtual assistant coach.  
It ingests Team X game data, reasons over it, and returns coach-ready reports and strategy suggestions through a Marvel-themed dashboard.

---

## 1. Key Features
- **Multi-Agent Pipeline**  
  • Analysis Agent → reads last 20 games and finds patterns  
  • Reporting Agent → rewrites analysis in clear Markdown  
  • (Extra) Game-Insights Agent with Wikipedia tool access  
- **Stylised Front-End**  
  Animated Arc-Reactor loader, particle effects, Chart.js radar graphs.  
- **Data Entry**  
  In-app form appends new rows to `data/team_x_games.csv`.  
- **Session-Based History**  
  Reports persist per user until **Clear Reports** is pressed.

---

## 2. Folder Structure
