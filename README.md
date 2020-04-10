# Discord Chat Logger
A small bot made to log messages in a chat into files. The filenames are formated as (server_name)-(channel_name)-(channel_id).txt

## Installation
Clone this repository or download its zipfile and uncompresse it

Install [Python](https://www.python.org/downloads/) if you don't have it. Make sure you have the pip and path options ticked.

In case you already had python and you don't have pip download [get-pip.py](https://bootstrap.pypa.io/get-pip.py) and run it in the console.
```bash
python get-pip.py
```
Navigate to the folder where the bot is and install the requirements in requirements.txt
```bash
pip install -r requirements.txt
```

## Run the Bot
To run the bot navigate to the folder where the bot files are and run:
```bash
python ./src/bot.py
```

To stop the bot use `CTRL+C`

## Commands
`$dl track <channel>`
Marks the specified channel for tracking.

`$dl untrack <channel>`
Unmarks the specified channel for tracking.

`$dl list`
Lists channels being tracked in a server.

`$dl help`
Shows all the possible commands for the bot.