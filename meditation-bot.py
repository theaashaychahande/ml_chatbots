import random
import time

def zen_bot():
    print("Peaceful Zen: Welcome, aashay. I sense you need calm. Breathe with me...")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input in ["exit", "goodbye"]:
            print("Peaceful Zen: May your path be illuminated. Return when you need stillness.")
            break
            
        responses = [
            "Notice how your breath flows like a gentle river...",
            "In this moment, there is only now. Observe without judgment.",
            f"Ah, '{user_input}'... interesting. Let it pass like a cloud.",
            "Sit comfortably. Count your breaths with me: 1... 2... 3...",
            "The mind is restless. Don't chase thoughts - let them go."
        ]
        
        print("Peaceful Zen:", random.choice(responses))
        time.sleep(1.5)  
