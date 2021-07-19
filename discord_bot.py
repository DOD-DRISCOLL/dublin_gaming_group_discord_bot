# bot.py
import os
import random
import discord

from discord.ext import commands
from dotenv import load_dotenv
from discord.utils import get

global dnd_mode
dnd_mode = False
global werewolf_mode 
werewolf_mode = False
global vampire_mode 
vampire_mode = False
global exploding_dice 
exploding_dice = False
global successes 
successes = False

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='', intents=intents)

@bot.command(name = 'roll', help='simulate dice rolling.')
async def roll(ctx, command_1: str, command_2 = '', command_3 = ''):
    global successes
    d_position = command_1.find("d")
    first_number = ''
    second_number = ''
    number_of_dice = 0
    number_of_sides = 0
    number_of_successes = 0
    explosion_number_target = 10
    dice = []
    counter = 0
    rote = False

    if (command_2 == "9again"):
        explosion_number_target = 9

    if (command_2 == "8again"):
        explosion_number_target = 8

    if (command_2 == "rote"):
        rote = True

    if (command_3 == "rote"):
        rote = True

    for x in range(d_position):
        first_number += command_1[x]

    for x in range(d_position+1, len(command_1)):
        second_number += command_1[x]

    number_of_dice = int(first_number)
    number_of_dice_original = number_of_dice
    number_of_sides = int(second_number)

    print('Number of dice = ' + str(number_of_dice))
    print('Number of sides = ' + str(number_of_sides))
    if guild.members[i].id == 225026277701189642:
        number_of_successes = number_of_dice
    elif (number_of_sides == 10 and rote == False):
        while (counter < number_of_dice): 
            random_number = random.choice(range(1, number_of_sides + 1))
        
            if (random_number >= explosion_number_target and exploding_dice == True and successes == True):
                dice.append('(' + str(random_number) + ')')
                number_of_dice = number_of_dice + 1
            else:
                dice.append(str(random_number))
            if (random_number >= 8):
                number_of_successes = number_of_successes + 1
            counter = counter + 1
    elif (number_of_sides == 10 and rote == True):
        while (counter < number_of_dice): 
            random_number = random.choice(range(1, number_of_sides + 1))
        
            if (random_number >= explosion_number_target and exploding_dice == True and successes == True):
                dice.append('(' + str(random_number) + ')')
                number_of_dice = number_of_dice + 1
            else:
                dice.append(str(random_number))

            if (random_number >= 8):
                number_of_successes = number_of_successes + 1
            elif counter < number_of_dice_original and random_number < 8:
                number_of_dice = number_of_dice + 1

            counter = counter + 1
    else:
        for x in range(number_of_dice):
            random_number = random.choice(range(1, number_of_sides + 1))
            dice.append(str(random_number))    

    line_1 = ', '.join(dice)
    line_2 = ''
    line_3 = ''

    if (number_of_sides == 10 and successes == True):
        line_2 = 'Number of successes = ' + str(number_of_successes)  

    if (number_of_sides == 10 and successes == True):
        average_comparison = calculate_better_than_average(number_of_dice_original, number_of_successes, explosion_number_target)

        if average_comparison == 1:
            line_3 = 'Better than average'
        elif average_comparison == -1:
            line_3 = 'Worse than average'
        elif average_comparison == 0:
            line_3 = 'Average'
            
    await ctx.send(line_1 + '\n' + line_2 + '\n' + line_3)

@bot.command(name = 'dnd_mode', help='change nicknames and remove dice explosions and successes')
async def dnd_mode(ctx):
    global dnd_mode
    dnd_mode = True
    global werewolf_mode
    werewolf_mode = False
    global vampire_mode
    vampire_mode = False

    global exploding_dice
    exploding_dice = False
    global successes
    successes = False

    for guild in bot.guilds:
        if guild.name == GUILD:
           break 

    i = 0
    while i < len(guild.members):
        print(guild.members[i])
        if guild.members[i].id == 225027798870261760:
            await guild.members[i].edit(nick = 'Gloom')

        if guild.members[i].id == 225026277701189642:
            await guild.members[i].edit(nick = 'Erkir')

        #if guild.members[i].id == 343840363745640468:
        #    await guild.members[i].edit(nick = 'Shathor')

        if guild.members[i].id == 534893622869491734:
            await guild.members[i].edit(nick = 'Jim')

        if guild.members[i].id == 619826458566852608:
            await guild.members[i].edit(nick = 'The Mad Mage')

        if guild.members[i].id == 689439023009103987:
            await guild.members[i].edit(nick = 'Br Gray')

        if guild.members[i].id == 374739932352348160:
            await guild.members[i].edit(nick = 'Rhothomir')

        i = i + 1

    await ctx.send('dnd mode activated')

@bot.command(name = 'werewolf_mode', help='change members nicknames to their werewolf characters and add explosions and successes')
async def werewolf_mode(ctx):
    global dnd_mode
    dnd_mode = False
    global werewolf_mode
    werewolf_mode = True
    global vampire_mode
    vampire_mode = False

    global exploding_dice
    exploding_dice = True
    global successes
    successes = True

    for guild in bot.guilds:
        if guild.name == GUILD:
           break 

    i = 0
    while i < len(guild.members):
        print(guild.members[i])
        if guild.members[i].id == 225027798870261760:
            await guild.members[i].edit(nick = 'Ricardo')

        if guild.members[i].id == 225026277701189642:
            await guild.members[i].edit(nick = 'Brendan')

        #if guild.members[i].id == 343840363745640468:
        #    await guild.members[i].edit(nick = 'DM')

        if guild.members[i].id == 534893622869491734:
            await guild.members[i].edit(nick = 'Robert')

        if guild.members[i].id == 619826458566852608:
            await guild.members[i].edit(nick = 'Scars')

        if guild.members[i].id == 689439023009103987:
            await guild.members[i].edit(nick = 'Jackson')

        i = i + 1
    await ctx.send('activating werewolf mode')


@bot.command(name = 'vampire_mode', help='change member nicknames to their vampire characters and add explosions and successes')
async def vampire_mode(ctx):
    global dnd_mode
    dnd_mode = False
    global werewolf_mode
    werewolf_mode = False
    global vampire_mode
    vampire_mode = True

    global exploding_dice
    exploding_dice = True
    global successes
    successes = True

    for guild in bot.guilds:
        if guild.name == GUILD:
           break 

    i = 0
    while i < len(guild.members):
        if guild.members[i].id == 225027798870261760:
            await guild.members[i].edit(nick = 'Bowden')

        if guild.members[i].id == 225026277701189642:
            await guild.members[i].edit(nick = 'DM')

        #if guild.members[i].id == 343840363745640468:
        #    await guild.members[i].edit(nick = 'Phaxos')

        if guild.members[i].id == 534893622869491734:
            await guild.members[i].edit(nick = 'Thomas')

        if guild.members[i].id == 619826458566852608:
            await guild.members[i].edit(nick = 'Gawain')

        if guild.members[i].id == 689439023009103987:
            await guild.members[i].edit(nick = 'Sebastian')

        i = i + 1

    await ctx.send('activating vampire mode')


def calculate_better_than_average(number_of_dice, number_of_successes, explosion_number_target):
    if explosion_number_target == 10:
        expected_successes = number_of_dice * .33
    if explosion_number_target == 9:
        expected_successes = number_of_dice * .38
    if explosion_number_target == 8:
        expected_successes = number_of_dice * .42

    print('expected_successes : ' + str(expected_successes))

    if number_of_successes > expected_successes:
        return 1
    elif number_of_successes == expected_successes:
        return 0
    return -1

bot.run(TOKEN)