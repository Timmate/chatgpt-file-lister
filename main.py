import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
import os


class FileDragDropApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Drag & Drop App")
        self.files = {}
        self.create_widgets()
        self.setup_drag_and_drop()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.text = tk.Text(self.frame, wrap=tk.WORD)
        self.text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.go_button = tk.Button(self.button_frame, text="Go", command=self.display_files)
        self.go_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(self.button_frame, text="Reset", command=self.reset_files)
        self.reset_button.pack(side=tk.LEFT, padx=10)

    def setup_drag_and_drop(self):
        self.root.drop_target_register(DND_FILES)
        self.root.dnd_bind('<<Drop>>', self.on_file_drop)

    def on_file_drop(self, event):
        files = self.root.tk.splitlist(event.data)
        for file_path in files:
            if os.path.isfile(file_path):
                with open(file_path, 'r') as file:
                    content = file.read()
                    self.files[file_path] = content
        self.update_text_widget()

    def update_text_widget(self):
        self.text.delete(1.0, tk.END)
        for file_path in self.files.keys():
            self.text.insert(tk.END, f"{file_path}\n")

    def display_files(self):
        self.text.delete(1.0, tk.END)
        for ix, (file_path, content) in enumerate(self.files.items()):
            self.text.insert(tk.END, f"File path/name: {file_path}\nFile content:\n{content}\n\n")
            if ix != len(self.files.items()) - 1:
                self.text.insert(tk.END, ('=' * 40) + '\n\n')

    def reset_files(self):
        self.files.clear()
        self.text.delete(1.0, tk.END)


if __name__ == "__main__":
    root = TkinterDnD.Tk()
    app = FileDragDropApp(root)
    root.mainloop()
