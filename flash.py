from pyrogram import Client, Filters
import time

app = Client("account")


@app.on_message()
def echo(client, message):
	text = message.text
	chat_id = message.chat.id
	i = 1
	if text:
		print("Flashing")
		while i < 6:
			time.sleep(0.001)
			#chat_id = 1072101036
			app.send_message(chat_id,"Spam Bot \nDeveloped By realDev \n Unban To Stop Spamming")


app.run()  # Automatically start() and idle()