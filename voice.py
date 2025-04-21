import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
import pyttsx3
from word2number import w2n
import sympy as sp
import math

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def record_audio(filename='input.wav', duration=5, fs=44100):
    print("Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    sf.write(filename, recording, fs)
    print("Recording saved!")

def get_audio():
    record_audio()
    r = sr.Recognizer()
    with sr.AudioFile('input.wav') as source:
        audio = r.record(source)
    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return None
    except sr.RequestError:
        speak("Speech service is down.")
        return None

def parse_expression(speech_input):
    replacements = {
        'plus': '+',
        'minus': '-',
        'times': '*',
        'multiplied by': '*',
        'divided by': '/',
        'over': '/',
        'into': '*',
        'mod': '%',
        'modulus': '%',
        'power': '**',
        'to the power of': '**',
        'square root of': 'sqrt',
        'log of': 'log',
        'sin': 'sin()',
        'cos': 'cos()',
        'tan': 'tan()',
        'pi': 'pi',
        'e': 'E',
        'x': '*'  # Handle 'x' as multiplication
    }

    speech_input = speech_input.lower()

    # Replace words with math operators and function calls
    for word, symbol in replacements.items():
        speech_input = speech_input.replace(word, symbol)

    # Ensure correct closing parentheses for functions like sin, cos, tan, etc.
    for func in ['sin', 'cos', 'tan', 'sqrt', 'log']:
        speech_input = speech_input.replace(f'{func} ', f'{func}(')
    speech_input = speech_input.replace('sin(', 'sin()').replace('cos(', 'cos()').replace('tan(', 'tan()')

    # Add closing parentheses for each trigonometric function
    for func in ['sin', 'cos', 'tan', 'sqrt', 'log']:
        speech_input = speech_input.replace(f'{func}(', f'{func}(') + ')'

    # Split the input into words and attempt to convert any worded numbers to digits
    tokens = speech_input.split()
    converted_tokens = []
    for token in tokens:
        try:
            converted = str(w2n.word_to_num(token))  # Converts word to number
            converted_tokens.append(converted)
        except:
            converted_tokens.append(token)  # Keeps the token as is if it's not a number word

    parsed_expr = ' '.join(converted_tokens)  # Joins the tokens back into a single string
    print(f"Parsed Expression: {parsed_expr}")  # Debug print
    return parsed_expr

def main():
    speak("Please say your scientific arithmetic expression.")
    speech_input = get_audio()
    if speech_input:
        expression = parse_expression(speech_input.lower())
        try:
            # Attempt to evaluate the expression
            result = sp.sympify(expression)
            speak(f"The result is {result}")
            print(f"Result: {result}")  # Print result to the console
        except Exception as e:
            print(f" Error while evaluating: {e}")
            speak("Sorry, I couldn't calculate that.")

if __name__ == "__main__":
    main()
