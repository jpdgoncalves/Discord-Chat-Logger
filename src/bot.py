import sys
import discord

import channel_logger
import commands

class MyClient(discord.Client):

    async def on_ready(self):
        print(f'Logged on as {self.user}!')
    
    async def on_message(self, message):
        print(f'Message from {message.author} at {message.channel.name}-{message.channel.id}: {message.content}')
        if commands.is_command(message):
            await commands.execute(message)
        elif message.author != self.user:
            channel_logger.log(message)

if len(sys.argv) != 2:
    print("Usage: python ./src/bot.py <BOT_AUTH_TOKEN>")
    quit()

client = MyClient()
client.run(sys.argv[1])