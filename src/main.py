#------------------------------------
# Kommen zwei Stumme in die Bar. Sagt der eine:"",Sagt der andere:"".
#------------------------------------

from twitchio.ext import commands
from dotenv import load_dotenv
import os
from termcolor import colored
import random
from datetime import datetime
from ascii_art import *

load_dotenv("secret.env")
Twitch_token = os.getenv("TOKEN")
count = 0
channel = None

def main():
    os.system("clear")
    print(random.choice(ascii_list))
    print(colored("Works offline and online.", "yellow"))
    print(colored("Press ctrl + c to quit.", "red"))
    channel = input(colored("Type a Channel (Streamer) name: ","green"))
    return channel

channel = main()

class Chat(commands.Bot):
    def __init__(self,**kwargs):
        super().__init__(token=Twitch_token,prefix=None, initial_channels=[channel],**kwargs)


    async def event_ready(self):
        print(colored(f"Bot ist bereit und verbunden mit {self.nick} im Kanal {channel}", "yellow"))

    async def event_message(self, message):
        global count
        count += 1
        # print(count,"minus char_counter ")
        farben_choice = ["red", "green", "cyan", "blue", "magenta"]
        self.farben = random.choice(farben_choice)

        if message.author.name == "nightbot":
            self.farben = "white"
        if message.author.name == "streamelements":
            self.farben = "white"

        self.date_now = datetime.now().strftime("%H:%M")
        color_message = colored(f"{message.author.name}", self.farben)
        print(f"[{self.date_now}] {color_message}: {message.content}")



if __name__ == "__main__":
    try:
        bot = Chat()
        bot.run()
    except Exception as e:
        print("Please create a secret.env file with your ACCESS TOKEN. Like TOKEN=1234")
        print(e)

print(colored(f"\nMenge an Chat Nachrichten: {count}", "green"))

