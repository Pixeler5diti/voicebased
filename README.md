# 🎙️ Voice-Based Calculator

A Python-based voice-controlled calculator that listens to your spoken arithmetic expressions, converts them into valid math expressions, and speaks out the result. Perfect for quick, hands-free calculations!
![image](https://github.com/user-attachments/assets/81563120-e31b-4ac2-a680-b4bb85e15f24)


---

## 🚀 Features

- 🎧 Takes voice input using your microphone  
- 🔉 Reads the result out loud using text-to-speech  
- 🧠 Converts natural language arithmetic to valid math expressions  
- 🔢 Converts number words to digits (e.g., "twenty five" → 25)  
- ➕ Supports basic arithmetic operations: `+`, `-`, `*`, `/`, `%`, `**`

---

## ❗ Not Yet Supported

- Scientific functions like `sin`, `cos`, `tan`, `log`, `sqrt`, etc. (coming soon!)

---

## 🛠️ Technologies Used

- `sounddevice` & `soundfile` – audio recording  
- `speech_recognition` – convert speech to text  
- `pyttsx3` – text-to-speech  
- `word2number` – convert words to numbers  
- `sympy` – for symbolic math evaluation  

---

## 🧪 Sample Commands

Say things like:
- `"twenty plus thirty"`
- `"forty divided by five"`
- `"three power two"`
- `"ten modulus three"`

And the program will say the result!

---

## 🖥️ Installation

1. **Clone the repository**:
```bash
git clone git@github.com:Pixeler5diti/voicebased.git
cd voicebased
