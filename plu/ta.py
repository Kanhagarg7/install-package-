from . import kanha_cmd
from pyUltroid.fns.helper import inline_mention
@kanha_cmd(pattern="tag$",manager=True)
async def hi(event):
  reply = await event.get_reply_message()
  if reply:
    await event.respond(inline_mention(reply.sender))
  else:
    await event.respond(inline_mention(event.sender))
