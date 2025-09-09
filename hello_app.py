import tkinter as tk
from tkinter import messagebox
import sys
import os

class HelloApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hello Application")
        self.root.geometry("350x250")
        self.root.configure(bg='lightblue')
        self.root.resizable(False, False)
        
        # Center the window
        self.center_window()
        
        # Create main frame
        main_frame = tk.Frame(root, bg='lightblue', padx=20, pady=20)
        main_frame.pack(expand=True, fill='both')
        
        # Create title label
        title_label = tk.Label(
            main_frame, 
            text="🎉 Welcome to Hello App! 🎉", 
            font=("Arial", 14, "bold"),
            bg='lightblue',
            fg='darkblue'
        )
        title_label.pack(pady=(0, 20))
        
        # Create the "Hi" button with hover effects
        self.hi_button = tk.Button(
            main_frame,
            text="👋 Hi",
            command=self.show_hello,
            font=("Arial", 14, "bold"),
            bg='#4CAF50',
            fg='white',
            width=15,
            height=2,
            relief='raised',
            cursor='hand2'
        )
        self.hi_button.pack(pady=10)
        
        # Bind hover effects
        self.hi_button.bind("<Enter>", self.on_hover_enter)
        self.hi_button.bind("<Leave>", self.on_hover_leave)
        
        # Create status label
        self.status_label = tk.Label(
            main_frame,
            text="Click 'Hi' to see the magic! ✨",
            font=("Arial", 10),
            bg='lightblue',
            fg='gray'
        )
        self.status_label.pack(pady=10)
        
        # Create exit button
        exit_button = tk.Button(
            main_frame,
            text="❌ Exit",
            command=self.safe_exit,
            font=("Arial", 10),
            bg='#f44336',
            fg='white',
            width=10,
            cursor='hand2'
        )
        exit_button.pack(pady=(20, 0))
    
    def center_window(self):
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (350 // 2)
        y = (self.root.winfo_screenheight() // 2) - (250 // 2)
        self.root.geometry(f"350x250+{x}+{y}")
    
    def on_hover_enter(self, event):
        self.hi_button.config(bg='#45a049')
    
    def on_hover_leave(self, event):
        self.hi_button.config(bg='#4CAF50')
    
    def show_hello(self):
        # Update status
        self.status_label.config(text="Hello message displayed! 🎊", fg='green')
        
        # Create a new window with "hello" message
        hello_window = tk.Toplevel(self.root)
        hello_window.title("Hello Message!")
        hello_window.geometry("300x180")
        hello_window.configure(bg='lightyellow')
        hello_window.resizable(False, False)
        
        # Center the hello window
        hello_window.update_idletasks()
        x = (hello_window.winfo_screenwidth() // 2) - (300 // 2)
        y = (hello_window.winfo_screenheight() // 2) - (180 // 2)
        hello_window.geometry(f"300x180+{x}+{y}")
        
        # Make it modal
        hello_window.grab_set()
        hello_window.focus_set()
        
        # Create hello content
        hello_frame = tk.Frame(hello_window, bg='lightyellow', padx=20, pady=20)
        hello_frame.pack(expand=True, fill='both')
        
        hello_label = tk.Label(
            hello_frame,
            text="🎈 Hello! 🎈",
            font=("Arial", 28, "bold"),
            bg='lightyellow',
            fg='#FF6B35'
        )
        hello_label.pack(expand=True)
        
        subtitle_label = tk.Label(
            hello_frame,
            text="Your executable is working perfectly!",
            font=("Arial", 10),
            bg='lightyellow',
            fg='gray'
        )
        subtitle_label.pack()
        
        # Close button
        close_button = tk.Button(
            hello_frame,
            text="Close",
            command=hello_window.destroy,
            font=("Arial", 10),
            bg='white',
            fg='black',
            cursor='hand2'
        )
        close_button.pack(pady=(10, 0))
        
        # Reset status after window closes
        def reset_status():
            if hello_window.winfo_exists():
                hello_window.after(100, reset_status)
            else:
                self.status_label.config(text="Click 'Hi' to see the magic! ✨", fg='gray')
        
        hello_window.protocol("WM_DELETE_WINDOW", lambda: [hello_window.destroy(), reset_status()])
    
    def safe_exit(self):
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            self.root.quit()

def main():
    root = tk.Tk()
    app = HelloApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
