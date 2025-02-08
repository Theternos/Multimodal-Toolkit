import os
import subprocess
import sys
import ast
import tkinter as tk
from tkinter import messagebox

def check_unused_imports(file_path, output_text):
    output_text.insert(tk.END, f"Checking unused imports...\n")
    result = subprocess.run([sys.executable, '-m', 'vulture', file_path], capture_output=True, text=True)

    if result.stdout:
        output_text.insert(tk.END, f"Unused imports found.\n")
        output_text.insert(tk.END, result.stdout + "\n")
    else:
        output_text.insert(tk.END, f"No unused imports found.\n")

def extract_used_columns_from_code(code):
    used_columns = set()

    tree = ast.parse(code)

    for node in ast.walk(tree):
        if isinstance(node, ast.Subscript):
            if isinstance(node.value, ast.Name) and node.value.id == 'data':
                if isinstance(node.slice, ast.Index) and isinstance(node.slice.value, ast.Str):
                    used_columns.add(node.slice.value.s)

    return used_columns

def check_unused_columns_in_file(file_path, output_text):
    with open(file_path, 'r') as file:
        code = file.read()

    data_dict_column_names = []
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            if isinstance(node.targets[0], ast.Name) and node.targets[0].id == 'data':
                if isinstance(node.value, ast.Dict):
                    data_dict_column_names = [key.s for key in node.value.keys]
                    break

    if not data_dict_column_names:
        output_text.insert(tk.END, "No data dictionary found.\n")
        return

    used_columns = extract_used_columns_from_code(code)

    unused_columns = [col for col in data_dict_column_names if col not in used_columns]

    if unused_columns:
        output_text.insert(tk.END, f"Unused columns: {unused_columns}\n")
    else:
        output_text.insert(tk.END, f"No unused columns found.\n")

def extract_np_functions_used(code):
    np_functions = set()

    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute):
            if isinstance(node.value, ast.Name) and node.value.id == 'np':
                np_functions.add(node.attr)

    return np_functions

def check_unused_code(file_path, output_text):
    check_unused_imports(file_path, output_text)
    check_unused_columns_in_file(file_path, output_text)

    with open(file_path, 'r') as file:
        code = file.read()

    np_functions_used = extract_np_functions_used(code)

    if np_functions_used:
        output_text.insert(tk.END, f"\nUsed np.* functions: {', '.join(np_functions_used)}\n")
    else:
        output_text.insert(tk.END, "\nNo np.* functions used.\n")

def create_ui():
    root = tk.Tk()
    root.title("Unused Code Checker")

    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    label = tk.Label(frame, text="Checking unused imports, columns, and np.* functions in test.py file:")
    label.pack()

    output_text = tk.Text(frame, width=80, height=20, wrap=tk.WORD)
    output_text.pack()

    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, 'test.py')

    if os.path.exists(file_path):
        check_unused_code(file_path, output_text)
    else:
        output_text.insert(tk.END, f"The file 'test.py' does not exist in the directory.\n")

    root.mainloop()

if __name__ == "__main__":
    create_ui()