import discord  

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTQ4ODg5NDE5MDY5NDgyNTk4NA.GmH0Br.SF4Rs3hS0lIHsAaEr_4qGQbYFBq_zaxX8mbFL4') # Replace with your own token.