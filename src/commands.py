import re

import channel_logger
from utils import serialize_id, extract_id

_COMMAND_PREFIX = "$dl"

def is_command(message):
    return message.content.startswith(_COMMAND_PREFIX)


async def execute(message):

    COMMANDS = {
        "track" : _track,
        "untrack" : _untrack,
        "list" : _list_channels,
        "help" : _help
    }

    if message.author != message.guild.owner:
        await message.channel.send("Only the owner of the server can run commands")
        return

    if not is_command(message):
        print(f"'{message.content}' is not a command!")
    
    print(f"Executing command '{message.content}'")

    command_parts = message.content.split(" ")
    
    cmd = command_parts[1]
    args = command_parts[2:]

    if cmd in COMMANDS:
        await COMMANDS[cmd](args, message)
    else:
        await message.channel.send(f"'{cmd}' is an unknown command!")


async def _help(args, message):
    await message.channel.send(f'''
    Dislogger:
      - {_COMMAND_PREFIX} <command> [args]
    
    Commands:
      - track <channel> : Marks a channel as to track
      - untrack <channel> : Unmarks a previously tracked channel
      - list : Lists all channels that are being tracked
      - help : Sends this help message
    ''')


async def _track(args, message):
    if len(args) != 1:
        await message.channel.send(f" Wrong number of arguments for track {args}. Usage: $dcl track <channel>")
    
    channel_id = extract_id(args[0])
    channel = message.guild.get_channel(channel_id)

    channel_logger.track(channel)
    await message.channel.send(f"Sucessfully tracking {args[0]}")


async def _untrack(args, message):
    if len(args) != 1:
        await message.channel.send(f"Wrong number of arguments for untrack {args}. Usage: $dcl untrack <channel>")
    
    channel_id = extract_id(args[0])
    channel = message.guild.get_channel(channel_id)

    result = channel_logger.untrack(channel)
    if result:
        await message.channel.send(f"Sucessfully untracking {args[0]}")
    else:
        await message.channel.send(f"Channel {args[0]} was not being tracked")


async def _list_channels(args, message):
    if len(args) != 0:
        await message.channel.send(f"Wrong number of arguments for list {args}. Usage: $dcl list")
    
    server = message.guild
    tracked_channels = channel_logger.list_channels(server)

    reply = [f"Tracked channels:\n"]
    for channel_id in tracked_channels:
        reply.append(f"{serialize_id(channel_id)}\n")
    
    await message.channel.send("".join(reply))