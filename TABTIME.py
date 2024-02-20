import tkinter as tk
from threading import Thread
import time
import webbrowser

class BrowserAutomationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lary Gary Mods Auto Browser")
        self.root.config(bg="#f0f0f0")

        # Set a fixed window size
        self.root.geometry("500x110")
        self.root.resizable(False, False)

        # Grid configuration
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # URL Entry
        tk.Label(root, text="URL:", bg="#f0f0f0", fg="#333").grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.url_entry = tk.Entry(root, width=34, bg="#fff", fg="#333")
        self.url_entry.grid(row=0, column=1, padx=5, pady=5)

        # Start Button
        self.start_button = tk.Button(root, text="Start", command=self.start_process, bg="#4CAF50", fg="#fff")
        self.start_button.grid(row=0, column=2, padx=5, pady=5)

        # Stop Button
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_process, state=tk.DISABLED, bg="#f44336", fg="#fff")
        self.stop_button.grid(row=0, column=3, padx=5, pady=5)

        # Dark Mode Toggle Button
        self.dark_mode_button = tk.Button(root, text="Dark Mode", command=self.toggle_dark_mode, bg="#333", fg="#fff")
        self.dark_mode_button.grid(row=0, column=4, padx=5, pady=5)

        # Neon Mode Toggle Button
        self.neon_mode_button = tk.Button(root, text="Rick Mode", command=self.toggle_neon_mode, bg="#333", fg="#fff")
        self.neon_mode_button.grid(row=0, column=5, padx=5, pady=5)

        self.running = False
        self.dark_mode = False
        self.neon_mode = False

        # Set the web browser to Mozilla Firefox
        self.browser_path = "C:/Program Files/Mozilla Firefox/firefox.exe"
        webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(self.browser_path))

        # Grid configuration
        self.root.grid_rowconfigure(1, weight=0)  # Change weight to 0
        self.root.grid_columnconfigure(0, weight=1)
        
        # Info Label
        self.info_label = tk.Label(root, text="Made By Lary Gary Mods V1.2", bg="#f0f0f0", fg="#333")
        self.info_label.grid(row=1, column=0, columnspan=6, sticky='s', pady=1)

        # Custom Browser Info and Project Details Label
        self.details_label = tk.Label(root, text="Custom Browser Automation Tool\n Automated Tab Management for Efficient Browsing", bg="#f0f0f0", fg="#333")
        self.details_label.grid(row=2, column=0, columnspan=6, sticky='n', pady=1)

    def start_process(self):
        url = self.url_entry.get()
        if url.startswith("http"):
            self.running = True
            self.open_in_browser(url)
        else:
            self.running = True
            self.open_in_browser(f"file:///{url}")

    def open_in_browser(self, url):
        thread = Thread(target=self.open_in_background, args=(url,))
        thread.start()
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

    def open_in_background(self, url):
        while self.running:
            webbrowser.get('firefox').open_new(url)
            time.sleep(15)  # Adjust the sleep time as needed

    def stop_process(self):
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def toggle_dark_mode(self):
        dark_bg = "#333"
        dark_fg = "#fff"
        entry_dark_bg = "#555"
        entry_dark_fg = "#fff"
    
        if self.dark_mode:
            self.root.config(bg="#f0f0f0")
            self.url_entry.config(bg="#fff", fg="#333")
            self.start_button.config(bg="#4CAF50", fg="#fff")
            self.stop_button.config(bg="#f44336", fg="#fff")
            self.dark_mode_button.config(bg="#333", fg="#fff")
            self.neon_mode_button.config(bg="#333", fg="#fff")
            self.info_label.config(bg="#f0f0f0", fg="#333")
            self.details_label.config(bg="#f0f0f0", fg="#333")
            for widget in self.root.winfo_children():
                if isinstance(widget, tk.Label):
                    widget.config(bg="#f0f0f0", fg="#333")
            self.dark_mode = False
        else:
            self.root.config(bg=dark_bg)
            self.url_entry.config(bg=entry_dark_bg, fg=entry_dark_fg)
            self.start_button.config(bg="#4CAF50", fg=dark_fg)
            self.stop_button.config(bg="#f44336", fg=dark_fg)
            self.dark_mode_button.config(bg=entry_dark_bg, fg=dark_fg)
            self.neon_mode_button.config(bg=entry_dark_bg, fg=dark_fg)
            self.info_label.config(bg=dark_bg, fg=dark_fg)
            self.details_label.config(bg=dark_bg, fg=dark_fg)
            for widget in self.root.winfo_children():
                if isinstance(widget, tk.Button):
                    widget.config(bg=dark_bg, fg=dark_fg)
                elif isinstance(widget, tk.Label):
                    widget.config(bg=dark_bg, fg=dark_fg)
            self.dark_mode = True
            self.neon_mode = False

    def toggle_neon_mode(self):
    # Define neon mode colors
        neon_background = "#0EE701"  # Bright neon green for the background
        text_color = "#000000"  # Black for text
        entry_and_button_bg = "#1B1F23"  # Dark for entry box and buttons

        # Apply neon mode colors
        self.root.config(bg=neon_background)
        self.url_entry.config(bg=entry_and_button_bg, fg=text_color)
        self.start_button.config(bg=entry_and_button_bg, fg=neon_background)
        self.stop_button.config(bg=entry_and_button_bg, fg=neon_background)
        self.dark_mode_button.config(bg=entry_and_button_bg, fg=neon_background)
        self.neon_mode_button.config(bg=entry_and_button_bg, fg=neon_background)
        self.info_label.config(bg=neon_background, fg=text_color)
        self.details_label.config(bg=neon_background, fg=text_color)

        for widget in self.root.grid_slaves():
            if isinstance(widget, tk.Label):
                widget.config(bg=neon_background, fg=text_color)

        # Indicate that neon mode is now active
        self.neon_mode = True
        # Ensure dark mode is not active
        self.dark_mode = False






# Creating Tkinter window
root = tk.Tk()
app = BrowserAutomationApp(root)
root.mainloop()
