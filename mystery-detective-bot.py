clues = []

def noir_bot():
    print("Detective Noir: *lights cigarette* Another rainy night. What's your case?")
    
    while True:
        print("\n1. Add clue\n2. Review clues\n3. Solve case\n4. Exit")
        choice = input("You: ")
        
        if choice == "4":
            print("Detective Noir: The city sleeps... but crime never does.")
            break
            
        if choice == "1":
            clue = input("Describe the clue: ")
            clues.append(clue)
            print("*scribbles in notebook* Added.")
        elif choice == "2":
            print("Collected clues:", ", ".join(clues) if clues else "None yet...")
        elif choice == "3":
            print("Detective Noir: My theory?", "The butler did it!" if clues else "Need more clues, kid.")
        else:
            print("*grunts* Stick to the numbers, see?")
