# ⌨️ Typing Speed Trainer with Tkinter

A simple Python GUI app that helps you practice and improve your typing speed and accuracy. Built with **Tkinter** and powered by a custom list of practice sentences.

---

## 🧠 Features

- Randomized sentences loaded from a text file (`sentences.txt`)
- Timer starts automatically on first keypress
- Press **Enter** to submit — no mouse needed
- Automatically loads the next sentence after each attempt
- Displays:
  - ⏱ Time taken
  - 📈 Words per minute (WPM)
  - ✅ Accuracy (%)
- Ends with a completion message

---

## 📁 File Structure
Average-typing/
```
├── main.py # Main script to run the GUI app
├── sentences.txt # Text file containing practice sentences
├── README.md # This file
└── .gitignore # Optional Git ignore rules
```

---

## 📜 Example `sentences.txt`

🚀 How to Run
Install Python 3.6 or higher

Make sure sentences.txt is in the same folder as main.py

Run the app:
python main.py

⌨️ Controls
- 🖱 Start typing: Timer starts on your first keystroke
- ⏎ Press Enter: Submit your typed sentence and go to the next one
- 🏁 After the last sentence, the app will display "All sentences completed!"

💡 Future Ideas
- Show average WPM across all sentences
- Add a restart button
- Import longer texts or paragraphs
- Export results to a CSV or log file
