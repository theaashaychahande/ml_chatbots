import requests

def space_bot():
    print("Cosmo: Greetings Earthling! Let's explore the cosmos together!")
    
    while True:
        print("\nAsk about: planets, stars, ISS or say 'return'")
        query = input("You: ").lower()
        
        if query == "return":
            print("Cosmo: Safe travels through the cosmic void!")
            break
            
        if query == "iss":
            response = requests.get("http://api.open-notify.org/iss-now.json")
            data = response.json()
            print(f"ISS is currently at: {data['iss_position']}")
        elif query == "planets":
            print("Cosmo: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune")
        else:
            print("Cosmo: Did you know a neutron star is so dense, one teaspoon weighs a billion tons?")
