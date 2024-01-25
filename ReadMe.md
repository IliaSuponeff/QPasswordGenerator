# PasswordGenerator

## Help

### Initialize virtual environment
```
Linux | MacOS
python3 -m venv .venv
```
```
Window
python -m venv .venv
```

### Activate virtual environment
```
Linux | MacOS
source .venv/bin/activate

Window | cmd.exe
.\.venv\Scripts\activate.bat

Window | PowerShell
.\.venv\Scripts\Activate.ps1
```

### Convert `main_window_template.ui` file to `main_window.py` file
```
bash | bat

pyside6-uic ./src/ui/main_window_template.ui -o ./src/ui/main_window.py
```
