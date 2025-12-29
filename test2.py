import os
import json

config_file = "config.json"

if os.path.exists(config_file):
    with open(config_file, "r") as f:
        config = json.load(f)
        print("Loaded:", config)
else:
    print("Файл не знайдено")


