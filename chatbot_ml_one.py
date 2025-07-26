import json
import os
import datetime
import random
from colorama import Fore, Style, init
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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

def preprocess(text):
    return ' '.join(
        text.lower()
             .replace("?", "").replace("!", "").replace(".", "")
             .replace(",", "").replace(":", "").replace(";", "")
             .split()
    )

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

def get_response(user_input, memory):
    user_input = user_input.lower()

  
    if any(greet in user_input for greet in ["hi", "hello", "hey"]):
        return random.choice(RESPONSES["greeting"])

 
    elif "how are you" in user_input:
        return random.choice(RESPONSES["how_are_you"])


    elif any(goodbye in user_input for goodbye in ["bye", "exit", "quit", "goodbye"]):
        return random.choice(RESPONSES["goodbye"])

  
    elif any(thanks in user_input for thanks in ["thank", "thanks", "thx"]):
        return random.choice(RESPONSES["thanks"])


    elif detect_emotion(user_input) == "sad":
        return "I'm sorry to hear that. Want to talk about it?"
    elif detect_emotion(user_input) == "angry":
        return "Whoa, sounds like something's really frustrating you."
    elif detect_emotion(user_input) == "happy":
        return "That's awesome to hear! 😊"
    

    else:
        return find_similar_response(user_input, memory)

def find_similar_response(user_input, memory):
    if len(memory) < 2:
        return "Interesting... Tell me more!"

    cleaned_input = preprocess(user_input)
   
    all_questions = cleaned_questions + [cleaned_input]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_questions)

    similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    most_similar_idx = similarities.argmax()


    if similarities[0][most_similar_idx] > 0.3: 
        return memory[most_similar_idx]["bot"]
    else:
        return "That's new to me! Tell me more."
def chatbot():
    memory = load_memory()
    print(Fore.CYAN + "🧠 AI Chatbot (with ML): Hello! I learn from our conversations. Type 'exit' to end.")

    while True:
        user_input = input(Fore.YELLOW + "You: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            save_memory(memory)
            print(Fore.MAGENTA + "🧠 AI Chatbot: Goodbye!")
            break

        response = get_response(user_input, memory)
        emotion = detect_emotion(user_input)

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        memory.append({
            "timestamp": timestamp,
            "user": user_input,
            "emotion": emotion,
            "bot": response
        })

        print(Fore.GREEN + f"🧠 AI Chatbot: {response}")

if __name__ == "__main__":

