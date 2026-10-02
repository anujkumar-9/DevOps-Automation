import subprocess
from pathlib import Path


PROJECT_DIR = Path("my-app")


def run_command(command):
    print(f"Running: {' '.join(command)}")

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("Command failed!")
        print(result.stderr)
        raise SystemExit(1)

    print(result.stdout)


def main():
    print("Starting DevOps automation...")

    # Create project directory
    PROJECT_DIR.mkdir(exist_ok=True)

    # Initialize Git repository
    run_command(["git", "init"])

    # Check Git status
    run_command(["git", "status"])

    print("DevOps automation completed successfully!")


if __name__ == "__main__":
    main()



#     Simple flow
# Python Script
#      ↓
# Create Directory
#      ↓
# Git Init
#      ↓
# Git Status
#      ↓
# Automation Complete
# Interview mein important:

# subprocess → Python se system/Git/Docker/Terraform jaise commands execute karne ke liye.

# Path → Files aur directories ko programmatically handle karne ke liye.

# returncode → Command successful hui ya failed, check karne ke liye.

# if __name__ == "__main__": → Script ko directly run karne par main() execute karta hai.

# Ye file bhi reference/practice ke liye hai; abhi run karne ki zarurat nahi.