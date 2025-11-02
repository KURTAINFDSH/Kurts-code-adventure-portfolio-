import json
import os

# Correct path inside accessible storage
path = "/storage/emulated/0/CODES/data"
os.makedirs(path, exist_ok=True)

# File path
file_path = os.path.join(path, "player.json")  # lowercase "player.json"

# Player data
player_data = {"name": "kurt", "wins": 1, "scores": 1}

# Save to JSON
with open(file_path, "w") as file:
    json.dump(player_data, file, indent=4)

# Load from JSON
with open(file_path, "r") as file:
    loaded_data = json.load(file)

print(loaded_data["name"])   # kurt
print(loaded_data["wins"])   # 1