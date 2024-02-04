import discord
from discord.ext import commands
from project import gen_pass, sampah_organik, sampah_anorganik
import random, os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
    
@bot.command()
async def password(ctx):
    await ctx.send('BERIKUT PASSWORD UNTUKMU: ')
    await ctx.send(gen_pass())

@bot.command()
async def cats(ctx):
    gambar = random.choice(os.listdir('cats'))
    with open(f'cats/{gambar}', 'rb') as f:
        pic = discord.File(f)

    await ctx.send(file=pic)

@bot.command()
async def organik(ctx):
    sampah = ""
    for i in sampah_organik:
        i = i+'\n'
        sampah += i
    await ctx.send('berikut daftar sampah organik: ')
    await ctx.send(sampah)

@bot.command()
async def anorganik(ctx):
    sampah = ""
    for i in sampah_anorganik:
        i = i+'\n'
        sampah += i
    await ctx.send('berikut daftar sampah anorganik: ')
    await ctx.send(sampah)


bot.run("isi token kamu")