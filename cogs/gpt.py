import discord
from discord.ext import commands

## Whitelisted Servers 
whitelistedServers=[1053879369011044444]

class gpt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.author != self.bot.user:  
            print(ctx)

    @commands.slash_command(guild_ids = whitelistedServers,description="Ping!")
    async def ping(self, ctx):
        await ctx.respond(f"Pong!({self.bot.latency} ms)")

    @commands.slash_command(guild_ids = whitelistedServers, description="Ask GPT a Question!")
    async def ask(self,message):
        print("Hello World!")

    


def setup(bot):
    bot.add_cog(gpt(bot))