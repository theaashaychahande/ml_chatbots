import json
import os
import datetime
import random
from colorama import Fore, Style, init

init(autoreset=True)

MEMORY_FILE = "chat_memory.json"

EMOTION_KEYWORDS = {
    "happy": ["happy", "great", "awesome", "good", "fantastic", "joy"],
    "sad": ["sad", "bad", "depressed", "down", "unhappy", "miserable"],
    "angry": ["angry", "mad", "frustrated", "pissed", "annoyed"],
    "neutral": ["ok", "fine", "nothing", "alright"]
}

RESPONSES = {
    "greeting": ["Hi!", "Hello!", "Hey there!", "Howdy!"],
    "how_are_you": ["I'm doing well, thanks!", "Feeling good today!", "Alive and kicking! 😄"],
    "goodbye": ["Bye!", "See you later!", "Have a great day!", "Catch you soon!"],
    "thanks": ["You're welcome!", "Glad I could help!", "My pleasure!"]
}

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)

def detect_emotion(text):
    text = text.lower()
    for emotion, keywords in EMOTION_KEYWORDS.items():
        for word in keywords:
            if word in text:
                return emotion
    return "neutral"

def get_response(user_input, emotion):
    user_input = user_input.lower()

  
    if any(greet in user_input for greet in ["hi", "hello", "hey"]):
        return random.choice(RESPONSES["greeting"])

   
    elif "how are you" in user_input:
        return random.choice(RESPONSES["how_are_you"])


    elif any(goodbye in user_input for goodbye in ["bye", "exit", "quit", "goodbye"]):
        return random.choice(RESPONSES["goodbye"])


    elif any(thanks in user_input for thanks in ["thank", "thanks", "thx"]):
        return random.choice(RESPONSES["thanks"])

   
    elif emotion == "sad":
        return "I'm sorry to hear that. Want to talk about it?"
    elif emotion == "angry":
        return "Whoa, sounds like something's really frustrating you."
    elif emotion == "happy":
        return "That's awesome to hear! 😊"

    else:
        return "Interesting... Tell me more!"

def chatbot():
    memory = load_memory()
    print(Fore.CYAN + "🧠 AI Chatbot: Hello! I can remember our conversation. Type 'exit' to end.")

    while True:
        user_input = input(Fore.YELLOW + "You: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            save_memory(memory)
            print(Fore.MAGENTA + "🧠 AI Chatbot: Goodbye!")
            break

        emotion = detect_emotion(user_input)
        response = get_response(user_input, emotion)

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        memory.append({
            "timestamp": timestamp,
            "user": user_input,
            "emotion": emotion,
            "bot": response
        })

        print(Fore.GREEN + f"🧠 AI Chatbot: {response}")

if __name__ == "__main__":
