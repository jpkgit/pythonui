import tkinter as tk
from threading import Thread
import time

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Background Thread UI Update")

        # Text box
        self.text_box = tk.Text(root, height=10, width=40)
        self.text_box.pack(pady=20)

        # Start the background thread
        self.running = True
        self.thread = Thread(target=self.update_text_box)
        self.thread.start()

        # Close event
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def update_text_box(self):
        counter = 0
        while self.running:
            counter += 1
            message = f"Update {counter}\n"
            self.text_box.insert(tk.END, message)
            self.text_box.see(tk.END)  # Scroll to the end
            time.sleep(1)

    def on_closing(self):
        self.running = False
        self.thread.join()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
