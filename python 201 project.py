# https://pokeapi.co/api/v2/pokemon/

import requests



while True:
    pokemon_name = input("What pokemon you want to know?")
    req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    

    if req.status_code == 200:

        pokemon = req.json()

        print(f"\tName:\t{pokemon['name'].upper()}\n")
        

        typeOf = pokemon['types']

        for index, element in enumerate(typeOf):
            if 'type' in element and 'name' in element['type']:
                name = element['type']['name'].capitalize()
                if len(typeOf) > 1:
                    print(f"\tType {index + 1}:\t\t{name}")
                    
                else:
                    print(f"\tType :\t\t{name}")
                    

        print(' ')
                

        abilityOf = pokemon['abilities']
        
        for index, element in enumerate(abilityOf):
            if 'ability' in element and 'name' in element['ability']:
                name = element['ability']['name'].capitalize()
                if len(abilityOf) > 1:
                    print(f"\tAbility {index + 1}:\t\t{name}")
                    
                else:
                    print(f"\tAbility :\t\t{name}")
                    

        print(' ')

        moveOf = pokemon['moves']

        for index, element in enumerate(moveOf):
            if 'move' in element and 'name' in element['move']:
                name = element['move']['name'].capitalize()
                if len(moveOf) > 1:
                    print(f"\tMove {index + 1}:\t\t{name}")
                    
                else:
                    print(f"\tMove :\t\t{name}")

        print(' ')
                    

                
    else:
        print("Sorry, there is no Pokemon register in that name")
        

    continue_search = input("Wanna try again? y/n: ")
    if continue_search.lower() == 'n':
        print("Okay, Thank You")
        break
    elif continue_search.lower() == 'y':
        continue
    else:
        print("You mistype , you will exit now. Thank you")
        break