import discord
from discord.ext import commands
import logging
import asyncio
import random
import time
import os

client = commands.Bot(command_prefix="%")
footer_text = "Eclipse"

@client.event
async def on_ready():
    print("Logged in as:")
    print(client.user.name)
    print(client.user.id)
    print("---------------")
    await client.change_presence(game=discord.Game(name='with Earth'))

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

# <kick <user> [reason]
@client.command(pass_context=True)
async def kick(ctx, userName: discord.Member = None, *, args = None):
    helper_role = discord.utils.get(ctx.message.server.roles, name='CHAT MODS')
    mod_role = discord.utils.get(ctx.message.server.roles, name='MOD')
    admin_role = discord.utils.get(ctx.message.server.roles, name='ADMIN')
    manager_role = discord.utils.get(ctx.message.server.roles, name='CO-FOUNDERS')
    owner_role = discord.utils.get(ctx.message.server.roles, name='FOUNDERS')
    author = ctx.message.author
    msg = discord.Embed(colour=0x9b0019, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userName == None:
            msg.add_field(name=":warning: ", value="`%kick (user) (reason)`")
        elif helper_role in userName.roles or mod_role in userName.roles or admin_role in userName.roles or manager_role in userName.roles or owner_role in userName.roles:
            msg.add_field(name=":warning: ", value="`You can't kick other staff!`")
        elif args == None:
            msg.add_field(name=":boot: Kicker", value="`{} kicked {}!`\n`Reason: ?`".format(author.display_name, userName.display_name))
            await client.kick(userName)
        else:
            msg.add_field(name=":boot: Kicker", value="`{} kicked {}!`\n`Reason: {}`".format(author.display_name, userName.display_name, args))
            await client.kick(userName)
    else:
        msg.add_field(name=":octagonal_sign: ", value="`This command can only be used by Moderators, Administrators, Co-Founders and Founders!`")
    await client.say(embed=msg)
    
# %ban <user> [reason]
@client.command(pass_context=True)
async def ban(ctx, userName: discord.Member = None, *, args = None):
    helper_role = discord.utils.get(ctx.message.server.roles, name='CHAT MODS')
    mod_role = discord.utils.get(ctx.message.server.roles, name='MOD')
    admin_role = discord.utils.get(ctx.message.server.roles, name='ADMIN')
    manager_role = discord.utils.get(ctx.message.server.roles, name='CO-FOUNDERS')
    owner_role = discord.utils.get(ctx.message.server.roles, name='FOUNDERS')
    author = ctx.message.author
    msg = discord.Embed(colour=0x9b0019, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userName == None:
            msg.add_field(name=":warning: ", value="`%ban <user> [reason]`")
        elif helper_role in userName.roles or mod_role in userName.roles or admin_role in userName.roles or manager_role in userName.roles or owner_role in userName.roles:
            msg.add_field(name=":warning: ", value="`You can't ban other staff!`")
        elif args == None:
            msg.add_field(name=":hammer: Ban Hammer", value="`{} banned {}!`\n`Reason: ?`".format(author.display_name, userName.display_name))
            await client.ban(userName)
        else:
            msg.add_field(name=":hammer: Ban Hammer", value="`{} banned {}!`\n`Reason: {}`".format(author.display_name, userName.display_name, args))
            await client.ban(userName)
    else:
        msg.add_field(name=":warning: ", value="`This command can only be used by Moderators, Admins, Co Founders and Founders!`")
    await client.say(embed=msg)

# %unban <user id>
@client.command(pass_context=True)
async def unban(ctx, userID = None):
    mod_role = discord.utils.get(ctx.message.server.roles, name='MOD')
    admin_role = discord.utils.get(ctx.message.server.roles, name='ADMIN')
    manager_role = discord.utils.get(ctx.message.server.roles, name='CO-FOUNDERS')
    owner_role = discord.utils.get(ctx.message.server.roles, name='FOUNDERS')
    author = ctx.message.author
    msg = discord.Embed(colour=0x9b0019, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userID == None:
            msg.add_field(name=":warning: ", value="`%unban <user id>`")
        else:
            banned_users = await client.get_bans(ctx.message.server)
            user = discord.utils.get(banned_users,id=userID)
            if user is not None:
                await client.unban(ctx.message.server, user)
                msg.add_field(name=":tools: ", value="`{} unbanned the user with the following ID: {}!`".format(author.display_name, userID))
            else:
                msg.add_field(name=":octagonal_sign: ", value="`The ID you specified is not banned! ID: {}`".format(userID))
    else:
        msg.add_field(name=":warning: ", value="`This command can only be used by Moderators, Administrators, Co Founders and Founders!`")
    await client.say(embed=msg)
    
# %say <text>
@client.command(pass_context=True)
async def say(ctx, *, args=None): 
    staff_role = discord.utils.get(ctx.message.server.roles, name='STAFF')
    author = ctx.message.author
    msg = discord.Embed(colour=0x9b0019, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if staff_role in author.roles or staff_role in author.roles:
        if args == None:
            msg.add_field(name=":warning: ", value="%say <text>")
            await client.say(embed=msg)
        else:
            await client.say("{}".format(args))
            await client.delete_message(ctx.message)
    else:
        msg.add_field(name=":warning: ", value="`This command can only be used by Staff!`")
        await client.say(embed=msg)
        
# %penis
@client.command(pass_context=True)
async def penis(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0x9b0019, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    choice = random.randint(0, 12)
    if choice == 0 or choice == 1:
        msg.add_field(name=":straight_ruler: ", value="`I'm sorry, {}, you currently do not have a dick.`".format(author.display_name))
    elif choice == 10 or choice == 12:
        msg.add_field(name=":straight_ruler: ", value="`Error! Currently {}'s dick is too big for me to take the length of it.`".format(author.display_name))
    else:
        msg.add_field(name=":straight_ruler: ", value="`Currently, {}'s dick is {}cm long.`".format(author.display_name, random.randint(1, 14)))
    await client.say(embed=msg)
    
# Member Count
@client.command(pass_context=True)
async def mc(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0x9b0019, description= "")
    msg.title = ":closed_book: Member Count :closed_book:"
    msg.add_field(name="MEMBERS", value=(len(ctx.message.server.members)), inline=True)
    await client.say(embed=msg)
    
# %userinfo <user>
@client.command(pass_context=True)
async def userinfo(ctx, userName: discord.Member = None):
    member_role = discord.utils.get(ctx.message.server.roles, name='MEMBERS')
    staff_role = discord.utils.get(ctx.message.server.roles, name='STAFF')
    author = ctx.message.author
    msg = discord.Embed(colour=0x9b0019, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if member_role in author.roles or staff_role in author.roles:
        if userName == None:
            msg.title = ""
            msg.add_field(name="       :warning: ", value="`%userinfo <user>`")
        else:
            imageurl = userName.avatar_url
            msg.title = ":closed_book: USER INFORMATION"
            msg.set_thumbnail(url=imageurl)
            msg.add_field(name="NAME:", value=(userName), inline=True)
            msg.add_field(name="ID:", value=(userName.id), inline=True)
            msg.add_field(name="CREATED AT:", value=(userName.created_at), inline=True)
            msg.add_field(name="JOINED AT:", value=(userName.joined_at), inline=True)
            msg.add_field(name="STATUS:", value=(userName.status), inline=True)
            msg.add_field(name="IS BOT:", value=(userName.bot), inline=True)
            msg.add_field(name="GAME:", value="Playing {}".format(userName.game), inline=True)
            msg.add_field(name="NICKNAME:", value=(userName.nick), inline=True)
            msg.add_field(name="TOP ROLE:", value=(userName.top_role), inline=True)
            msg.add_field(name="VOICE CHANNEL:", value=(userName.voice_channel), inline=True)
    await client.say(embed=msg)
    
# <hug <user>
@client.command(pass_context=True)
async def hug(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x9b0019, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`%hug (user)`")
    else:
        msg.set_image(url="{}".format(random.choice(huglinks)))
        msg.add_field(name=":new_moon: Emotes :new_moon:", value="`{}, you got a hug from {}!`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}hug <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

huglinks = ["https://i.imgur.com/yE2RnXK.gif",
            "https://i.imgur.com/R9sYxk8.gif",
            "https://i.imgur.com/iLBEoKv.gif",
            "https://i.imgur.com/cc554e8.gif",
            "https://i.imgur.com/1dqkjHe.gif",
            "https://i.imgur.com/Ph8GTqg.gif",
            "https://i.imgur.com/G6EnOxd.gif",
            "https://i.imgur.com/ZxwHn5Y.gif",
            "https://i.imgur.com/movPIsP.gif",
            "https://i.imgur.com/tKlfSgo.gif",
            "https://i.imgur.com/ICg9nCr.gif",
            "https://i.imgur.com/yC95DC2.gif",
            "https://i.imgur.com/hRYXNKX.gif",
            "https://i.imgur.com/br3bGQc.gif",
            "https://i.imgur.com/IcNGAQD.gif"]

# %eightball <yes or no question>
@client.command(pass_context=True)
async def eightball(ctx, *, args=None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x9b0019, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name="warning: ", value="`%eightball (Y/N Question)`")
    else:
        msg.add_field(name="Magic Eight Ball", value=":question: **Question:**\n`{}`\n \n:8ball: **Answer:**\n`{}`".format(args, random.choice(eightballmsgs)))
    await client.say(embed=msg)
    print("============================================================")
    print("<eightball <yes or no question>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

eightballmsgs = ["Yes!",
                 "No!",
                 "Probably!",
                 "Most likely!",
                 "Probably not!",
                 "Definitely!",
                 "Definitely not!",
                 "Of course!",
                 "Of course not!",
                 "WTF no!",
                 "Hell yeah!"]

# %calculator <math problem>
@client.command(pass_context=True)
async def calculator(ctx, *, args=None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x9b0019, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name=":warning: ", value="`%calculator (Math Problem)`")
    else:
        answer = str(eval(args))
        msg.add_field(name=":fax: Calculator", value= "`Problem: {}`\n \n`Answer: {}`".format(args, answer), inline=True)
    await client.say(embed=msg)
client.run(os.environ['BOT_TOKEN'])
