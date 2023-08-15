import tkinter as tk
import os

def execute_script(name):
    script_path = os.path.join('scripts', name + '.py')
    os.system(f'py {script_path}')

root = tk.Tk()
root.title("Desktop Automation Dashboard")
root.geometry("360x150")
root.configure(bg="#A1DE93")

frame = tk.Frame(root)
frame.grid(row=0, column=0, pady=20)

button_padx = 10
button_pady = 10

coding_button = tk.Button(root, text="Coding", command=lambda: execute_script('Coding'), bg="#70A1D7", fg="#000000", font="bold", padx=20)
coding_button.grid(row=1, column=0, pady=button_pady, padx=button_padx)

gaming_button = tk.Button(root, text="Gaming", command=lambda: execute_script('Gaming'), bg="#F47C7C", fg="#000000", font="bold", padx=20)
gaming_button.grid(row=1, column=1, pady=button_pady, padx=button_padx)

work_button = tk.Button(root, text="Work", command=lambda: execute_script('Work'), bg="#F7F48B", fg="#000000", font="bold", padx=20)
work_button.grid(row=1, column=2, pady=button_pady, padx=button_padx)

root.mainloop()
