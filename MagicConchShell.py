import discord
from discord.ext import commands, tasks
import nacl
import ffmpeg.audio
import random
import time
import asyncio
from time import gmtime, strftime

start_time = time.time()
client = commands.Bot(command_prefix='$')

# Have to change this path for Linux
token = open(r'.\token.txt', 'r').read()
# token = open(r'/home/ubuntu/Discord/MagicConchShell/token.txt', 'r').read()

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
    'Hollow Knight: Silksong (devbuild 0.91.12)',
    'Among Us',
    'Breath of the Wild 2'
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
    'yea... they sus',
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

food_list = [
    ':green_apple:',
    ':apple:',
    ':pear:',
    ':tangerine:',
    ':lemon:',
    ':banana:',
    ':watermelon:',
    ':grapes:',
    ':blueberries:',
    ':strawberry:',
    ':melon:',
    ':cherries:',
    ':peach:',
    ':mango:',
    ':pineapple:',
    ':coconut:',
    ':kiwi:',
    ':tomato:',
    ':eggplant:',
    ':avocado:',
    ':olive:',
    ':broccoli:',
    ':leafy_green:',
    ':bell_pepper:',
    ':cucumber:',
    ':hot_pepper:',
    ':corn:',
    ':carrot:',
    ':garlic:',
    ':onion:',
    ':potato:',
    ':sweet_potato:',
    ':croissant:',
    ':bagel:',
    ':bread:',
    ':french_bread:',
    ':flatbread:',
    ':pretzel:',
    ':cheese:',
    ':egg:',
    ':cooking:',
    ':butter:',
    ':pancakes:',
    ':waffle:',
    ':bacon:',
    ':cut_of_meat:',
    ':poultry_leg:',
    ':meat_on_bone:',
    ':hotdog:',
    ':hamburger:',
    ':fries:',
    ':pizza:',
    ':sandwich:',
    ':stuffed_flatbread:',
    ':falafel:',
    ':taco:',
    ':burrito:',
    ':tamale:',
    ':salad:',
    ':shallow_pan_of_food:',
    ':fondue:',
    ':canned_food:',
    ':spaghetti:',
    ':ramen:',
    ':stew:',
    ':curry:',
    ':sushi:',
    ':bento:',
    ':dumpling:',
    ':oyster:',
    ':fried_shrimp:',
    ':rice_ball:',
    ':rice:',
    ':rice_cracker:',
    ':fish_cake:',
    ':fortune_cookie:',
    ':moon_cake:',
    ':oden:',
    ':dango:',
    ':shaved_ice:',
    ':ice_cream:',
    ':icecream:',
    ':pie:',
    ':cupcake:',
    ':cake:',
    ':birthday:',
    ':custard:',
    ':lollipop:',
    ':candy:',
    ':chocolate_bar:',
    ':popcorn:',
    ':doughnut:',
    ':cookie:',
    ':chestnut:',
    ':peanuts:',
    ':honey_pot:',
    ':milk:',
    ':baby_bottle:',
    ':coffee:',
    ':tea:',
    ':teapot:',
    ':mate:',
    ':bubble_tea:',
    ':beverage_box:',
    ':cup_with_straw:',
    ':sake:',
    ':beer:',
    ':beers:',
    ':champagne_glass:',
    ':wine_glass:',
    ':tumbler_glass:',
    ':cocktail:',
    ':tropical_drink:',
    ':champagne:',
    ':ice_cube:',
    ':takeout_box:',
    ':salt:'
]


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
    try:
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
            if random.randint(0, 99) < 75:
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
            if random.randint(0, 99) < 50:
                await message.add_reaction(discord.utils.get(message.guild.emojis, name='bruhwack'))

    except:
        pass

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
@client.command(help="$ping", aliases=['p'])
async def ping(ctx):
    await ctx.send(f'Bot latency: {round(client.latency * 1000)}ms')


