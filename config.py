import os
from dotenv import load_dotenv

load_dotenv()

# Основной токен
BOT_TOKEN = os.getenv("BOT_TOKEN")
MACAROON_PHOTO = os.getenv('MACAROON_PHOTO')
BROWNIE_PHOTO = os.getenv('BROWNIE_PHOTO')


working_hours = {'weekday': {'from': 8, 'to': 20},
                 'weekend': {'from': 9, 'to': 20}}
admin_id = int(os.getenv('MY_ID'))
admin_chat_id = int(os.getenv('ADMIN_CHAT_ID'))
IP_WHITELIST = [int(os.getenv('MY_ID')), int(os.getenv('EVGEN_ID')), int(os.getenv('ALEXANDR_ID'))]
DB_LINK = os.getenv('mongodb://localhost:27017')
