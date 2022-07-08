import os
import nextcord
from dotenv import load_dotenv
from nextcord.ext import commands

bot = commands.Bot(command_prefix="-")


@bot.event
async def on_ready():
    await bot.change_presence(
        activity=nextcord.Activity(
            type=nextcord.ActivityType.playing, name="-h for help"
        )
    )

    print("Bot is online.")


@bot.command()
async def h(ctx):
    msg = """
    ```
    -------------------------------------
    -h              help command
    -ping           ping to get a pong 
    -------------------------------------
    ```
    """

    em = nextcord.Embed(title="Help", description=msg, color=0xFF0000)  # hex for red
    await ctx.send(embed=em)


@bot.command()
async def ping(ctx):
    await ctx.send("pong!")


load_dotenv()
bot.run(os.getenv("TOKEN"))
