import tkinter as tk
from tkinter import messagebox
import time
import random

class TypingTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Trainer")

        # Load all sentences
        with open("sentences.txt", "r") as f:
            self.sentences = [line.strip() for line in f if line.strip()]
        random.shuffle(self.sentences)

        self.current_index = 0
        self.start_time = None

        self.label = tk.Label(root, text="", wraplength=500, font=("Arial", 14))
        self.label.pack(pady=20)

        self.entry = tk.Text(root, height=5, width=60)
        self.entry.pack()
        self.entry.bind("<KeyPress>", self.start_timer)
        self.entry.bind("<Return>", self.on_enter_press)

        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.next_btn = tk.Button(root, text="Submit & Next", command=self.check_sentence)
        self.next_btn.pack(pady=5)

        self.load_sentence()

    def load_sentence(self):
        if self.current_index < len(self.sentences):
            self.label.config(text=self.sentences[self.current_index])
            self.entry.delete("1.0", tk.END)
            self.result_label.config(text="")
            self.start_time = None
        else:
            self.label.config(text="✅ All sentences completed!")
            self.entry.config(state=tk.DISABLED)
            self.next_btn.config(state=tk.DISABLED)

    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = time.time()

    def on_enter_press(self, event):
        self.check_sentence()
        return "break"

    def check_sentence(self):
        if self.start_time is None:
            messagebox.showinfo("Wait", "Please start typing first.")
            return

        end_time = time.time()
        time_taken = end_time - self.start_time

        typed = self.entry.get("1.0", tk.END).strip()
        expected = self.sentences[self.current_index]

        words = typed.split()
        wpm = round((len(words) / time_taken) * 60)

        # Calculate word-by-word accuracy
        correct_words = sum(1 for i, w in enumerate(typed.split()) if i < len(expected.split()) and w == expected.split()[i])
        accuracy = round((correct_words / len(expected.split())) * 100)

        self.result_label.config(
            text=f"Time: {round(time_taken, 2)}s | WPM: {wpm} | Accuracy: {accuracy}%"
        )

        self.current_index += 1
        self.root.after(1500, self.load_sentence)  # wait 1.5 seconds then load next

