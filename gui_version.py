import os
import tkinter as tk
from tkinter import filedialog, messagebox
from subprocess import Popen, PIPE

from main import main

window = tk.Tk()
window.title("ZipFuck by EHF")
window.configure(bg="#34495E")

def run_cli_version():
    process = Popen(["python", "main.py"], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    output_text.insert(tk.END, stdout.decode(), "output")
    output_text.insert(tk.END, stderr.decode(), "output")

def select_zip_file():
    zip_file_path = filedialog.askopenfilename(title="Select Zip File", filetypes=[("Zip files", "*.zip")])
    zip_file_entry.delete(0, tk.END)
    zip_file_entry.insert(0, zip_file_path)

def select_wordlist():
    wordlist_path = filedialog.askopenfilename(title="Select Wordlist", filetypes=[("Text files", "*.txt")])
    wordlist_entry.delete(0, tk.END)
    wordlist_entry.insert(0, wordlist_path)

def strip_ansi_escape_codes(text):
    import re
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[-/]*[@-~])')
    return ansi_escape.sub('', text)

def start_bruteforce():
    zip_file_path = zip_file_entry.get()
    wordlist_path = wordlist_entry.get()
    bruteforce_inprogress.grid(row=5, columnspan=3)
    window.update()
    if os.path.exists(zip_file_path) and os.path.exists(wordlist_path):
        process = Popen(["python", "main.py"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate(f"{zip_file_path}\n{wordlist_path}\n".encode())
        output_text.insert(tk.END, strip_ansi_escape_codes(stdout.decode()), "output")
        output_text.insert(tk.END, strip_ansi_escape_codes(stderr.decode()), "output")
        output_text.see(tk.END)
    else:
        messagebox.showwarning("Warning", "Please select both a zip file and a wordlist.")

def on_enter(e):
    e.widget['background'] = '#16A085'  # Lighter green

def on_leave(e):
    e.widget['background'] = '#1ABC9C'  # Original green

# Shows the Disclaimer of this program
title_label = tk.Label(window,
                       text="This Tool only works with 'ZIP Legacy Encryption'\n"
                            "ethicalhacking.freeflarum.com",
                       bg="#34495E", fg="#ECF0F1", font=("Helvetica", 12, "bold"))
title_label.grid(row=0, columnspan=3, pady=(10, 0))

zip_file_label = tk.Label(window, text="Zip File:", bg="#34495E", fg="#ECF0F1", font=("Helvetica", 10))
zip_file_label.grid(row=1, column=0, sticky="e")
zip_file_entry = tk.Entry(window, width=50, highlightbackground="#1ABC9C", highlightthickness=2, relief="flat",
                          font=("Helvetica", 10))
zip_file_entry.grid(row=1, column=1, padx=5, pady=5)
zip_file_button = tk.Button(window, text="Browse", command=select_zip_file, bg="#1ABC9C", fg="#ECF0F1",
                            activebackground="#16A085", relief="flat", borderwidth=0, padx=10, pady=5, 
                            font=("Helvetica", 10, "bold"))
zip_file_button.grid(row=1, column=2, padx=5, pady=5)

wordlist_label = tk.Label(window, text="Wordlist:", bg="#34495E", fg="#ECF0F1", font=("Helvetica", 10))
wordlist_label.grid(row=2, column=0, sticky="e")
wordlist_entry = tk.Entry(window, width=50, highlightbackground="#1ABC9C", highlightthickness=2, relief="flat",
                          font=("Helvetica", 10))
wordlist_entry.grid(row=2, column=1, padx=5, pady=5)
wordlist_button = tk.Button(window, text="Browse", command=select_wordlist, bg="#1ABC9C", fg="#ECF0F1",
                            activebackground="#16A085", relief="flat", borderwidth=0, padx=10, pady=5,
                            font=("Helvetica", 10, "bold"))
wordlist_button.grid(row=2, column=2, padx=5, pady=5)

start_button = tk.Button(window, text="Start Bruteforce", command=start_bruteforce, bg="#E67E22", fg="#ECF0F1",
                         activebackground="#D35400", relief="flat", borderwidth=0, padx=10, pady=10,
                         font=("Helvetica", 12, "bold"))
start_button.grid(row=3, columnspan=3, pady=10)

# Button to run CLI version
run_cli_button = tk.Button(window, text="Run CLI Version", command=run_cli_version, bg="#E67E22", fg="#ECF0F1",
                           activebackground="#D35400", relief="flat", borderwidth=0, padx=10, pady=10,
                           font=("Helvetica", 12, "bold"))
run_cli_button.grid(row=4, columnspan=3, pady=10)

# Text widget to display output
output_text = tk.Text(window, height=10, width=70, bg="#2C3E50", fg="#ECF0F1", font=("Helvetica", 12, "bold"), 
                      highlightbackground="#1ABC9C", highlightthickness=2, relief="flat", padx=5, pady=5)
output_text.grid(row=6, columnspan=3, padx=10, pady=10)
output_text.tag_configure("output", foreground="#ECF0F1")

bruteforce_inprogress = tk.Label(window,
                                 text="Bruteforce Attack is Activated in the Background\n "
                                      "You will be Notified after the attack is completed",
                                 bg="#34495E", fg="#ECF0F1", font=("Helvetica", 10))

for button in [zip_file_button, wordlist_button, start_button, run_cli_button]:
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

window.mainloop()

if __name__ == "__main__":
    main()

