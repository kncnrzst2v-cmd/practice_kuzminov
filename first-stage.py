import tkinter as tk

class VFS:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("KuzminovVFS")
        self.root.geometry("1000x300")
        
        self.output = tk.Text(self.root, height=15)
        self.output.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.entry = tk.Entry(self.root)
        self.entry.pack(fill=tk.X, padx=5, pady=5)
        self.entry.bind("<Return>", self.run_command)
        self.entry.focus()
    
    def print_text(self, text):
        self.output.insert(tk.END, text)
        self.output.see(tk.END)
    
    def run_command(self, event):
        cmd = self.entry.get()
        self.entry.delete(0, tk.END)
        self.print_text(f"$ {cmd}\n")
        
        parts = cmd.split()
        if not parts: return
        
        command = parts[0]
        args = parts[1:]
        
        if command == "exit":
            self.root.quit()
        elif command == "ls":
            self.print_text(f"ls: {args}\n")
        elif command == "cd":
            self.print_text(f"cd: {args}\n")
        else:
            self.print_text(f"Ошибка: команда '{command}' не найдена\n")

if __name__ == "__main__":
    vfs = VFS()
    vfs.root.mainloop()