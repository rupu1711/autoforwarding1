from telethon import TelegramClient, events


# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 19634185
api_hash = 'b3b9dddf1fe26908bca459a96c89c3f1'


client = TelegramClient('AutoForward', api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
  chat=await event.get_chat()
  chat_id = event.chat_id
  print("{}{}".format(chat_id,chat))

  if chat_id == -1001289118315 or -1001532734505 or -1001303616692 or -1001342468454 or -1001184107063:
      await client.send_message(-1001529919625, event.raw_text)
  
client.start()
client.run_until_disconnected()