#############################
# uptime command
#############################
def get_uptime():
    end_time = time.time()
    return(strftime("%H:%M:%S", gmtime(int('{:.0f}'.format(float(str((end_time-start_time))))))))


@client.command(help="$uptime", aliases=['u'])
async def uptime(ctx):
    await ctx.send(f'Uptime: {get_uptime()}')


#############################
# mcs command
#############################
@client.command(help="$mcs [Yes or No question]", aliases=['conch', 'shell'])
async def mcs(ctx, *, question):
    time.sleep(1)
    await ctx.send(random.choice(ConchShellResponses))


# on_error
@mcs.error
async def mcs_handler(ctx, error):
    time.sleep(1)
    await ctx.send(f"You didn't ask me anything...")
    await ctx.send(f"Try asking something like this:\n```$mcs am I stupid?```")


#############################
# sus command
#############################
@client.command(help='$sus [the sus]', aliases=['sus?', 'howsus', 'howsus?'])
async def sus(ctx, *, arg):
    time.sleep(1)
    
    matches = ['mcs', 'yourself', 'magic', 'conch', 'shell', 'i']
    # $sus mcs
    if any(x in arg.lower() for x in matches) or str(arg) == '<@!754734227651690526>':
        await ctx.send(f'How dare you even ask...')
        return

    else:
        await ctx.send(random.choice(sus_list))


# on_error
@sus.error
async def sus_handler(ctx, error):
    time.sleep(1)
    await ctx.send(random.choice(sus_list))


#############################
# percent command
#############################
@client.command(help="$percent [what percentage is x?]", aliases=['whatpercent'])
async def percent(ctx, *arg):
    time.sleep(1)
    await ctx.send(f'{random.randint(0, 100)}%')


#############################
# price command
#############################
@client.command(help="$price [how much is x worth?]")
async def price(ctx, *, arg):
    time.sleep(1)

    matches = ['mcs', 'yourself', 'magic', 'conch', 'shell']
    if any(x in arg.lower() for x in matches) or str(arg) == '<@!754734227651690526>':
        await ctx.send(f"Priceless")
    else:
        await ctx.send(f'${random.randint(0, 60)}.{"%02d" % random.randint(0, 99)}')


# on_error
@price.error
async def price_handler(ctx, error):
    time.sleep(1)
    await ctx.send(f"You didn't say what you wanted appraised...")


#############################
# game command
#############################
def log_game(gamename, user):
    log_path = r'.\LogGames.txt'
    # log_path = r'/home/ubuntu/Discord/MagicConchShell/LogGames.txt'
    with open(log_path, 'a') as log_file:
        log_file.write(gamename + " " + user + '\n')


@client.command(help="$game [Name of Game]")
async def game(ctx, *arg):
    # If no game is entered. Empty tuple
    if not arg:
        await ctx.send(f"You didn't specify a game...")

    else:
        gamename = ''
        for i in arg:
            gamename += i + " "
        await ctx.send(f'Now playing {gamename}')
        await client.change_presence(activity=discord.Game(name=gamename))
        log_game(gamename, str(ctx.author))


#############################
# slap command
#############################
@client.command(help="$slap [name]")
async def slap(ctx, *, arg):
    time.sleep(1)

    matches = ['mcs', 'yourself', 'magic', 'conch', 'shell', 'i']
    matches2 = ['me', 'myself']

    # $slap mcs
    if any(x in arg.lower() for x in matches) or str(arg) == '<@!754734227651690526>':
        await ctx.send(f':raised_hand: *Slap!* {ctx.author.mention} has been punished for trying to be smart.')
        return
    
    # $slap me
    if any(x in arg.lower() for x in matches2):
        await ctx.send(f':raised_hand: *Slap!* {ctx.author.mention} has been punished.')
        return

    else:
        await ctx.send(f':raised_hand: *Slap!* {arg} has been punished.')


