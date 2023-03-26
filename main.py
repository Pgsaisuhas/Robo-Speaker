import pyttsx3

# Create a TTS engine
engine = pyttsx3.init()

# Set the voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Speak a text message
if __name__ == '__main__':
    print("Welcome to Robo Speaker 1.0. created by Sai Suhas")
    while True:
        x = input("Enter what you want me to speak: ")
        if x == "Exit":
            engine.say("Ok!!, it was nice meeting you, bahh bye.")
            engine.runAndWait()
            break
        # command = f"{x}"
        engine.say(x)
        engine.runAndWait()
