from aiohttp import ClientSession

from config.config import TOKEN

BASE = "https://discord.com/api/v8"


class HTTP:
    def __init__(self):
        self.sess = ClientSession(headers={'Authorization': f'Bot {TOKEN}'})

    async def init(self):
        if self.sess.closed:
            self.sess = ClientSession(headers={'Authorization': f'Bot {TOKEN}'})

    async def send_message(self, channel: str, message: str, allowed_mentions: dict = {}):
        async with self.sess.post(BASE + f"/channels/{channel}/messages", json={"content":message, **allowed_mentions}) as resp:
            return await resp.json()
