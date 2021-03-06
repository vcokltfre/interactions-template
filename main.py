from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException
from discord_interactions import verify_key
from traceback import format_exc

from config.config import PUBKEY
from src.http import HTTP
from src.responses import respond_ephemeral

app = FastAPI(docs_url=None)

http = HTTP()

handlers = {}

@app.post("/interactions")
async def interactions(req: Request):
    body = await req.body()
    sig = req.headers["X-Signature-Ed25519"]
    ts = req.headers["X-Signature-Timestamp"]

    if not verify_key(body, sig, ts, PUBKEY):
        raise HTTPException(400)

    data = await req.json()

    if data["type"] == 1:
        return {"type":1}

    print(data)
    await http.init()

    name = data["data"]["name"]
    if name in handlers:
        try:
            return await handlers[name].call(data)
        except:
            return respond_ephemeral(f"An error occurred while processing the command:\n```py\n{format_exc(1900)}```")
    return respond_ephemeral("This command has not yet been implemented.")
