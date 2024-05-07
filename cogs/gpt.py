import discord
from discord.ext import commands

class gpt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author != self.bot.user:  
            await message.channel.send("Hi!")


def setup(bot):
    bot.add_cog(gpt(bot))