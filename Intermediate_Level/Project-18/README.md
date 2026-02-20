# ⏰ Python Alarm Clock

A simple yet effective alarm clock built with Python.  
It allows you to set a specific time in **24-hour format (HH:MM:SS)**, continuously checks the system time, and plays a custom sound (`alarm.wav`) when the alarm triggers.

---

## 📌 Features
- Set alarms in **24-hour format** (`HH:MM:SS`).
- Displays **live system time** in the console.
- Plays a **custom alarm sound** (`alarm.wav`) when the alarm time is reached.
- Runs the alarm sound in a **separate thread** for smooth execution.
- Lightweight and beginner-friendly project.

---

## 🛠️ Requirements
- **Python Version:** Python 3.x
- **Dependencies:**  
  - `time` (built-in)  
  - `datetime` (built-in)  
  - `threading` (built-in)  
  - `os` (built-in)  
  - `winsound` (Windows-only)

- **Alarm Sound File:** Place an `alarm.wav` file in the same directory as the script.

---

## 💻 Platform Support
| Platform | Support | Notes |
|----------|----------|-------|
| **Windows** | ✅ Full support | Uses `winsound` for audio playback. |
| **Linux** | ⚠️ Partial support | Replace `winsound` with `playsound` or `pygame`. |
| **macOS** | ⚠️ Partial support | Replace `winsound` with `playsound` or `pygame`. |

---

## 🚀 Usage
1. Clone the repository or download the script.
2. Ensure `alarm.wav` is in the same folder as the script.
3. Run the script:
   ```bash
   python alarm_clock.py
   ```
4. Enter the alarm time in **HH:MM:SS (24-hour format)** when prompted:
   ```
   ==== Python Alarm Clock ====
   Format: HH:MM:SS (24-hour format)
   Enter alarm time: 07:30:00
   ```
5. The program will display the current time until the alarm triggers:
   ```
   Alarm set for 07:30:00
   Waiting for alarm...
   Current Time: 07:29:59
   🔔 WAKE UP! 🔔
   ```

---

## 📂 Project Structure
```
📁 Python-Alarm-Clock
 ┣ 📄 alarm_clock.py
 ┣ 📄 alarm.wav
 ┗ 📄 README.md
```

---

## 🔮 Future Improvements
- Add **cross-platform audio support** (using `playsound` or `pygame`).
- Allow **multiple alarms** to be set in one session.
- Add **snooze functionality** (e.g., 5-minute repeat).
- Provide a **GUI interface** using `Tkinter` or `PyQt`.
- Add **custom alarm messages** or motivational quotes.
- Integrate with **system notifications** for better visibility.
- Option to **loop alarm sound** until stopped manually.

---

## 👨‍💻 Author
**Subhadeep Bag**  
🔗 [GitHub Profile](https://github.com/SUBHADEEPBAG300)
