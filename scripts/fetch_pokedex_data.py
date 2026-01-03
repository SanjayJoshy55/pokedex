import pandas as pd
import pokebase as pb
import requests
import json
import time

def fetch_hoenn_data():
    print("Fetching Hoenn Pokedex...")
    # Hoenn Pokedex ID is 4 (original) or 15 (ORAS - Updated Hoenn). 
    # using 'hoenn' usually maps to the generation III dex, let's use the updated one for ORAS if possible, or just 'hoenn' (id 4).
    # ORAS pokedex is id 15 "updated-hoenn".
    try:
        dex = pb.pokedex('updated-hoenn')
    except:
        print("Could not fetch 'updated-hoenn', trying 'hoenn'...")
        dex = pb.pokedex('hoenn')

    data = []
    
    print(f"Found {len(dex.pokemon_entries)} Pokemon. Processing...")
    
    # Limit to first 20 for quick testing if you want, but here we loop all
    # set limit=None to fetch all
    count = 0
    limit = None 
    
    for entry in dex.pokemon_entries:
        if limit and count >= limit:
            break
            
        p = entry.pokemon_species
        # We need the actual pokemon object for types and sprites
        try:
            # Get pokemon details (using the species name to get the default variety)
            # Note: pokebase might lazy load.
            pk_data = pb.pokemon(p.name)
            
            # Types
            types = [t.type.name for t in pk_data.types]
            
            # Sprite
            sprite_url = pk_data.sprites.front_default
            
            # Location (This mimics specific ORAS locations)
            # This is complex to fetch via API for every single one efficiently 
            # so we might placeholder it or fetch strict encounter data if needed.
            # simpler: just use a placeholder or generic "Hoenn" for now to save time
            location = "Hoenn Region" 
            
            data.append({
                "id": pk_data.id,
                "name": p.name.title(),
                "types": ", ".join(types),
                "sprite_url": sprite_url,
                "location": location
            })
            
            count += 1
            if count % 10 == 0:
                print(f"Processed {count}...")
                
        except Exception as e:
            print(f"Error processing {p.name}: {e}")
            continue

    df = pd.DataFrame(data)
    df.to_csv('data/hoenn_pokedex.csv', index=False)
    print("Saved to data/hoenn_pokedex.csv")

if __name__ == "__main__":
    fetch_hoenn_data()
