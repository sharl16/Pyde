import os
import tkinter as tk
from tkinter import ttk

def populate_tree(tree, node, parent=''):
    if os.path.isdir(node):
        folder_node = tree.insert(parent, 'end', text=os.path.basename(node), open=False)
        for item in os.listdir(node):
            populate_tree(tree, os.path.join(node, item), parent=folder_node)
    else:
        insert_file(tree, node, parent=parent)

def insert_file(tree, file_path, parent=''):
    folder, file_name = os.path.split(file_path)
    tree.insert(parent, 'end', text=file_name)

def main():
    root = tk.Tk()
    root.title("File Explorer")

    tree = ttk.Treeview(root)
    tree.pack(fill='both', expand=True)

    # Add a scrollbar
    scrollbar = ttk.Scrollbar(root, orient='vertical', command=tree.yview)
    scrollbar.pack(side='right', fill='y')
    tree.configure(yscroll=scrollbar.set)

    # Populate tree with current directory
    current_dir = os.getcwd()
    populate_tree(tree, current_dir)

    root.mainloop()

if __name__ == "__main__":
    main()
