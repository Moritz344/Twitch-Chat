from twitchio.ext import commands
from dotenv import load_dotenv
import os
from termcolor import colored
import random
from datetime import datetime

load_dotenv("secret.env")
Twitch_token = os.getenv("TOKEN")
channel = "ThePrimeagen"



class Chat(commands.Bot):
    def __init__(self):
        super().__init__(token=Twitch_token,prefix="!",initial_channels=[channel])

    async def event_ready(self):
        print(colored(f"Bot ist bereit und verbunden mit {self.nick} im Kanal {channel}","yellow")) # Bot ist aktiv
        

    async def event_message(self,message): # prüft Nachrichten
        if message.author.name.lower() == self.nick.lower():
            return
        farben_choice = ["red","green","cyan","blue","magenta"]
        self.farben = random.choice(farben_choice)

        if message.author.name == "nightbot":
            self.farben = "white"
        if message.author.name == "streamelements":
            self.farben = "white"
            
        self.date_now = datetime.now()strftime("%H:%M")
        color_message = colored(f"{message.author.name}",self.farben)
        print(f"[{self.date_now}]{color_message}: {message.content}")

if __name__ == "__main__":
    bot = Chat()
    bot.run()


