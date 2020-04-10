import discord

import channel_logger
import commands

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author} at {0.channel.name}-{0.channel.id}: {0.content}'.format(message))
        if commands.is_command(message):
            await commands.execute(message)
        elif message.author != self.user:
            channel_logger.log(message)

client = MyClient()
client.run('YOUR TOKEN HERE')