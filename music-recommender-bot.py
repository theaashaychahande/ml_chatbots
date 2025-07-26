import pywhatkit

def music_bot():
    print("Grammy: Hey sugar! Let's find you the perfect tune!")
    
    while True:
        mood = input("\nHow you feeling? (happy/sad/angry/chill) or 'stop': ")
        
        if mood == "stop":
            print("Grammy: Keep that music in your soul, darlin'!")
            break
            
        songs = {
            "happy": ["Uptown Funk", "Dancing Queen", "Happy"],
            "sad": ["Someone Like You", "Hurt", "Nothing Compares 2 U"],
            "angry": ["Break Stuff", "Killing in the Name", "Sabotage"],
            "chill": ["Redbone", "Dreams", "Sunflower"]
        }
        
        if mood in songs:
            print(f"Grammy: Try these: {', '.join(songs[mood])}")
            pywhatkit.playonyt(random.choice(songs[mood]))
        else:
            print("Grammy: Hmm... let's just play some Motown!")
