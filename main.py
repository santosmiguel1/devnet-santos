import random
import requests

POKEMON_LIST = ["pikachu", "bulbasaur", "charizard", "greninja", "lucario"]

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print(f"Error: Pokémon '{pokemon_name}' not found.")
            return None
        else:
            print(f"Error: Received unexpected status code {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: Network connection failed - {e}")
        return None

def play_game():
    print("=== WELCOME TO WHO'S THAT POKÉMON! ===")

    answer = random.choice(POKEMON_LIST)
    data = fetch_pokemon_data(answer)
    
    if not data:
        print("Could not retrieve Pokémon data. Exiting game.")
        return

    name = data.get("name")
    height = data.get("height")
    weight = data.get("weight")
    
    print(f"\nA wild Pokémon has appeared!")
    print(f"    - Height: {height}")
    print(f"    - Weight: {weight}")
    
    attempts = 3

    while attempts > 0:
        print(f"\nAttempts remaining: {attempts}")
        guess = input("What's that Pokémon? ").strip().lower()
        
        if guess == name.lower():
            print(f"\n[+] Correct! You win! The Pokémon was {name.capitalize()}!")
            return
        else:
            print("[-] Wrong guess! Try again.")
            attempts -= 1
            
    print("\n[-] Game Over!")
    print(f"    The correct Pokémon was: {name.capitalize()}")

if __name__ == "__main__":
    play_game()
