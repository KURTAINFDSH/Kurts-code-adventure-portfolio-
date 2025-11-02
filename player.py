import os
import json

# Use Pydroid internal storage (this works without extra permission)
path = "/data/data/ru.iiec.pydroid3/files/Gamelib/Playerdata"
os.makedirs(path, exist_ok=True)

file_path = os.path.join(path, "player.json")

player_data = {"name": "kurt", "wins": 1, "scores": 1}

# Save
with open(file_path, "w") as file:
    json.dump(player_data, file, indent=4)

# Load
with open(file_path, "r") as file:
    loaded_data = json.load(file)

print(loaded_data)