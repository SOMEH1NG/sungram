from sungram import SungramClient, SungramBot

# Example for Sungram Client (User Account)
client = SungramClient(token="your_user_token")
client.run()

# Example for Sungram Bot
bot = SungramBot(token="your_bot_token")
bot.send_message(chat_id="your_chat_id", text="Hello from Sungram!")
