# Setup Guide

## Prerequisites

- Python 3.8 or higher installed
- A terminal (Mac/Linux) or Command Prompt / PowerShell (Windows)

---

## Do You Need a Virtual Environment?

This course uses **only Python's standard library** — no third-party packages are required.
You can run every file directly without creating a virtual environment:

```bash
# Mac / Linux
python3 choco_pos/session1_receipt.py

# Windows
python choco_pos/session1_receipt.py
```

A virtual environment is only needed if you later `pip install` something (e.g. `flask`, `requests`, `pandas`). The steps below are here for reference.

---

## Creating a Virtual Environment

### Mac / Linux

```bash
# Create
python3 -m venv venv

# Activate
source venv/bin/activate

# Deactivate
deactivate
```

### Windows — Command Prompt

```bat
# Create
python -m venv venv

# Activate
venv\Scripts\activate.bat

# Deactivate
deactivate
```

### Windows — PowerShell

```powershell
# Create
python -m venv venv

# Activate
venv\Scripts\Activate.ps1

# Deactivate
deactivate
```

> **PowerShell blocked?** Run this one-time fix, then try activating again:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```
> Windows blocks unsigned scripts by default. This command allows locally created scripts to run.

---

## Installing & Saving Dependencies

Once your virtual environment is active:

```bash
# Install a package
pip install requests

# Save all installed packages to a file
pip freeze > requirements.txt

# Restore packages on another machine
pip install -r requirements.txt
```

Your terminal prompt will show `(venv)` when the environment is active.

---

## Running the ChocoPOS Project

No setup required — just run the session file for the session you are in:

| Session | Command (Mac/Linux) | Command (Windows) |
|---|---|---|
| Session 1 | `python3 choco_pos/session1_receipt.py` | `python choco_pos/session1_receipt.py` |
| Session 2 | `python3 choco_pos/session2_menu.py` | `python choco_pos/session2_menu.py` |
| Session 3 | `python3 choco_pos/session3_tracker.py` | `python choco_pos/session3_tracker.py` |
| Session 4 | `python3 choco_pos/session4_shop_engine.py` | `python choco_pos/session4_shop_engine.py` |
