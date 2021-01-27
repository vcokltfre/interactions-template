from discord_interactions import InteractionResponseType, InteractionResponseFlags

def respond_default(message: str) -> dict:
    return {
        "type": InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
        "data": {
            "content": message,
            "allowed_mentions":{
                "users": False
            }
        }
    }

def respond_ephemeral(message: str) -> dict:
    return {
        "type": InteractionResponseType.CHANNEL_MESSAGE,
        "data": {
            "content": message,
            "allowed_mentions":{
                "users": False
            },
            "flags": InteractionResponseFlags.EPHEMERAL
        }
    }