# on_error
@slap.error
async def slap_handler(ctx, error):
    time.sleep(1)
    await ctx.send(f"You didn't say who to slap...")
    time.sleep(1)
    await ctx.send(f':raised_hand: *Slap!* {ctx.author.mention} has been punished for not saying who to slap.')


#############################
# dice command
#############################
@client.command(help='$dice 3d18 (This will roll 3 dice with 18 sides)')
async def dice(ctx, *, arg):

    arg = arg.lower()

    if 'd' in arg:
        dice_params_lst = arg.split('d')
        num_of_dice = int(dice_params_lst[0])
        num_of_sides = int(dice_params_lst[1])

        if num_of_dice <= 0 or num_of_sides <= 0:
            await ctx.send(f'```{arg}``` is not valid. You must use positive intergers.')
            return

        roll_lst = []
        for _ in range(num_of_dice):
            roll_lst.append(random.randint(1, num_of_sides))

        embed = discord.Embed(
            description=f":game_die: {arg} {roll_lst}", color=0xff0000)
        await ctx.send(embed=embed)
        # await ctx.send(f'```{arg} {roll_lst}```')
    else:
        await ctx.send(f'"{arg}" is not valid syntax.')
        await ctx.send('To roll 3 dice with 18 sides:\n```$dice 3d18```')


# on_error
@dice.error
async def dice_handler(ctx, error):
    time.sleep(1)
    await ctx.send("Invalid syntax.")
    await ctx.send('To roll 3 dice with 18 sides:\n```$dice 3d18```')


#############################
# die command
#############################
@client.command(help='$die (This automatically rolls a 1d6)')
async def die(ctx):
    roll = random.randint(1, 6)
    embed = discord.Embed(
        description=f":game_die: 1d6 [{roll}]", color=0xff0000)
    await ctx.send(embed=embed)
    # await ctx.send(f'```1d6 [{roll}]```')


#############################
# feed command
#############################
@client.command(help='$feed [@person]')
async def feed(ctx, person):
    time.sleep(1)

    food = random.choice(food_list)

    matches = ['mcs', 'shell', 'conch', 'bot', 'yourself', 'magic']
    matches2 = ['me', 'myself']

    # If they say $feed mcs
    if any(x in str(person).lower() for x in matches) or str(person) == '<@!754734227651690526>':
        await ctx.send(f"I'm a ~~bot~~ **Magic Conch**. I don't require the {food} like meer mortals.")
        return

    # If they say $feed me or $feed myself
    if any(x in str(person).lower() for x in matches2):
        embed = discord.Embed(
            description=f"Forces {food} down {ctx.author.display_name}'s throat", color=0xff0000)
        await ctx.send(embed=embed)
        return

    else:
        embed = discord.Embed(
            description=f"Forces {food} down {person}'s throat", color=0xff0000)
        await ctx.send(embed=embed)
        return


# on_error
@feed.error
async def feed_handler(ctx, error):
    time.sleep(1)
    # if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("You didn't tell me who to feed...")


#############################
# sprite cranberry command
#############################
@client.command(help='$sprite', aliases=['s'])
async def sprite(ctx):

    channel = ctx.author.voice.channel
    print(channel)

    if channel == None:
        await ctx.send("You are not in a voice channel...")
    else:
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('/home/ubuntu/Discord/MagicConchShell/SpriteCranberry.mp3'), after=lambda e: print('done', e))
        await asyncio.sleep(2.5)
        await vc.disconnect()


#############################
# wow command
#############################
@client.command(help='$wow (Oh my God, WOW!)')
async def wow(ctx):

    channel = ctx.author.voice.channel
    print(channel)

    if channel == None:
        await ctx.send("You are not in a voice channel...")
    else:
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('/home/ubuntu/Discord/MagicConchShell/wow.mp3'), after=lambda e: print('done', e))
        await asyncio.sleep(6.5)
        await vc.disconnect()


client.run(token)
