# 🧠 02_Programs

**02_Programs** is a collection of Python-based utility tools and learning projects.  
It serves as a **personal programming toolbox**, combining automation scripts, API experiments, and educational projects — all launched from a **single interactive command-line menu**.

This repository focuses on learning, experimentation, and clean project structure rather than production-ready software.

---

## 🚀 Features

### 🏠 Main Menu
- Interactive text-based menu
- Built with **pyfiglet** and **inquirer**
- Central launcher for all included tools

### 🌦 Weather Tools
- Real-time weather information by city
- Weather forecast modules
- Powered by the **OpenWeather API**

### 📚 Edubase Downloader
- Integrated as a **Git submodule**
- Demonstrates external tool integration

### 🧪 Quiz Module
- Interactive quiz
- Launched from the main menu
- Located in `08_Quiz/`

### 💾 Auto Installer
- `setup_and_run.py` automatically:
  - Installs dependencies from `requirements.txt`
  - Installs additional requirements for subprojects (when present)
  - Launches the main menu

### ⚙️ Expandable Structure
- Modular folder layout
- Easy to add new tools and experiments
- Example structure:
  - `01_Allgemein`
  - `03_weather`
  - `07_Banking`

---

### 🧩 How to Run
python setup_and_run.py
This script will:
- Install required dependencies
- Install additional dependencies for submodules if available
- Start the interactive main menu

### 📦 Tech Stack
- Python 3.12+
- pyfiglet
- inquirer
- requests
- simple-chalk
- argparse
- Git Submodules
### 📂 Repository Structure
bash
Code kopieren
02_Programs/
│
├── 00_DownloadSorting/
├── 01_api_infos/        # Submodule
├── 02_Edubase/          # Submodule
├── 03_weather/
├── 04_Forcast/
├── 05_Mailing/
├── 06_Passwords/
├── 07_Banking/
├── 08_Annoying/
│
├── setup_and_run.py
├── requirements.txt
├── README.md
├── LICENSE
├── SECURITY.md
├── CONTRIBUTING.md
└── .gitignore
### 🔐 Security & Privacy
No real API keys, passwords, or personal data are included

Sensitive files must be ignored via .gitignore

Example or placeholder data should be used only

For details, see SECURITY.md.

### 🤝 Contributing
Contributions are welcome for educational purposes.

Please read CONTRIBUTING.md before:

Opening issues

Submitting pull requests

A Code of Conduct applies to all interactions.

### 📘 Goal
This repository exists as a learning and experimentation hub to:

Practice Python scripting

Explore APIs

Learn project organization

Use Git features such as submodules, releases, and templates

### 📝 License
This project is licensed under the MIT License.

## ✅ What this README now does
- Matches your **GitHub project maturity**
- References SECURITY & CONTRIBUTING files
- Explains submodules properly
- Sets correct expectations (educational, not production)
- Looks clean for **school, teachers, and GitHub profile**

If you want next, I can:
- shorten this for a **repo description**
- prepare a **v1.0.0 release README snapshot**
- review the repo one last time like a teacher would
