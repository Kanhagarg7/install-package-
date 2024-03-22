import requests as st
from . import eor, kanha_cmd, get_string, bash

@kanha_cmd(pattern="log( (.*)|$)")
async def sse_ed(e):
  x = e.pattern_match.group(1).strip()
  y = await e.eor(get_string("com_1")) 
  r = st.get(f"https://raganork-network.vercel.app/api/logo/calligraphy?style=1&text={x}")

  with open("new.jpg", "wb") as a:
    a.write(r.content)
  await e.reply(file=f"new.jpg")
