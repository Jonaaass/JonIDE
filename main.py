import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TkinterFormatter

def save_file():
    content = text_area.get("1.0", "end-1c")
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(content)
        messagebox.showinfo("Save", "File saved successfully.")

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            text_area.delete("1.0", "end")
            text_area.insert("1.0", content)
            highlight_syntax()

def highlight_syntax():
    content = text_area.get("1.0", "end-1c")
    highlighted_code = highlight(content, PythonLexer(), TkinterFormatter())
    text_area.tag_configure("code", background="white")
    text_area.insert("1.0", highlighted_code, "code")

# Create main window
root = tk.Tk()
root.title("Text Editor")
root.geometry("800x600")

# Create menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)

# Create File menu
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)

# Create text area
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, undo=True)
text_area.pack(fill=tk.BOTH, expand=True)

# Highlight syntax on initial load
highlight_syntax()

# Run the application
root.mainloop()
