# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "29223994")

API_HASH = os.environ.get("API_HASH", "f0e65bcb07e8a5b64cc82dc9a4b2bdcd")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6853506576:AAFhhUNlQoTtVBnmToYmaXZ2035AG1lGdPU") 

FORCE_SUB = os.environ.get("FORCE_SUB", "prashant_bots") 

             # Don't Remove Credit @prashant_bots
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "renamevjbot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://chakravartisamraat56831:M2ESg4dBfzKtO4Vq@cluster0.tdxx2j8.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6385957578').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
