import os
import discord
import aiohttp
from termcolor import colored
from discord.ext import commands, events

token = 

COGS = [
    'leaderboard',
]

intents = discord.Intents.default()
intents.message_content = True

class Bot(commands.Bot, events.EventsMixin):
    def __init__(self, **kwargs):
        
        super().__init__(
            **kwargs,
            command_prefix="?", slash_commands=True, intents=intents,
            allowed_mentions=discord.AllowedMentions(everyone=False, roles=True, replied_user=False),
            case_insensitive=False,
        )

        self.remove_command("help")

    def cog_load(self):
        print(colored('[INFO] ', 'grey'), colored(f'Loaded {self.name}', 'cyan'))

    def cog_unload(self):
        print(colored('[INFO] ', 'grey'), colored(f'Unloaded {self.name}', 'cyan'))
        
    async def setup_hook(self):
        self.http_session = aiohttp.ClientSession()
        await self.load_extension("jishaku")
        for i in COGS:
            await self.load_extension(f"cogs.{i}")

if __name__ == "__main__":
    bot = Bot()
    bot.run(token)
