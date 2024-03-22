from . import kanha_cmd, get_string
@kanha_cmd(pattern="cp",manager=True)
async def hi(event):
  reply = await event.get_reply_message()
  a = await event.edit(f"`{reply.text}`")
  try:
    await event.respond(f"{a}")
  except:
    await event.respond(f"`{reply.text}`")