import discord 
import responses


async def send_message(message,user_message,is_private):
  try:
    response = responses.handle_response(user_message)
    await message.author.send(response) if is_private else await message.channel.send(response)
  except Exception as e:
    print(e)
    
    
def run_discord_bot():
  TOKEN="MTA1NDczMDg1NTIwNzE0NTYxMw.GTGaKj.H0leS5oTlaGx2StYNGYkvU4nen-zIxadxrpXKU"
  client = discord.Client()
  @client.event
  async def on_ready():
    print(f'{client.user} is now running')
  
  
  @client.event
  async def on_message(message):
    if message.author == client.user:
      return
      
    username= str(message.author)
    user_message = str(message.content)
    channel=str(message.channel)

    print(f"{username} said: '{user_message}' ({channel})")
    print(user_message)
    
    if user_message[0] == "~":
      user_message = user_message[1:]
      await send_message(message,user_message,is_private=True)
    else:
      await send_message(message,user_message,is_private=False)
    

  client.run(TOKEN)
  
