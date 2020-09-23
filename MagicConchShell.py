import discord
from discord.ext import commands, tasks
import random
import time

client = commands.Bot(command_prefix='$')

# Have to change this path for Linux
# token = open(r'.\token.txt', 'r').read()
token = open(r'/home/ubuntu/Discord/MagicConchShell/token.txt', 'r').read()

status_list = [
    'beep boop beep',
    'bee boo boo bop boo boo bop',
    'Rocket League',
    '01010010 01001100',
    "the world's smallest violin",
    'null',
    "AttributeError: 'NoneType'",
    'NameError: GameNotFound',
    '001100 010010 011110 100001 101101 110011',
    "Wii Sports Resort",
    "Mario Kart",
    'Fallout 4',
    'Hollow Knight: Silksong (devbuild 0.91.12)'
]

ConchShellResponses = [
    "Maybe someday.",
    "Nothing.",
    "Neither.",
    "I don't think so.",
    "No.",
    "Yes.",
    "Try asking again."
]

sus_list = [
    'yea.. they sus',
    'they super sus, bro',
    'mhmm, sus',
    'oh yeah, sus',
    'super sus...',
    'not sus, they good',
    'nah, not sus',
    'not sus at all, bro',
    'they good, no sus here',
    'no sus found'
]

# emotes = [
#     'MCS',
#     'DeleteThis',
#     'bruhwack',
#     'yowza',
#     'sads',
#     'WWWAAAA',
#     'lol',
#     'huh',
#     'hooookay'
# ]


#############################
# Start-up command
#############################
@client.event
async def on_ready():
    print(f'{client.user} bot ready!')
    await client.change_presence(activity=discord.Game(name=random.choice(status_list)))
    change_status.start()


#############################
# Message specifics
#############################
@client.event
async def on_message(message):
    # Adds Bread reaction to random message
    if random.randint(0, 99) == 0:
        bread = '\U0001f35e'
        await message.add_reaction(bread)

    matches = ['mcs', 'shell', 'conch', 'bot']
    if any(x in message.content.lower() for x in matches):
        time.sleep(1)
        if random.randint(0, 99) < 5:
            await message.add_reaction(discord.utils.get(message.guild.emojis, name='MCS'))

    matches = ['haha', 'lol']
    if any(x in message.content.lower() for x in matches):
        time.sleep(1)
        if random.randint(0, 99) < 5:
            await message.add_reaction(discord.utils.get(message.guild.emojis, name='lol'))

    matches = ['psyonix']
    if any(x in message.content.lower() for x in matches):
        time.sleep(1)
        if random.randint(0, 99) < 10:
            await message.add_reaction(discord.utils.get(message.guild.emojis, name='WWWAAAA'))

    matches = ['ok', 'sounds good', 'nice!', 'cool!', 'hop on', 'back on']
    if any(x in message.content.lower() for x in matches):
        time.sleep(1)
        if random.randint(0, 99) < 5:
            await message.add_reaction(discord.utils.get(message.guild.emojis, name='hooookay'))

    matches = [':(', '):', 'noo', 'sorry', "i don't think so",
               ' f ', 'rip', 'sad', "can't", "won't", 'maybe later', 'maybe someday']
    if any(x in message.content.lower() for x in matches):
        time.sleep(1)
        if random.randint(0, 99) < 5:
            await message.add_reaction(discord.utils.get(message.guild.emojis, name='sads'))

    matches = ['upload']
    if any(x in message.content.lower() for x in matches):
        time.sleep(1)
        if random.randint(0, 99) < 25:
            await message.add_reaction(discord.utils.get(message.guild.emojis, name='bruhwack'))

    # This line allows on_message and commands
    await client.process_commands(message)


##########################################################
# looping command
# Changes the bot's game status every x minutes
##########################################################
@tasks.loop(minutes=120)
async def change_status():
    await client.change_presence(activity=discord.Game(name=random.choice(status_list)))


#############################
# ping command
#############################
@client.command(help="$ping")
async def ping(ctx):
    await ctx.send(f'Bot latency: {round(client.latency * 1000)}ms')


#############################
# mcs command
#############################
@client.command(help="$mcs [Yes or No question]", aliases=['magicconchshell', 'conch', 'conchshell', 'magicshell', 'shell', 'MCS'])
async def mcs(ctx, *, question):
    time.sleep(1)
    await ctx.send(random.choice(ConchShellResponses))


#############################
# sus command
#############################
@client.command(aliases=['sus?'])
async def sus(ctx):
    time.sleep(1)
    await ctx.send(random.choice(sus_list))


#############################
# percent command
#############################
@client.command(help="$percent [what percentage is x?]", aliases=['whatpercent'])
async def percent(ctx, *, question):
    time.sleep(1)
    await ctx.send(f'{random.randint(0, 100)}%')


#############################
# price command
#############################
@client.command(help="$price [how much is x worth?]")
async def price(ctx, *, question):
    time.sleep(1)
    await ctx.send(f'${random.randint(0, 60)}.{"%02d" % random.randint(0, 99)}')


#############################
# game command
#############################
def log_game(gamename):
    # log_path = r'.\LogGames.txt'
    log_path = r'/home/ubuntu/Discord/MagicConchShell/LogGames.txt'
    with open(log_path, 'a') as log_file:
        log_file.write(gamename + '\n')


@client.command(help="$game [Name of Game]")
async def game(ctx, *arg):
    gamename = ''
    for i in arg:
        gamename += i + " "
    await ctx.send(f'Now playing {gamename}')
    await client.change_presence(activity=discord.Game(name=gamename))
    log_game(gamename)


#############################
# slap command
#############################
@client.command(help="$slap [name]")
async def slap(ctx, *, arg):
    time.sleep(1)

    # matches = ['mcs', 'yourself', 'magic', 'conch', 'shell']
    # if any(x in arg.lower() for x in matches):

    if 'mcs' in arg.lower() or 'yourself' in arg.lower() or 'the' in arg.lower() or 'magic' in arg.lower() or 'conch' in arg.lower() or 'shell' in arg.lower():
        await ctx.send(f':raised_hand: *Slap!* {ctx.author} has been punished for trying to be smart.')
    else:
        await ctx.send(f':raised_hand: *Slap!* {arg} has been punished.')


client.run(token)
