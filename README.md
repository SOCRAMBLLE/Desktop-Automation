# Desktop Automation Project

This project demonstrates how to automate the opening and closing of specific programs, folders, and web addresses using Python. It utilizes the `psutil` and `subprocess` libraries to manage processes and perform automation tasks.

## Usage

1. **Clone the Repository:** Start by cloning the repository to your local machine:
```bash
git clone https://github.com/your-username/desktop-automation.git
```

2. **Install Dependencies:** Install the required dependencies using pip:
```bash
pip install psutil
```

3. **Configure config.ini:** Create a config.ini file in the project directory with the following sections and examples:

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

4. **Customize and Run Scripts:** Adapt the code in the provided script templates to open the specific programs, folders, and web addresses you want.

5. **Run the User Interface:** To use the project, run the User Interface script to open the dashboard. Click on the desired script button to execute it:
```bash
py GUI.py
```

## Contributions
Contributions are welcome! Feel free to open an issue or submit a pull request.