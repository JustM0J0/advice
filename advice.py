import json
import requests


advice = requests.get("https://api.adviceslip.com/advice")

advice = advice.json()

print(advice['slip']['advice'])
