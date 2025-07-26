import webbrowser

RECIPES = {
    "pasta": "Boil water, add salt, cook pasta 8-10 mins",
    "omelette": "Whisk 2 eggs, cook in butter, fold when set",
    "salad": "Mix greens, cherry tomatoes, cucumber. Add dressing"
}

def chef_remy():
    print("Chef Remy: Bonjour! Hungry? I'll help you cook!")
    
    while True:
        print("\nWhat would you like to make? (pasta/omelette/salad) or say 'exit'")
        choice = input("You: ").lower()
        
        if choice == "exit":
            print("Chef Remy: Au revoir! May your kitchen always be joyful!")
            break
            
        if choice in RECIPES:
            print(f"Chef Remy: For {choice}: {RECIPES[choice]}")
            webbrowser.open(f"https://www.youtube.com/results?search_query={choice}+recipe")
        else:
            print("Chef Remy: Sacre bleu! Try one of my specialties first!")
