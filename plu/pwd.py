from . import eor, kanha_cmd
from os import getcwd as pwd

@kanha_cmd(pattern="pwd")
async def sshe_ed(e):
  await e.reply(f"Your directory : **{pwd()}**")