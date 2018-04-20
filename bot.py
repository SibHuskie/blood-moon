import discord
from discord.ext import commands
import logging
import asyncio
import random
import time
import os
import music

client = commands.Bot(command_prefix="%")
footer_text = "Eclipse"

@client.event
async def on_ready():
    print("Logged in as:")
    print(client.user.name)
    print(client.user.id)
    print("---------------")
    await client.change_presence(game=discord.Game(name='with Huskie'))

# %tempmute <user> <time> [reason]
@client.command(pass_context=True)
async def tempmute(ctx, userName: discord.Member = None, time: int = None, *, args = None):
    punished_role = discord.utils.get(ctx.message.server.roles, name='Muted')
    helper_role = discord.utils.get(ctx.message.server.roles, name='CHAT MODS')
    mod_role = discord.utils.get(ctx.message.server.roles, name='MOD')
    admin_role = discord.utils.get(ctx.message.server.roles, name='ADMIN')
    manager_role = discord.utils.get(ctx.message.server.roles, name='CO-FOUNDERS')
    owner_role = discord.utils.get(ctx.message.server.roles, name='FOUNDERS')
    author = ctx.message.author
    msg = discord.Embed(colour=0x9b0019, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if helper_role in author.roles or mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userName == None or time == None:
            msg.add_field(name=":warning: ", value="`%tempmute (user) (time) (reason)`")
            await client.say(embed=msg)
        elif helper_role in userName.roles or mod_role in userName.roles or admin_role in userName.roles or manager_role in userName.roles or owner_role in userName.roles:
            msg.add_field(name=":warning: ", value="`You can't mute other staff!`")
            await client.say(embed=msg)
        elif punished_role in userName.roles:
            msg.add_field(name=":warning: ", value="`That user is already muted!`")
            await client.say(embed=msg)
        else:
            time2 = time * 60
            if args == None:
                await client.add_roles(userName, punished_role)
                await client.remove_roles(userName, member_role)
                msg.add_field(name=":speak_no_evil: ", value="`{} has been muted by {}! for {} minute(s)!`\n`Reason: ?`".format(userName.display_name, author.display_name, time))
                await client.say(embed=msg)
                await asyncio.sleep(float(time2))
                await client.remove_roles(userName, punished_role)
                await client.say("```diff\n- Removed {}'s punishment! ({} minute(s) are up.)\n```".format(userName.display_name, time))
            else:
                await client.add_roles(userName, punished_role)
                msg.add_field(name=":speak_no_evil: ", value="`{} has been punished by {} for {} minute(s)!`\n`Reason: {}`".format(userName.display_name, author.display_name, time, args))
                await client.say(embed=msg)
                await asyncio.sleep(float(time2))
                await client.remove_roles(userName, punished_role)
                await client.say("```diff\n- Removed {}'s mute! ({} minute(s) are up.)\n```".format(userName.display_name, time))
    else:
        msg.add_field(name=":warning: ", value="`This command can only be used by staff!`")
        await client.say(embed=msg)
        
#%mute <user>
@client.command(pass_context=True)
async def mute(ctx, userName: discord.Member = None, args = None):
    punished_role = discord.utils.get(ctx.message.server.roles, name='Muted')
    helper_role = discord.utils.get(ctx.message.server.roles, name='CHAT MODS')
    mod_role = discord.utils.get(ctx.message.server.roles, name='MOD')
    admin_role = discord.utils.get(ctx.message.server.roles, name='ADMIN')
    manager_role = discord.utils.get(ctx.message.server.roles, name='CO-FOUNDERS')
    owner_role = discord.utils.get(ctx.message.server.roles, name='FOUNDERS')
    author = ctx.message.author
    msg = discord.Embed(colour=0x9b0019, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if helper_role in author.roles or mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userName == None or time == None:
            msg.add_field(name= ":warning:", value'"`%mute (user) (reason)
            await client.say(embed.msg)
        elif helper_role in userName.roles or mod_role in userName.roles or admin_role in userName.roles or manager_role in userName.roles or owner_role in userName.roles:
             msg.add_field(name=":warning: ", value="`You can't punish other staff!`")
            await client.say(embed=msg)
        elif punished_role in userName.roles:
            msg.add_field(name=":warning: ", value="`That user is already punished!`")
            await client.say(embed=msg)
        else:
            await client.add_roles(userName, punished_role)
            msg.add_field(name=":speak_no_evil: ", value="`{} has been muted by {}! for {} minute(s)!`\n`Reason: ?`".format(userName.display_name, author.display_name))
        else:
            msg.add_field(name=":warning:", value=",value="`This command can only be used by staff!`"
            await client.say(embed=msg)
client.run(os.environ['BOT_TOKEN'])
