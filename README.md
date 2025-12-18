🧠 02_Programs

02_Programs is a collection of Python-based utility tools and learning projects.
It’s designed as a personal toolbox — combining small automation scripts, API experiments, and educational code examples — all launched from a single interactive menu.

⸻

🚀 Features
	•	🏠 Main Menu — easy text-based interface built with pyfiglet.
	•	🌦 Weather Info — fetches real-time weather data for any city using the OpenWeather API.
	•	📚 Edubase Downloader — integrates the edubase-downloader as a Git submodule.
	•	🧪 Quiz — interactive quiz launched from the main menu (08_Quiz).
	•	💾 Auto Installer — the setup_and_run.py script automatically installs dependencies globally and runs the program. It will also attempt to install additional requirements for the 08_Quiz/Program subfolder if present.
	•	⚙️ Expandable Structure — clean folder layout for adding more tools (e.g., 01_Allgemein, 03_weather, etc.).

⸻

🧩 How to Run

python setup_and_run.py

This script will:
	1.	Automatically install dependencies from requirements.txt (and quiz subfolder requirements when present)
	2.	Launch the main menu interface

⸻

📦 Tech Stack
	•	Python 3.12+
	•	pyfiglet
	•	inquirer
	•	requests
	•	simple-chalk
	•	argparse
	•	Git Submodules (for external tools)

⸻

📘 Goal

This repository serves as a personal programming hub — a place to learn, automate, and experiment with APIs, scripting, and Git integration.

⸻

📝 License

This project is under the MIT licens
