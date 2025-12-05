import os
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def run(cmd, **kwargs):
    """Run a command and stream its output."""
    print("> " + " ".join(cmd))
    subprocess.check_call(cmd, **kwargs)

def install_requirements():
    """Install dependencies from requirements.txt globally."""
    req_file = os.path.join(BASE_DIR, "requirements.txt")
    if os.path.exists(req_file):
        print("📦 Installing required packages globally...")
        run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], cwd=BASE_DIR)
        run([sys.executable, "-m", "pip", "install", "-r", req_file], cwd=BASE_DIR)
        print("All required packages are installed.\n")
    else:
        print("No requirements.txt found — skipping package installation.\n")
    """Install dependencies from requirements.txt globally."""

def run_main():
    """Run the main menu program."""
    main_path = os.path.join(BASE_DIR, "main.py")
    if not os.path.exists(main_path):
        print("❌ main.py not found in the project folder!")
        sys.exit(1)

    print("▶️  Running main.py...\n")
    run([sys.executable, main_path], cwd=BASE_DIR)

if __name__ == "__main__":
    install_requirements()
    run_main()
