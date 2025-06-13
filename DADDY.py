import telebot
from telebot import types
import os
import random
import threading
import time

token = "7828550293:AAHQK64NpZdRSDhAhDdOo2ZOrWu-OKO8G1I"
bot = telebot.TeleBot(token)

APPROVED_USERS_FILE = "approved_users.txt"
spamming_users = {}

# Full list of abusive messages (galis)
galis = [
    "MADARCHOD TERI MAA KI CHUT ME GHUTKA KHAAKE THOOK DUNGA 🤣🤣",
    "TERE BEHEN K CHUT ME CHAKU DAAL KAR CHUT KA KHOON KAR DUGA",
    "TERI MAA K BHOSDE ME AEROPLANE PARK KARKE UDAAN BHAR DUGA ✈️🛫",
    "TERI MAA KI CHUT ME SUTLI BOMB FOD DUNGA 💣",
    "TERI MAAKI CHUT ME SCOOTER DAAL DUGA👅",  
    "TERE BHAI KI CHUT ME JHAADU LAGA DUNGA", 
    "Bhadhava Maderchod Bhosadike teri bhn ko chodu chutiya gandu scammer chut kay gulaam 😡😡🥵", 
    "Sunn Scammer Mai teri ma ko chodke apna lund chusakay aur tujhe apni jhaat chatake tujhe esa bhai dunga jo meri zindagi mai baar baar choosne ke liye taiyaar hojayenge 😂🥵🤢", 
    "teri maa ki chut me nimbu ka achar daalkr chode dalunga sale scammer kay fate hue condom ki aulad 😡🥵", 
    "jhaatu scammer teri jhant mein kerosene daal kar aag laga dunga Hijde ki kaali gaand 🥵🤢", 
    "Teri Gaand Mein Kutte Ka Lund kutiya ki paidayish scammer 😡🤮", 
    "Teri Jhaatein Kaat Kar Tere Mooh Par Laga Kar Unki scam French Beard Bana Doonga", 
    "Chullu Bhar Muth Mein Doob Mar bhaadu scammer Chut Ke Pasine Main apni kaak gand chuda bhosdike", 
    "kaali gand kay fatey hue lund jhaatu scammer kaas ush din Tera baap condom use kar leta betichod 🤬🤬", 
    "scammer hathi kay lund ka bhsoda bna kar teri kaali gand mai de dunga chhipakali ki choot jesi sakal kay 🤬🖕", 
    "Randi ki Najais lode tere jese chutiya scammer randi k baccho ko bachpan mai maar dena chiye", 
    "Chipkali ki bhigi chut Choot kay baal Chipkali ke jhaat ke paseene",
    "Gote Kitne Bhi Badey Ho, Lund Ke Niche Hi Rehtein Hain",
    "chutiye behenchod lauda madarchod gaandu bhosadikey",
    "Chullu Bhar Muth Mein Doob Mar Kaali Chut Ke Safed Jhaat",
    "chut kay baal nipple ki dhaar teri gaand mai Road roller de dunga 🖕🤬",
    "Teri Gaand Mein Kutte Ka Lund 🖕 Teri Jhaatein Kaat Kar Tere Mooh Par Laga Kar Unki French Beard Bana Doonga!",
    "Phatele Nirodh Ke Natije! 😂😂",
    "Teri maa ki choot gand kay tatto teri maa ka bhosda karke uski gaand mai ping pong kar dunga",
    "GAND KII DHAAR BHOSDIKE FATEE HUE CONDOM KI NAAJAIS PAIDAISH",
    "Teri ma ka bhosda sale maderchod ki aulad 🤬",
    "madarchod chutmarke teri tatti jesi shakl pe pad dunga bhen k lode chutiye",
    "maa k lode tere jese randi k baccho ko bachpan mai maar dena chiye",
    "TERA BAAP JOHNY SINS CIRCUS KAY BHOSDE JOKER KI CHIDAAS 14 LUND KI DHAAR TERI MUMMY KI CHUT MAI 200 INCH KA LUND",
    "teri bhn ko chodu 🥵 scam kay Paiso se apni mummy kay lie condom khareed lie jhaatu 😂",
    "🖕Scammer maderchod teri maa ka bhosda 🤮🤢 sale 2 koodi kay lund🤬🤬",
    "TARI MAA KI CHUT ME NAARIYAL PHOR DUNGA 🔋 🔥", 
    "TERI MAA KI CHUT MEI C++ STRING ENCRYPTION LAGA DUNGA",  
    "TERI VAHEEN KO HORLICKS PEELAUNGA MADARCHOD😚",
    "TERI MAA KO KOLKATA VAALE JITU BHAIYA KA LUND MUBARAK 🤩🤩",  
    "TUJHE DEKH KE TERI RANDI BAHEN PE TARAS ATA HAI MUJHE BAHEN KE LODEEEE 👿💥🤩🔥",  
    "TERI MAA KI CHUT ME NAARIYAL PHOR DUNGA 🔥"
]

