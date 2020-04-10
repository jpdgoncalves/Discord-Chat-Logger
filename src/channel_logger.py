import os
import json
import pprint

from utils import escape_non_alphanumeric, escape_non_ascii

'''
{
    <server_id> : [<channel_id>]
}
'''
_SERVERS_FILE = "server.json"
_LOG_DIR = "logs"
tracked_servers = {}

def track(channel):
    server = channel.guild
    server_id = str(server.id)
    channel_id = str(channel.id)

    if not server_id in tracked_servers:
        tracked_servers[server_id] = []
    
    tracked_servers[server_id].append(channel_id)
    _save_servers()


def untrack(channel):
    server = channel.guild
    server_id = str(server.id)
    channel_id = str(channel.id)

    if not server_id in tracked_servers:
        return False
    
    if not channel_id in tracked_servers[server_id]:
        return False
    
    tracked_servers[server_id].remove(channel_id)
    _save_servers()
    
    return True
    

def list_channels(server):
    server_id = str(server.id)
    
    if not server_id in tracked_servers:
        return []
    
    return tracked_servers[server_id]


def log(message):
    server = message.guild
    channel = message.channel
    server_id = str(server.id)
    channel_id = str(channel.id)
    server_name = escape_non_alphanumeric(server.name)
    channel_name = escape_non_alphanumeric(channel.name)
    author_name = escape_non_ascii(message.author.display_name)
    message_creation_time = message.created_at.ctime()
    message_content = escape_non_ascii(message.content)

    if server_id in tracked_servers and channel_id in tracked_servers[server_id]:
        content = f"<{author_name} {message_creation_time}>\n"
        content += f"{message_content}\n\n"
        print(f"Logging:\n {content}")

        with open(f"{_LOG_DIR}/{server_name}-{channel_name}-{channel_id}.txt", "a") as log_file:
            log_file.write(content)
    

def _save_servers():
    print(f"Saving to {_SERVERS_FILE}:")
    pprint.pprint(tracked_servers)
    with open(_SERVERS_FILE, "w") as server_file:
        server_file.write(json.dumps(tracked_servers))


def _load_servers():
    global tracked_servers

    print(f"Loading {_SERVERS_FILE}")

    with open(_SERVERS_FILE, "r") as server_file:
        tracked_servers = json.loads(server_file.read())
    
    print(f"Finished loading {_SERVERS_FILE}:")
    pprint.pprint(tracked_servers)


if not os.path.isfile(_SERVERS_FILE):
    print(f"{_SERVERS_FILE} not found. Creating new one.")
    with open(_SERVERS_FILE, "w") as server_file:
        server_file.write("{}")

if not os.path.isdir(_LOG_DIR):
    os.mkdir(_LOG_DIR)

_load_servers()