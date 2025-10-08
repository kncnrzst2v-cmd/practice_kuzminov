import tkinter as tk
import sys
import time

class VFS:
    def __init__(self, vfs_path=None, script_path=None):
        self.root = tk.Tk()
        self.root.title("KuzminovVFS")
        self.root.geometry("1000x300")
        
        print("Параметры запуска:")
        print(f"  VFS путь: {vfs_path}")
        print(f"  Скрипт: {script_path}")
        
        self.output = tk.Text(self.root, height=15)
        self.output.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.entry = tk.Entry(self.root)
        self.entry.pack(fill=tk.X, padx=5, pady=5)
        self.entry.bind("<Return>", self.run_command)
        self.entry.focus()
        
        self.print_text("Добро пожаловать в KuzminovVFS!\n")
        
        if script_path:
            self.execute_script(script_path)
    
    def print_text(self, text):
        self.output.insert(tk.END, text)
        self.output.see(tk.END)
        self.root.update()
    
    def execute_script(self, script_path):
        self.print_text(f"Выполнение скрипта: {script_path}\n\n")
        
        try:
            with open(script_path, 'r') as file:
                for line in file:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    
                    self.print_text(f"{line}\n")
                    self.execute_command(line)
                    time.sleep(0.3)
        except FileNotFoundError:
            self.print_text(f"Ошибка: скрипт {script_path} не найден\n")
    
    def execute_command(self, command_line):
        parts = command_line.split()
        if not parts:
            return
        
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
    
    def run_command(self, event):
        cmd = self.entry.get()
        self.entry.delete(0, tk.END)
        self.print_text(f"{cmd}\n")
        self.execute_command(cmd)

if __name__ == "__main__":
    vfs_path = None
    script_path = None
    
    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == "--vfs-path" and i + 1 < len(sys.argv):
            vfs_path = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "--script" and i + 1 < len(sys.argv):
            script_path = sys.argv[i + 1]
            i += 2
        else:
            i += 1
    
    vfs = VFS(vfs_path, script_path)
    vfs.root.mainloop()