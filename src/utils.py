import re

def extract_id(channel_id):
    channel_id = re.sub(
        "<|#|>",
        "",
        channel_id
    )
    return int(channel_id)


def serialize_id(channel_id):
    return f"<#{channel_id}>"

def escape_non_alphanumeric(string):
    return re.sub(
        "[^0-9a-zA-Z]+",
        "",
        string
    )