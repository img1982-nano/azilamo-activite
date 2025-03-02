
from pypresence import Presence
import time


client_id = "1345466488781275156"  # Enter your Application ID here.
RPC = Presence(client_id=client_id)
RPC.connect()


RPC.update(
            state="何かしら中",
            details="Work",
            large_image=("https://media1.tenor.com/m/8wBCqZH60U8AAAAC/computer-cat.gif"), 
            large_text="Work",
            small_image=("https://images.emojiterra.com/google/noto-emoji/unicode-16.0/color/share/1f914.jpg"), small_text="Work",
            buttons=[{"label": "Mysite()", "url": "https://azilamo.com"}]
)

while True:
    time.sleep(1)