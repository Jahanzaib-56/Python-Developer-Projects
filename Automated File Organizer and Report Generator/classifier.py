import json
import logging
from pathlib import Path

def load_rules(config_path: str = 'config.json') -> dict:
    try:
        with open('config.json', 'r') as f:
            rules = json.load(f)

        for cat in rules:
            rules[cat] = [ext.lower() for ext in rules[cat]]

        logging.info("Rules for Classification loaded successfully")

        return rules
    
    except Exception as e:
        logging.error("Failed to load config file")
        return {}
    
def file_classifier(file_meta: dict, rules: dict) -> dict:

    extension = file_meta.get("extension", "").lower()

    for category, extensions in rules.items():
        if extension in extensions:
            file_meta['category'] = category
            return file_meta
        
    file_meta['category'] = 'Others'
    return file_meta