import discord
from discord.ext import commands
from discord.ext.commands import Bot
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
    await client.change_presence(game=discord.Game(name='check #eclipse-commands'))

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
    choice = random.randint(0, 14)
    if choice == 0 or choice == 2:
        msg.add_field(name=":straight_ruler: ", value="`I'm sorry, {}, you currently do not have a dick.`".format(author.display_name))
    elif choice == 13 or choice == 14:
        msg.add_field(name=":straight_ruler: ", value="`Error! Currently {}'s dick is too big for me to take the length of it.`".format(author.display_name))
    else:
        msg.add_field(name=":straight_ruler: ", value="`Currently, {}'s dick is {} inches long.`".format(author.display_name, random.randint(2, 13)))
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
    
# %warn <user> <reason>
@client.command(pass_context=True)
async def warn(ctx, userName: discord.Member = None, *, args = None):
    helper_role = discord.utils.get(ctx.message.server.roles, name='CHAT MODS')
    mod_role = discord.utils.get(ctx.message.server.roles, name='MOD')
    admin_role = discord.utils.get(ctx.message.server.roles, name='ADMIN')
    manager_role = discord.utils.get(ctx.message.server.roles, name='CO-FOUNDERS')
    owner_role = discord.utils.get(ctx.message.server.roles, name='FOUNDERS')
    author = ctx.message.author
    msg = discord.Embed(colour=0x9b0019, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg2 = discord.Embed(colour=0x9b0019, description= "")
    msg2.title = ""
    msg2.set_footer(text=footer_text)
    if helper_role in author.roles or mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userName == None or args == None:
            msg.add_field(name=":warning: ", value="`%warn <user> <reason>`")
            await client.say(embed=msg)
        else:
                msg2.add_field(name=":pencil: ", value="`You have been warned by {} in Eclipse!`\n`Reason: {}`".format(author.display_name, args))
                msg.add_field(name=":pencil: ", value="`{} warned {}!`\n`Reason: {}`".format(author.display_name, userName.display_name, args))
                await client.say(embed=msg)
                await client.send_message(userName, embed=msg2)
    else:
        msg.add_field(name=":warning: ", value="`This command can only be used by staff!`")
        await client.say(embed=msg)
        
# <lick <user>
@client.command(pass_context=True)
async def lick(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x9b0019, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`%lick <user>`")
    else:
        msg.set_image(url="{}".format(random.choice(licklinks)))
        msg.add_field(name=":tongue: Emotes :tongue:", value="`{} licked {}!`".format(author.display_name, userName.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}lick <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

licklinks = ["https://i.imgur.com/QkRz1GJ.gif",
             "https://i.imgur.com/ObCPKYV.gif",
             "https://i.imgur.com/7fWrYqd.gif",
             "https://i.imgur.com/O8CNVUL.gif",
             "https://i.imgur.com/4QIlJtC.gif",
             "https://i.imgur.com/LptJIi1.gif",
             "https://i.imgur.com/THGgRJz.gif"]

# <kiss <user>
@client.command(pass_context=True)
async def kiss(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x9b0019, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`%kiss (user)`")
    else:
        msg.set_image(url="{}".format(random.choice(kisslinks)))
        msg.add_field(name=":tongue: Emotes :tongue:", value="`{}, you got kissed by {}!`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}kiss <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

kisslinks = ["https://i.imgur.com/0Ri9sfq.gif",
             "https://i.imgur.com/EMdpmXW.gif",
             "https://i.imgur.com/Y9iLoiv.gif",
             "https://i.imgur.com/ZlqZy8S.gif",
             "https://i.imgur.com/ySav1IQ.gif",
             "https://i.imgur.com/ZGfrn2d.gif",
             "https://i.imgur.com/glwWeUl.gif",
             "https://i.imgur.com/j5hDl7V.gif",
             "https://i.imgur.com/w7mVYty.gif",
             "https://i.imgur.com/FJ5bckO.gif",
             "https://i.imgur.com/KqVmVU7.gif",
             "https://i.imgur.com/EM1C9a6.gif",
             "https://i.imgur.com/TACVpH9.gif",
             "https://i.imgur.com/opiHLtc.gif",
             "https://i.imgur.com/LylJAea.gif"]

# <spank <user>
@client.command(pass_context=True)
async def spank(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x9b0019, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`%spank (user)`")
    else:
        msg.set_image(url="{}".format(random.choice(spanklinks)))
        msg.add_field(name=":tongue: Emotes :tongue:", value="`{} spanked {}!`".format(author.display_name, userName.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}spank <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

spanklinks = ["https://i.imgur.com/dt1TTQu.gif",
              "https://i.imgur.com/ZsTbDvh.gif",
              "https://i.imgur.com/4LHwG60.gif",
              "https://i.imgur.com/xLOoHKP.gif",
              "https://i.imgur.com/UShywVv.gif",
              "https://i.imgur.com/RE3mnrA.gif"]

# %slap <user>
@client.command(pass_context=True)
async def slap(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x9b0019, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`}slap <user>`")
    else:
        msg.set_image(url="{}".format(random.choice(slaplinks)))
        msg.add_field(name=":tongue: Emotes :tongue:", value="`{}, you got slapped by {}! :3`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}slap <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

slaplinks = ["https://i.imgur.com/EAF42MG.gif",
             "https://i.imgur.com/tLTT9Q4.gif",
             "https://i.imgur.com/tEWjg7v.gif",
             "https://i.imgur.com/MlkLTjv.gif",
             "https://i.imgur.com/hoTYJZP.gif",
             "https://i.imgur.com/Pthhs3Y.gif"]

# %report <user> <reason>
@client.command(pass_context=True)
async def report(ctx, userName: discord.Member = None, *, args = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x9b0019, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg2 = discord.Embed(colour=0x9b0019, description= "")
    msg2.title = ""
    msg2.set_footer(text=footer_text)
    if userName == None or args == None:
        msg.add_field(name=":warning: ", value="`%report <user> <reason>`")
    else:
        msg.add_field(name=":clipboard: REPORT", value="`{} has reported {}!`".format(author.display_name, userName.display_name))
        msg2.add_field(name=":clipboard: REPORT", value="`Reporter:`\n`{} ### {}`\n`Reported:`\n`{} ### {}`\n`Reason:`\n`{}`".format(author, author.id, userName, userName.id, args))
        channel = client.get_channel('437169979662663680')
        await client.send_message(channel, embed=msg2)
    await client.say(embed=msg)
    print("============================================================")
    print("%report <user> <reason>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# %stare <user>
@client.command(pass_context=True)
async def stare(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x9b0019, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`%stare (user)`")
    else:
        msg.set_image(url="{}".format(random.choice(starelinks)))
        msg.add_field(name=":tongue: Emotes :tongue:", value="`{}, {} is staring at you! :3`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}stare <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
starelinks = ["https://i.imgur.com/f8rFNH0.gif",
              "https://i.imgur.com/ACCQDj4.gif",
              "https://i.imgur.com/1Co1i9t.gif",
              "https://i.imgur.com/uPZHQxV.gif",
              "https://i.imgur.com/wXQLAb3.gif",
              "https://i.imgur.com/hY7ZngK.gif"]

# %rate <text>
@client.command(pass_context=True)
async def rate(ctx, *, args = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x9b0019, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name=":warning: ", value="`%rate (text)`")
    else:
        msg.add_field(name=":scales:", value="`I'd rate {} a {}/10`".format(args, random.randint(0, 11)))
    await client.say(embed=msg)
    print("============================================================")
    print("}rate <text>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# %ship <text> <text>
@client.command(pass_context=True)
async def ship(ctx, args1 = None, args2 = None):
    percent = random.randint(0, 101)
    author = ctx.message.author
    msg = discord.Embed(colour=0x9b0019, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName1 == None or userName2 == None:
        msg.add_field(name=":warning: ",value="`%ship (text1) (text2)`")
    else:
        if percent >= 1 and percent <= 10:
            msg.add_field(name=":heartpulse: S H I P  M A C H I N E :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Shit\n```\n:sob: ".format(args1, args2, percent))
        elif percent >= 11 and percent <= 20:
            msg.add_field(name=":heartpulse: S H I P  M A C H I N E :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Awful\n```\n:cry: ".format(args1, args2, percent))
        elif percent >= 21 and percent <= 30:
            msg.add_field(name=":heartpulse: S H I P  M A C H I N E :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Really Bad\n```\n:frowning2: ".format(args1, args2, percent))
        elif percent >= 31 and percent <= 40:
            msg.add_field(name=":heartpulse: S H I P  M A C H I N E :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Bad\n```\n:slight_frown: ".format(args1, args2, percent))
        elif percent >= 41 and percent <= 50:
            msg.add_field(name=":heartpulse: S H I P  M A C H I N E :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Okay\n```\n:neutral_face: ".format(args1, args2, percent))
        elif percent >= 51 and percent <= 60:
            msg.add_field(name=":heartpulse: S H I P  M A C H I N E :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Good\n```\n:slight_smile: ".format(args1, args2, percent))
        elif percent >= 61 and percent <= 70:
            msg.add_field(name=":heartpulse: S H I P  M A C H I N E :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Very Good\n```\n:smiley: ".format(args1, args2, percent))
        elif percent >= 71 and percent <= 80:
            msg.add_field(name=":heartpulse: S H I P  M A C H I N E :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Fantastic\n```\n:blush: ".format(args1, args2, percent))
        elif percent >= 81 and percent <= 90:
            msg.add_field(name=":heartpulse: S H I P  M A C H I N E :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Amazing\n```\n:heart_eyes: ".format(args1, args2, percent))
        else:
            msg.add_field(name=":heartpulse: S H I P  M A C H I N E :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Perfect\n```\n:revolving_hearts: ".format(args1, args2, percent))
    await client.say(embed=msg)
    print("============================================================")
    print("}ship <user1> <user2>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# %roast <user>
@client.command(pass_context=True)
async def roast(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x9b0019, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`%roast (user)`")
    else:
        msg.add_field(name=":fire: Roast Machine :fire:", value="`{}, {}`".format(userName.display_name, random.choice(roasts)))
    await client.say(embed=msg)
    print("============================================================")
    print("}roast <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
roasts = ["stop playing hard to get when you're hard to want.",
          "you uncultured cranberry fucknut.",
          "12 must be hard for you. Not the age. Having it as an IQ.",
          "your ass must be jealous of all the shit that comes out of your mouth.",
          "I'm trying to see from your perspective but I just can't get my head that far up my ass.",
          "the only thing you're fucking in natural selection.",
          "I can't breathe when I see you... cause I'm suffocating of your bullshit.",
          "your mom is twice the man you will ever be.",
          "you have the right to remain silent, cause what ever you say will be stupid anyways.",
          "the only thing you are good at is being a cunt.",
          "it's hard to ignore you, mostly cause you smell like shit.",
          "you must've fallen from Mars, cause you clearly can't understand anything happening around you.",
          "did you fall from Heaven? Cause so did Satan.",
          "you're so ugly, you went to an ugly competition and they said 'No professionals allowed!'.",
          "I'd give you a nasty look but you've already got one.",
          "if laughter is the best medicine, your face must be curing the world.",
          "the only way you'll ever get laid is if you crawl up a chicken's ass and wait.",
          "your family tree must be a cactus because everyone on it is a prick.",
          "someday you'll go far... and I hope you stay there.",
          "the zoo called. They're wondering how you got out of your cage?",
          "you have something on your chin... no, the 3rd one down.",
          "thought of you today. It reminded me to take the garbage out.",
          "it's better to let someone think you're stupid than open your mouth and prove it.",
          "calling you an idiot would be an insult to all stupid people.",
          "I just stepped in something that was smarter than you... and smelled better too."]

# %nom <user>
@client.command(pass_context=True)
async def nom(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x9b0019, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`%nom (user)`")
    else:
        msg.set_image(url="{}".format(random.choice(nomlinks)))
        msg.add_field(name=":tongue: Emotes :tongue:", value="`{}, {} nommed you! :3`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}nom <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
nomlinks = ["https://i.imgur.com/E1eQPfu.gif",
            "https://i.imgur.com/UUZY3Rb.gif",
            "https://i.imgur.com/Zd6fIpA.gif",
            "https://i.imgur.com/i2NaBS7.gif",
            "https://i.imgur.com/Up5J6Nn.gif",
            "https://i.imgur.com/J5MLku7.gif",
            "https://i.imgur.com/7yYgZXE.gif"]

# %bite <user>
@client.command(pass_context=True)
async def bite(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x9b0019, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`%bite (user)`")
    else:
        msg.set_image(url="{}".format(random.choice(bitelinks)))
        msg.add_field(name=":tongue: Emotes :tongue:", value="`{}, you got bitten by {}! :3`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}bite <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
bitelinks = ["https://i.imgur.com/E0jIIa9.gif",
             "https://i.imgur.com/Nvkw6hN.gif",
             "https://i.imgur.com/wr7l06j.gif",
             "https://i.imgur.com/uce91VI.gif"]

# %cookie <user> <number>
@client.command(pass_context=True)
async def cookie(ctx, userName: discord.Member = None, number: int = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x9b0019, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None or number == None:
        msg.add_field(name=":warning: ", value="`%cookie (user) (number)`")
    else:
        if number > 100:
            msg.add_field(name=":warning: ", value="`You can't give over 100 cookies to someone! Save some for yourself!`")
        else:
            msg.add_field(name=":smiley: ", value="`{} gave {}` :cookie: `to {}!`\n`Be like {}!`".format(author.display_name, number, userName.display_name, author.display_name))
    await client.say(embed=msg)
    print("============================================================")
    print("}cookie <user> <number>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# %annoy <user> [text]
@client.command(pass_context=True)
async def annoy(ctx, userName: discord.Member = None, *, args = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x9b0019, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`%annoy (user) (text)`")
        await client.say(embed=msg)
    else:
        if args == None:
            msg.add_field(name=":drooling_face: ", value="`Sending a beautiful video to {}...`".format(userName.display_name))
            await client.say(embed=msg)
            await client.send_message(userName, "{}".format(random.choice(rickrolls)))
        else:
            msg.add_field(name=":drooling_face: ", value="`Sliding in {}'s DMs...`".format(userName.display_name))
            await client.say(embed=msg)
            await client.send_message(userName, "{}".format(args))
    print("============================================================")
    print("}rickroll <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
rickrolls = ["https://www.youtube.com/watch?v=V-_O7nl0Ii0",
             "https://www.youtube.com/watch?v=ID_L0aGI9bg",
             "https://www.youtube.com/watch?v=yBLdQ1a4-JI",
             "https://www.youtube.com/watch?v=6-HUgzYPm9g",
             "https://www.youtube.com/watch?v=Gc2u6AFImn8",
             "https://www.youtube.com/watch?v=4n7_Il1dft0",
             "https://www.youtube.com/watch?v=OL7B2z56ziQ",
             "https://www.youtube.com/watch?v=li7qFeHI5KM",
             "https://www.youtube.com/watch?v=wvWX-jWhLBI",
             "https://youtu.be/ByC8sRdL-Ro",
             "https://www.youtube.com/watch?v=HoWcnTsc5s8",
             "hi lol",
             "https://www.youtube.com/watch?v=E9DlT_DS0wA",
             "https://youtu.be/rp8hvyjZWHs",
             "https://www.youtube.com/watch?v=3HfnLwopb58"]

# %purge <number>
@client.command(pass_context=True)
async def purge(ctx, number: int = None):
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
        if number == None:
            msg.add_field(name=":warning: ", value="`%purge <number>`")
        else:
            deleted = await client.purge_from(ctx.message.channel, limit=number)
            if len(deleted) < number:
                msg.add_field(name=":wastebasket: ", value="`{} tried to delete {} messages!`\n`Deleted {} message(s)!`".format(author.display_name, number, len(deleted)))
            else:
                msg.add_field(name=":wastebasket: ", value="`{} deleted {} message(s)!`".format(author.display_name, len(deleted)))
    else:
        msg.add_field(name=":warning: ", value="`This command can only be used by staff!`")
    await client.say(embed=msg)
    print("============================================================")
    print("}purge <number>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# %nick <user> [nickname]
@client.command(pass_context=True)
async def nick(ctx, userName: discord.Member = None, *, args = None):
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
        if userName == None:
            msg.add_field(name=":warning: ", value="`%nick (user) (nickname)`")
        elif args == None:
            nickname = args
            await client.change_nickname(userName, nickname)
            msg.add_field(name=":label: ", value="`{} removed {}'s nickname!`".format(author.display_name, userName.display_name))
        else:
            nickname = args
            msg.add_field(name=":label: ", value="`{} changed {}'s nickname to {}!`".format(author.display_name, userName.display_name, args))
            await client.change_nickname(userName, nickname)
    else:
        msg.add_field(name=":warning: ", value="`This command can only be used by staff!`")
    await client.say(embed=msg)
    print("============================================================")
    print("}nick <user> <nickname>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# %giverole <user> <role name>
@client.command(pass_context=True)
async def giverole(ctx, userName: discord.Member = None, *, args = None):
    admin_role = discord.utils.get(ctx.message.server.roles, name='ADMIN')
    manager_role = discord.utils.get(ctx.message.server.roles, name='CO-FOUNDERS')
    owner_role = discord.utils.get(ctx.message.server.roles, name='FOUNDERS')
    author = ctx.message.author
    msg = discord.Embed(colour=0x9b0019, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    serverroles = [ctx.message.server.roles]
    if admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userName == None or args == None:
            msg.add_field(name=":warning: ", value="`%giverole (user) (role name)`")
        else:
            rolename2 = discord.utils.get(ctx.message.server.roles, name='{}'.format(args))
            if rolename2 == None:
                msg.add_field(name=":warning: ", value="`The specified role has not been found! Sorry I'm case sensitive...`")
            elif author.top_role == rolename2 or author.top_role < rolename2:
                msg.add_field(name=":warning: ", value="`You cannot give a role that is the same or higher than your top role!`")
            else:
                await client.add_roles(userName, rolename2)
                msg.add_field(name=":inbox_tray: ", value="`{} gave {} to {}!`".format(author.display_name, args, userName.display_name))
    else:
        msg.add_field(name=":warning: ", value="`This command can only be used by Adminis, Co-Founders and Founders!`")
    await client.say(embed=msg)
    print("============================================================")
    print("}giverole <user> <role name>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# %takerole <user> <role name>
@client.command(pass_context=True)
async def takerole(ctx, userName: discord.Member = None, *, args = None):
    admin_role = discord.utils.get(ctx.message.server.roles, name='ADMIN')
    manager_role = discord.utils.get(ctx.message.server.roles, name='CO-FOUNDERS')
    owner_role = discord.utils.get(ctx.message.server.roles, name='FOUNDERS')
    author = ctx.message.author
    msg = discord.Embed(colour=0x9b0019, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    serverroles = [ctx.message.server.roles]
    if admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userName == None or args == None:
            msg.add_field(name=":warning: ", value="`%takerole (user) (role name)`")
        else:
            rolename2 = discord.utils.get(ctx.message.server.roles, name='{}'.format(args))
            if rolename2 == None:
                msg.add_field(name=":warning: ", value="`The specified role has not been found! Sorry I'm case sensitive...`")
            elif author.top_role == rolename2 or author.top_role < rolename2:
                msg.add_field(name=":warning: ", value="`You cannot remove a role that is the same or higher than your top role!`")
            else:
                await client.remove_roles(userName, rolename2)
                msg.add_field(name=":outbox_tray: ", value="`{} removed {} from {}!`".format(author.display_name, args, userName.display_name))
    else:
        msg.add_field(name=":octagonal_sign: ", value="`This command can only be used by Adminis, Co-Founders and Founders!`")
    await client.say(embed=msg)
    print("============================================================")
    print("}takerole <user> <role name>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# %cuddle <user>
@client.command(pass_context=True)
async def cuddle(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x9b0019, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`%cuddle (user)`")
    else:
        msg.set_image(url="{}".format(random.choice(cuddlelinks)))
        msg.add_field(name=":tongue: Emotes :tongue:", value="`{}, you got a cuddle from {}! :3`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}cuddle <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
cuddlelinks = ["https://i.imgur.com/GWNWcLH.gif",
               "https://i.imgur.com/i3Eqqgz.gif",
               "https://i.imgur.com/GpFk6fE.gif",
               "https://i.imgur.com/mc3Z7wf.gif",
               "https://i.imgur.com/N5JYB5r.gif",
               "https://i.imgur.com/PGp8JYq.gif"]

# %help
client.remove_command('help')
@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0x9b0019, description= "")
    msg.title = ""
    msg.add_field(name=":incoming_envelope: ", value="`You can see all commands in the #eclipse-commands channel!`")
    msg.set_footer(text=footer_text)
    await client.say(embed=msg)
    print("============================================================")
    print("}help")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# %gay
@client.command(pass_context=True)
async def gay(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0x9b0019, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name=":warning: ", value="`%gay`")
    else:
        msg.add_field(name=":gay_pride_flag:", value="`I'd say {} is {}% gay`".format(args, random.randint(0, 110)))
    await client.say(embed=msg)
    print("============================================================")
    print("}gay")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

@client.event
async def on_message(message):
    contents = message.content.split(" ") #contents is a list type
    for word.upper() in chat_filter:
        if not message.author.id in bypass_list:
            try:
                await client.send_message(message.channel, "Then talk...")
                
chat_filter = ["CHAT IS DEAD", "CHAT DEAD", "DEAD CHAT"]
bypass_list = []

client.run(os.environ['BOT_TOKEN'])
