import json
import os

DATA_FILE = "finance_data.json"

def load_data():
    """Loads data from a JSON file, handling errors."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            return {"categories": [], "transactions": []}  # Reset if file is corrupted
    return {"categories": [], "transactions": []}

def save_data(data):
    """Saves data to a JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

data = load_data()
