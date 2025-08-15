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

agents/ # LangChain agent definitions
router/ # agent_pipeline.py orchestrates agents
core/ # Django project settings / urls
dashboard/
├─ templates/home.html
├─ static/css/style.css
├─ views.py # main dashboard logic
├─ forms.py # Add-game form
└─ templatetags/markdown_extras.py
data/
└─ team_x_games.csv # sample game data (append-only)
requirements.txt # Python deps
package.json # Bootstrap / jQuery for front-end


---

## 3. Quick Start

### Prerequisites
Python 3.10+
Node 18+ (for frontend packages)

### 1️⃣ Clone & Install
git clone <repo>
cd <repo>
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
npm install # only if you want to rebuild CSS/JS

### 2️⃣ Environment Vars  
Create `.env` in project root:
GEMINI_API_KEY_AGENT1=your_google_api_key
GEMINI_API_KEY_AGENT2=your_google_api_key

### 3️⃣ Run Dev Server

Visit `http://127.0.0.1:8000/`.

---

## 4. Dashboard Work-Flow
1. **Analyse Team Data** – general performance summary + radar chart.  
2. **Assess Strengths** – focuses on fast breaks & 3-pt defence.  
3. **Build Strategy** – returns actionable training plan.  
4. **Add Game** – append new row to CSV via form.  
5. **Clear Reports** – wipes current session.

---

## 5. Tech Stack
| Layer      | Tech                               |
|------------|------------------------------------|
| Backend    | Django 5, SQLite (dev), Pandas     |
| AI/Agents  | LangChain, Google Gemini 1.5 Flash |
| Front-End  | HTML 5, Bootstrap 5, Chart.js, Phosphor Icons |
| Styling    | Custom CSS (Marvel / neon theme)   |

---

## 6. Known Limitations
- Uses **deprecated** `initialize_agent`; upgrade to AgentExecutor recommended.  
- CSV is single source; move to a DB or DataFrame tool for scale.  
- Wikipedia tool included but not yet used in prompts.  
- Radar chart only updates on “Analyse Team Data” action.

---

## 7. Contributing
1. Fork → feature branch → PR.  
2. Adhere to PEP 8 and run `black .`.  
3. Add doc-strings / comments for any agent prompt changes.

---

## 8. License
MIT — see `LICENSE` file.

*Happy coaching!* 🚀


