import discord
from discord.ext import commands
import random

token = 'OTcyMTUwMjc1NjQzMTUwMzY2.G37Qh6.mcYwzW7ImdFEFNrbe7FI8gtvaxcCttd_u7JrnY'
bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")


@bot.command()
async def os(ctx):
    await ctx.send("3mna ♥")


@bot.command()
async def اشتم(ctx, member: discord.Member):

    if member.mention == "<@716301044514029619>":
        await ctx.send("مقدرش 🥹")

    elif member.mention == "<@654371760476782592>":
        await ctx.send("", file=discord.File('lol.jpg'))
        await ctx.send(f"🏹 سهم فتيز الصيوحه ")

    elif member.mention == "<@972150275643150366>":
        await ctx.send(f" ينفع يعنى ؟ ")

    elif member.mention == "<@531920898488270848>":
        wali = ['العم وليد', 'العم لولو']
        await ctx.send("", file=discord.File('lol.jpg'))
        await ctx.send(f"🏹 سهم فتيز {random.choice(wali)}")

    elif member.mention == "<@581797646566424586>":
        await ctx.send("عيب vip member 💵")

    else:
        await ctx.send("", file=discord.File('lol.jpg'))
        await ctx.send(f"🏹 سهم فتيز {member.mention} ")


@ bot.command()
async def  بوس (ctx, member: discord.Member):
    await ctx.send(f"https://cdn.discordapp.com/emojis/710014175904137267.gif?v=1")


bot.run(token)