# Load approved users from file
def load_approved_users():
    if os.path.exists(APPROVED_USERS_FILE):
        with open(APPROVED_USERS_FILE, "r") as f:
            return [int(line.strip()) for line in f if line.strip().isdigit()]
    return []

# Save approved users to file
def save_approved_users():
    with open(APPROVED_USERS_FILE, "w") as f:
        for user_id in approved_users:
            f.write(f"{user_id}\n")

approved_users = load_approved_users()
admins = [8179218740]  # Replace with your admin user ID

# Inline button for owner
my = types.InlineKeyboardButton(text="Owner", url="t.me/team_nh")
xx = types.InlineKeyboardMarkup()
xx.add(my)

@bot.message_handler(commands=["start"])
def welcome(message):
    bot.reply_to(message, "Welcome To Gali Spam Bot 😈", reply_markup=xx)

@bot.message_handler(commands=["approve"])
def approve_user(message):
    if message.from_user.id not in admins:
        bot.reply_to(message, "Only Admins can approve users!")
        return
    
    msg = message.text.split()
    if len(msg) != 2 or not msg[1].isdigit():
        bot.reply_to(message, "Usage: /approve <user_id>")
        return

    user_id = int(msg[1])
    if user_id not in approved_users:
        approved_users.append(user_id)
        save_approved_users()
        bot.reply_to(message, f"User {user_id} approved!")
    else:
        bot.reply_to(message, f"User {user_id} is already approved.")

@bot.message_handler(commands=["fuck"])
def start_spam(message):
    if message.from_user.id not in approved_users:
        bot.reply_to(message, "You are not approved to use this bot!")
        return

    msg = message.text.split()
    if len(msg) != 2:
        bot.reply_to(message, "Usage: /fuck <username>")
        return

    target_username = msg[1]
    target_user = bot.get_chat_member(message.chat.id, target_username)

    if target_user is None:
        bot.reply_to(message, f"User {target_username} not found!")
        return

    if target_username in spamming_users:
        bot.reply_to(message, f"Already spamming {target_username}!")
        return

    def spam():
        try:
            while target_user:
                msg = random.choice(galis)
                bot.send_message(target_username, msg)
                time.sleep(2)  # Delay between each message
        except Exception as e:
            bot.send_message(message.chat.id, f"Error: {e}")
            spamming_users.pop(target_username, None)

    spamming_thread = threading.Thread(target=spam)
    spamming_thread.start()
    spamming_users[target_username] = spamming_thread
    bot.reply_to(message, f"Started spamming {target_username}")

@bot.message_handler(commands=["stop"])
def stop_spamming(message):
    if message.from_user.id not in approved_users:
        bot.reply_to(message, "You are not approved to stop spamming!")
        return

    msg = message.text.split()
    if len(msg) != 2:
        bot.reply_to(message, "Usage: /stop <username>")
        return

    target_username = msg[1]
    if target_username not in spamming_users:
        bot.reply_to(message, f"Not spamming {target_username} currently!")
        return

    spamming_users[target_username].stop()
    del spamming_users[target_username]
    bot.reply_to(message, f"Stopped spamming {target_username}")

bot.polling()