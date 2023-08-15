# Desktop Automation Project

This project demonstrates how to automate the opening and closing of specific programs, folders, and web addresses using Python. It utilizes the `psutil` and `subprocess` libraries to manage processes and perform automation tasks.

## Usage

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/desktop-automation.git
```

2. Install the required dependencies:
```bash
pip install psutil
```

3. Create a config.ini file in the project directory with the following sections and examples:

```bash
[ProgramPaths]
Outlook = C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE
Chrome = C:\Program Files\Google\Chrome\Application\chrome.exe

[FolderPaths]
Desktop = C:\Users\your-username\Desktop
Documents = C:\Users\your-username\Documents

[WebAddresses]
Google = https://www.google.com/
GitHub = https://www.github.com/
```

4. Adapt the code for opening the programs you want.

5. Run the Gaming.py script to open specified programs, folders, and web addresses.
```bash
py Gaming.py
```

## Contributions
Contributions are welcome! Feel free to open an issue or submit a pull request.