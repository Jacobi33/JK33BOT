import discord
from discord.ext import commands
import time
import random
from random import randint
from random import choice
import json
from discord.ext.commands.cooldowns import BucketType
import typing
from discord.utils import get
import os
import traceback
import sys
import subprocess
import aiohttp
import asyncio


bot = commands.Bot(command_prefix='?', description='Jacboi bot is here!')
bot.remove_command('help')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(name=f"on {len(set(bot.get_all_members()))} | ?help", type=discord.ActivityType.watching), status=discord.Status.online)
    print("Bot is ready")

   
@bot.event
async def on_message(message):
   if message.content.startswith("רון"):
       channel = message.channel
       await channel.send("?אולי אוכל לענות לך במקומו")

   if message.content.startswith("לילה טוב"):
       channel = message.channel
       await channel.send(":last_quarter_moon_with_face: לילה טוב גם לך")


   if message.content.startswith("בוקר טוב"):
       channel = message.channel
       await channel.send(":sunny:  בוקר טוב גם לך")

   if message.content.startswith("jacobi33"):
       channel = message.channel
       await channel.send("?אני פה במקומו. איך אפשר לעזור")
   await bot.process_commands(message)




@bot.command()
async def ping(ctx):
    ping1 = randint(1, 1000)
    await ctx.send(f'Pong! `{ping1}ms`')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title='Jacobi33 - BOT Commands' , description='**• Discord Bot by:**<@396693859436068875>  \n **• Teacher:**<@326736523494031360>\n **• Prefix:** ?' , color=0x52d2db)
    embed.add_field(name='• General Commands:' , value='`?help`\n `?helpme`\n `?bot`\n `?owner`\n `?serverinfo`\n  `?hebrules`\n `?engrules`\n `?dis`\n `?steam`\n `?info[@user]`\n `?pricelist`\n ' , inline=False)
    embed.add_field(name='• Staff Commands' , value='`?say [text]` \n `?clear [amount]`\n ' , inline=False)
    embed.add_field(name='• Administration Commands' , value= '`?kick [@user]`\n `?ban [@user]` \n `?editmassage [ID massage]`\n `?warn [@user + reason]`\n `?vote`\n `?mute`\n `?unmute`' , inline=False)
    embed.add_field(name='• Fun Commands' , value='`?gay[@user]`\n `?ping`\n `?slap[@user] [reason]`\n `?avatar [@user]`\n `magic8ball[question]`\n `?joke`\n `?meme`\n `?timer`\n `?coinflip`' , inline=False)
    embed.add_field(name="• Music commands" , value='`?play`\n `?skip`\n `?stop`\n `?np`\n `?queue`\n `?pause`\n `?resume`\n **《Music Commands Will Be Use Only In A Music Chat!》**') 
    embed.set_footer(text='© Help sytem', icon_url=ctx.bot.user.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def helpme(ctx):
    await ctx.send(f'<@&516686634973134859>, {ctx.author.mention} needs your help!')

@bot.command(name='bot')
async def _bot(ctx):
    embed = discord.Embed(
        title = 'Bot Information',
        description = '**Heres The Bot Information:**',
        color=0x52d2db

    )

    embed.set_footer(text='© Bot Information', icon_url=ctx.bot.user.avatar_url)
    embed.set_image(url='https://cdn.discordapp.com/attachments/508384956016492563/538027556297768980/Jacobi33_-_BOT.gif')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/508384956016492563/538027556297768980/Jacobi33_-_BOT.gif')
    embed.set_author(name='Jacobi33 - BOT',
    icon_url='https://cdn.discordapp.com/attachments/508384956016492563/532860958071062538/unknown.png')
    embed.add_field(name='servers', value=len(bot.guilds) , inline=False)
    embed.add_field(name='Online Users' , value=str(len({m.id for m in bot.get_all_members() if m.status is not discord.Status.offline})) , inline=False)
    embed.add_field(name='Channels' , value=f"{sum(1 for g in bot.guilds for _ in g.channels)}" , inline=False)
    embed.add_field(name='Total Users', value=len(bot.users) , inline=False)
    embed.add_field(name="Bot Latency", value=f"{bot.ws.latency * 500:.0f} ms" , inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def owner(ctx):
    embed = discord.Embed(title= '**Jacobi33 - BOT : Owner**' , description= 'My owner is: <@396693859436068875>\n If you need something you can ask him :smile:', color=0x52d2db)
    embed.set_footer(text='© Owner sytem', icon_url=ctx.bot.user.avatar_url)
    await ctx.author.send(embed=embed)
    
    embed = discord.Embed(description=":white_check_mark: Owner's Information was sent in DM." , color=0x41d31f)
    await ctx.send(embed=embed)




@bot.command()
async def steam(ctx):
    await ctx.author.send("**My owner's steam:** \n profilehttps://steamcommunity.com/profiles/76561198417142624/")

    embed = discord.Embed(description=':white_check_mark: Steam was sent in DM.' , color=0x41d31f)
    await ctx.send(embed=embed)



@bot.command()
async def serverinfo(ctx):
    server = ctx.message.guild
    channel_count = len([x for x in ctx.guild.channels if type(x) == discord.channel.TextChannel])
    role_count = len(ctx.guild.roles)
    emoji_count = len(ctx.guild.emojis)
    embed = discord.Embed(description="**__Server Info__**" , color=0x52d2db)
    embed.add_field(name="Server Name", value=ctx.guild.name , inline=False)
    embed.add_field(name='Server Owner', value=ctx.guild.owner , inline=False)
    embed.add_field(name="Server ID", value=ctx.guild.id , inline=False)
    embed.add_field(name="Roles", value=len(ctx.guild.roles) , inline=False)
    embed.add_field(name="Members", value=len(ctx.guild.members) , inline=False)
    embed.add_field(name="Text Channels", value=str(channel_count)  , inline=False)
    embed.add_field(name='Emotes', value=str(emoji_count), inline=False)
    embed.add_field(name="Region", value=ctx.guild.region , inline=False)
    embed.add_field(name="Verification Level", value=ctx.guild.verification_level, inline=False)
    embed.add_field(name="Created At", value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S') , inline=False)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)


@commands.has_permissions(administrator=True)
@bot.command()
async def ggg(ctx):
    embed = discord.Embed(title= ':pushpin: חוקי שרת הדסקורד' , description='אי ידיעת החוקים אינה פותרת מעונש \n ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ \n 1. אין לאיים על גולש אחר, איום נחשב בין היתר כעבירה פלילית ויטופל בהתאם \n 2. אין להטריד גולש אשר אינו מעוניין בקשר עמכם \n 3. יש לשמור על שפה נאותה, אין לקלל או לפגוע במשתמשים \n 4. !אין לפרסם בשום דרך שהיא קהילות מתחרות. כדוגמה (שרתי דיסקורד טיםספיק וכו...) אסור \n 5. אין לפרסם פרטים אישיים שלכם או של משתמשים אחרים \n 6. על כל משתמש לדבר בכבוד כלפי אדמינים ומשתמשים אחרים בשרת \n 7. יש לכתוב את הדברים המתאימים לחדר המתאים \n 8. אין להשתמש בשום תוכנה לשינוי קול \n 9. אין להשתמש בתמונות פרופיל פוגעניות וחושפניות \n 10. אין לפרסם שידורים ללא רשות \n 11. אין להספים או להציף את הצאט של השרת. \n 12. אין לפרסם פרטיים אישיים שלכם או של משתמשים אחרים \n 13.אין לצעוק במיקרופון בשום חדר \n 14.אין לתייג אונרים אלא אם מפנים אליהם \n 15.אין להשמיע מוסיקה בחדרים לא מתאימים לכך \n 16.אסור להספים \n 17.אין להשתמש בתוכנה לשינוי קול \n 18.אסור לבקש רולים \n 19.אסור לפעול בגזענות \n 20. יש לכבד את כל חוקי השרת הגלובאליים , כל חוק וחוק תקף ואין לעבור עליו \n ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ \n' , color=0x52d2db)
    embed.add_field(name="===עונשים ===" , value='בפעם הראשונה,עבירה על החוק -אזהרה \n Muted-בפעם השניה,עבירה על החוק \n בפעם השלישית,עבירה על החוק- קיק \n בפעם הרביעית,עבירה על החוק -באן \n ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ \n מוזמנים לפרסם את שרת הדיסקורד \n https://discord.gg/ZXXTyW7 \n \n ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬' )
    embed.set_footer(text='© All credit to Jacobi33', icon_url=ctx.bot.user.avatar_url)
    await ctx.send(embed=embed)


@bot.event
async def on_member_join(member):
    channel = member.guild.get_channel(431934639490203678)
    embed = discord.Embed(title='New Member Joined+', description=f'Hey {member.mention}, Welcome to **{member.guild.name}** :tada: Enjoy :tada: \nWe hope that you will enjoy :smiley:\n Read the <#501833051676999680> before activity!\n We are now **{len(member.guild.members)}** members! ' , color=0x52d2db)
    embed.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=embed)


@bot.event
async def on_member_remove(member):
    channel = member.guild.get_channel(431934639490203678)
    embed = discord.Embed(title='Server Member Left-', description=f'Bye Bye {member.mention}, The user left the server \nWe are now **{len(member.guild.members)}** members!' , color=0x52d2db)
    embed.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=embed)


@bot.command()
async def engrules(ctx):
    embed = discord.Embed(title= ':pushpin: Server rules' , description="The ignorance of the rules does not solve the problem \n ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ \n 1. Do not threaten another surfer, a threat is considered among other things \n 2. Do not harass a surfer who does not want to contact you \n 3. Maintain proper language, do not curse or harm users \n 4. Do not advertise in any way from competitors. As an example is not allowed \n 5. Do not post personal information to you or other users \n 6. Every user must respectfully invite to steam and other uses \n 7. Write the appropriate things in the appropriate room \n 8. Do not use any sound-changing software \n 9. Do not use abusive and revealing profile images \n 10. No broadcasts may be published without permission \n 11. Do not add or flood the server's chat. \n 12. Do not post personal information to yourself or other users \n 13. Do not shout in a microphone in any room \n 14. Do not label Users unless directed to them \n 15. Do not play music in unsuitable rooms \n 16. Do not spam! \n 17. Do not use the software to change the sound \n 18. Do not ask for roles \n 19. Prohibition of acts of racism \n 20. All global server rules must be respected, any applicable law and law should not be violated \n ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ \n" , color=0x52d2db)
    embed.add_field(name="=== Punishments ===" , value='For the first time, breaking the rules - a warning \n The second time, breaking the rules - Muted \n For the third time,breaking the rules - kick \n For the fourth time, breaking the rules - ban  \n ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ \n You are invited to publish the discord server! \n https://discord.gg/fPTApRf \n \n ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬' )
    embed.set_footer(text='© All rights belong to my programmer - Jacobi33 ', icon_url=ctx.bot.user.avatar_url)
    await ctx.author.send(embed=embed)

    embed = discord.Embed(description=':white_check_mark: English Rules were sent in DM.' , color=0x41d31f)
    await ctx.send(embed=embed)


@bot.command()
async def hebrules(ctx):
    embed = discord.Embed(title= ':pushpin: חוקי שרת הדסקורד' , description='אי ידיעת החוקים אינה פותרת מעונש \n ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ \n 1. אין לאיים על גולש אחר, איום נחשב בין היתר כעבירה פלילית ויטופל בהתאם \n 2. אין להטריד גולש אשר אינו מעוניין בקשר עמכם \n 3. יש לשמור על שפה נאותה, אין לקלל או לפגוע במשתמשים \n 4. !אין לפרסם בשום דרך שהיא קהילות מתחרות. כדוגמה (שרתי דיסקורד טיםספיק וכו...) אסור \n 5. אין לפרסם פרטים אישיים שלכם או של משתמשים אחרים \n 6. על כל משתמש לדבר בכבוד כלפי אדמינים ומשתמשים אחרים בשרת \n 7. יש לכתוב את הדברים המתאימים לחדר המתאים \n 8. אין להשתמש בשום תוכנה לשינוי קול \n 9. אין להשתמש בתמונות פרופיל פוגעניות וחושפניות \n 10. אין לפרסם שידורים ללא רשות \n 11. אין להספים או להציף את הצאט של השרת. \n 12. אין לפרסם פרטיים אישיים שלכם או של משתמשים אחרים \n 13.אין לצעוק במיקרופון בשום חדר \n 14.אין לתייג אונרים אלא אם מפנים אליהם \n 15.אין להשמיע מוסיקה בחדרים לא מתאימים לכך \n 16.אסור להספים \n 17.אין להשתמש בתוכנה לשינוי קול \n 18.אסור לבקש רולים \n 19.אסור לפעול בגזענות \n 20. יש לכבד את כל חוקי השרת הגלובאליים , כל חוק וחוק תקף ואין לעבור עליו \n ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ \n' , color=0x52d2db)
    embed.add_field(name="===עונשים ===" , value='בפעם הראשונה,עבירה על החוק -אזהרה \n Muted-בפעם השניה,עבירה על החוק \n בפעם השלישית,עבירה על החוק- קיק \n בפעם הרביעית,עבירה על החוק -באן  \n ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ \n מוזמנים לפרסם את שרת הדיסקורד\n https://discord.gg/fPTApRf \n \n ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬' )
    embed.set_footer(text=' © Jacobi33 כל הזכויות שייכות למתכנת שלי ', icon_url=ctx.bot.user.avatar_url)
    await ctx.author.send(embed=embed)

    embed = discord.Embed(description=':white_check_mark: Hebrew Rules were sent in DM.' , color=0x41d31f)
    await ctx.send(embed=embed)


@commands.has_permissions(administrator=True)
@bot.command()
async def gggg(ctx):
    embed = discord.Embed(title= ':ribbon: רולים בשרת :ribbon:' , description=':arrow_down_small::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::arrow_down_small: \n <@&423521102040530944> - בעל השרת \n <@&519437249536983071> - הבוט הראשי של השרת \n <@&502779628419547146> - מנהל השרת והמתכנת \n <@&519888471163142154> - שומרי השרת והסדר \n <@&523853936948543504> - עוזר פעיל בשרת \n <@&514769692985131019> - שומרי סדר וארגון והעוזרים \n <@&523853950550540289> - אחראי לפניות עזרה בשרת \n <@&517745634359640094> - אנשי שיתוף הפעולה \n <@&511152645524815883> - יוטיובר גדול עם לפחות 500 סאבים \n <@&517380474088325130> - יוטיובר מתחיל עם לפחות 200 סאבים \n <@&519899824741416961> - תורמים \n :heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign: \n @everyone \n :heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign:' , color=0x52d2db)
    embed.set_footer(text='© roles sytem', icon_url=ctx.bot.user.avatar_url)
    await ctx.send(embed=embed)




@bot.command()
async def dis(ctx):
    embed = discord.Embed(title="**My Owner's discord server:**" , description="https://discord.gg/fPTApRf \n pls invite your friends to the server!" , color=0x52d2db)
    await ctx.send(embed=embed)

@bot.command()
async def gay(ctx, user: discord.Member = None):
        if not user:
            user = ctx.author
        gay1 = randint(1, 100)
        embed = discord.Embed(title='**Gay Polygraph**', color=0x52d2db)
        embed.add_field(name='The result is ready!' , value=f'{user.mention} is **{gay1}%** gay :tongue: ', inline=False)
        await ctx.send(embed=embed)


@bot.command()
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.message.delete()
    await ctx.send('{} just got slapped for {}'.format(slapped, reason))


@commands.cooldown(1 ,3, BucketType.user)
@commands.has_permissions(manage_messages=True)
@bot.command(description="Clears X messages.")
async def clear(ctx, num: int, target: discord.Member=None):
    if num > 500 or num < 0:
        return await ctx.send("Invalid amount. Maximum is 500.")
    def msgcheck(amsg):
        if target:
           return amsg.author.id == target.id
        return True
    deleted = await ctx.channel.purge(limit=num, check=msgcheck)
    embed = discord.Embed(title='Someone deleted messages.. <:recycle:533234706385469471>' , color=0x52d2db)
    embed.add_field(name='Executor' , value=f'{ctx.author.mention}' , inline=False)
    embed.add_field(name='Deleted messages' , value=f'{len(deleted)}' , inline=False)
    await ctx.send(embed=embed, delete_after=20)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        time = gettime(error.retry_after)
        return await ctx.send(f'{ctx.author.mention} You are writing too fast, Chill dude.. \n wait more {time} ')
    if isinstance(error, commands.CheckFailure):
        return await ctx.send( ' :x: you are missing **permissions** for this command..')
@commands.cooldown(1 ,3, BucketType.user)
@commands.has_permissions(manage_messages=True)
@bot.command()
async def send(ctx, *, arg):
    await ctx.message.delete()
    await ctx.send(arg)


@commands.has_permissions(kick_members=True)
@bot.command()
async def kick(ctx, user: discord.Member):
    if (ctx.author.top_role > user.top_role) or (ctx.guild.owner == ctx.author):
        await user.kick()
    embed = discord.Embed(title='Someone just kicked from the server!' , color=0x52d2db)
    embed.add_field(name='Admin:' , value=f'{ctx.author.mention}' , inline=False)
    embed.add_field(name='was kicked:' , value=f'{user.mention}' , inline=False)
    await ctx.send(embed=embed, delete_after=20)


@commands.has_permissions(ban_members=True)
@bot.command()
async def ban(ctx, user: discord.Member):
    if (ctx.author.top_role > user.top_role) or (ctx.guild.owner == ctx.author):
        await user.ban()
    embed = discord.Embed(title='Someone just banned from the server!' , color=0x52d2db)
    embed.add_field(name='Admin:' , value=f'{ctx.author.mention}' , inline=False)
    embed.add_field(name='was banned:' , value=f'{user.mention}' , inline=False)
    await ctx.send(embed=embed, delete_after=20)


@commands.has_permissions(administrator=True)
@bot.command()
async def mute(ctx, member: discord.Member = None):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not member:
        member = ctx.author
        return
    await member.add_roles(role)
    await ctx.send(f'`✔️` {member.mention} Has been Muted!')


@commands.has_permissions(administrator=True)
@bot.command()
async def unmute(ctx, member: discord.Member = None):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not member:
        member = ctx.author
        return
    await member.remove_roles(role)
    await ctx.send(f'`✔️` {member.mention} Has been UnMuted!')

@bot.command()
async def event(ctx):
    member = ctx.author
    role = discord.utils.get(ctx.guild.roles, name="event")
    await member.add_roles(role)
    await ctx.send(f'`✔️` שמח לשמוע שאתה משתתף בתחרות\n בהצלחה')


@bot.command()
async def avatar(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
    embed = discord.Embed(title="**{}'s Avatar**".format(user.name) , color=0x52d2db)
    embed.set_image(url=user.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def info(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
    embed = discord.Embed(title="{}'s info".format(user.name) , description="**Here's what I could find...**" , color=0x52d2db)
    embed.add_field(name="Name" , value=user.name, inline=True)
    embed.add_field(name="ID" , value=user.id, inline=True)
    embed.add_field(name="status" , value=user.status, inline=True)
    embed.add_field(name="Joined" , value=user.joined_at)
    embed.add_field(name="Created At" , value=user.created_at)
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)


@commands.cooldown(1 ,3, BucketType.user)
@commands.has_permissions(administrator=True)
@bot.command()
async def editmessage(ctx, id:int, *, newmsg:str):
    try:
        msg = await ctx.channel.get_message(id)
    except discord.errors.NotFound:
        await ctx.send("Couldn't find a message with an ID of `{}` in this channel".format(id))
        return
    if msg.author != ctx.guild.me:
        await ctx.send("That message was not sent by me")
        return
    await msg.edit(content=newmsg)
    await ctx.send("`✔️` Editing succeed.")



@bot.command()
async def magic8ball(ctx):
    await ctx.send(random.choice(["It is certain :8ball:",
                                  "It is decidedly so :8ball:",
                                   "Without a doubt :8ball:",
                                   "Yes, definitely :8ball:",
                                   "You may rely on it :8ball:",
                                   "As I see it, yes :8ball:",
                                   "Most likely :8ball:",
                                   "Outlook good :8ball:",
                                   "Yes :8ball:",
                                   "Signs point to yes :8ball:",
                                   "Reply hazy try again :8ball:",
                                   "Ask again later :8ball:",
                                   "Better not tell you now :8ball:",
                                   "Cannot predict now :8ball:",
                                   "Concentrate and ask again :8ball:",
                                   "Don't count on it :8ball:",
                                   "My reply is no :8ball:",
                                   "My sources say no :8ball:",
                                   "Outlook not so good :8ball:",
                                   "Very doubtful :8ball:"]))






@commands.has_permissions(administrator=True)
@bot.command()
async def vote(ctx, *, args):
    await ctx.message.delete()
    embed = discord.Embed(title='Use the reactions to vote!' , description=args , color=0x52d2db)
    data = ['https://can2-prod.s3.amazonaws.com/uploads/data/000/035/481/original/vote_now_button.jpg' , 'https://s3-eu-west-1.amazonaws.com/nusdigital/article/images/18642/medium/vote_now.png' , 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTV5niSmeAs5lqYg8URLASxKB7YYovL34xVaPk7qyvcyS6BLSIM' , 'https://i2.wp.com/organhistoricalsociety.org/wp-content/uploads/2018/11/vote-now.png?w=1080&ssl=1' , 'http://nejetaa.com/wp-content/uploads/2016/11/Vote.jpg' , 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgVVR9SBJXEo1vb9Yw5qtYADIOmV1og-xB2Q4GxJasQQUVBIs_']
    embed.set_thumbnail(url=(choice(data)))
    embed.set_footer(text='© Vote system | Question by {}'.format(ctx.author.name))
    msg = await ctx.send(embed=embed)
    await msg.add_reaction(emoji="✅")
    await msg.add_reaction(emoji="❌")



@bot.command()
async def joke(ctx):
    embed = discord.Embed(title='Joke' , description=(random.choice(["Dad I’m hungry’ … ‘Hi hungry I’m dad",
                                                                  "Why are pirates called pirates? Because they arrr!",
                                                                  "Why did the girl smear peanut butter on the road? To go with the traffic jam.",
                                                                  "Where did you learn to make ice cream? Sunday school.",
                                                                  "How can you tell a vampire has a cold? They start coffin.",
                                                                  "A man walks into a bar and orders helicopter flavor chips. The barman replies “sorry mate we only do plain”",
                                                                  "I’m reading a book on the history of glue – can’t put it down.",
                                                                  "Camping is intense.",
                                                                  "How many optometrists does it take to change a light bulb? 1 or 2? 1... or 2?",
                                                                  "Don't tell secrets in corn fields. Too many ears around.",
                                                                  "I knew I shouldn't steal a mixer from work, but it was a whisk I was willing to take.",
                                                                  "I just got fired from a florist, apparently I took too many leaves.",
                                                                  '"What time is it?" I dont know... it keeps changing.',
                                                                  'Thanks for explaining the word "many" to me. It means a lot.',
                                                                  'A panda walks into a bar and says to the bartender “I’ll have a Scotch and . . . . . . . . . . . . . . Coke thank you \n \n “Sure thing” the bartender replies and asks “but what’s with the big pause?” \n The panda holds up his hands and says “I was born with them”',
                                                                  'I asked a frenchman if he played video games. He said "Wii"',
                                                                     'What is the similarity between a shrimp and a man? You can enjoy all but the head ',
                                                                     'What is the similarity between a dolphin and a man? They are both said to be intelligent, but no one can prove this'])) , color=0x52d2db)
    await ctx.send(embed=embed)






@bot.command()
async def meme(ctx):
    embed = discord.Embed(title='Funny Meme' , color=0x52d2db)
    embed.set_image(url=random.choice(["https://cdn.discordapp.com/attachments/524286210244476959/540840144643817492/63ea41463fb204e6ded6fdf32cfe775b--minecraft-memes-scene.jpg",
                                                                         "https://cdn.discordapp.com/attachments/524286210244476959/540840165417943040/de28f4b74c6fce3f6b044eabe508a1c2.jpeg",
                                                                         "https://cdn.discordapp.com/attachments/524286210244476959/540840180714700800/images.jpg",
                                                                         "https://cdn.discordapp.com/attachments/524286210244476959/540840198909591562/maxresdefault.jpg",
                                                                         "https://cdn.discordapp.com/attachments/524286210244476959/540840220619440130/27fc4b57b0a209b3c7daec8c53ebce70.jpg",
                                                                         "https://cdn.discordapp.com/attachments/524286210244476959/540840234963959819/41bf5f09c83abc099812163628355baa--holiday-pics-thanksgiving-humor.jpg",
                                                                         "https://cdn.discordapp.com/attachments/524286210244476959/540840248737792000/happy-easter-hilarious-april2014-funny-memes-17.jpg",
                                                                         "https://cdn.discordapp.com/attachments/524286210244476959/540840262172147722/meme_1.jpg",
                                                                         "https://cdn.discordapp.com/attachments/524286210244476959/540840302819147776/epic-minecraft-meme-7.jpg",
                                                                         "https://cdn.discordapp.com/attachments/524286210244476959/540840358075170826/884f441130e1b7e621aad4f95c61c947.jpg",
                                                                        "https://cdn.discordapp.com/attachments/524286210244476959/540840373493301248/5a560ee77a2be.jpeg",]))
    await ctx.send(embed=embed)



@commands.cooldown(1 ,3, BucketType.user)
@commands.has_permissions(administrator=True)
@bot.command()
async def warn(ctx, members: commands.Greedy[discord.Member], *, reason=':x: `Error! Missing reason`'):
    warned = ", ".join(x.mention for x in members)
    user = warned
    await ctx.send(':white_check_mark: **{}** has been warned for **{}**.' .format(warned, reason))
    embed = discord.Embed(description='**Member:** {} \n **Executor:** {} \n **Reason:** {}'.format(user, ctx.author.mention, reason), color=0x52d2db)
    embed.set_author(name='Warn Action' , icon_url=ctx.bot.user.avatar_url)
    embed.set_footer(text='© Warn sytem')
    await bot.get_channel(503243563686166548).send(embed=embed)



@commands.cooldown(1 ,3, BucketType.user)
@bot.command()
async def scrims(ctx):
    msg = await ctx.send('**Look what I can do!**')
    await asyncio.sleep(2)
    await msg.edit(content='**5**')
    await asyncio.sleep(2)
    await msg.edit(content='**4**')
    await asyncio.sleep(2)
    await msg.edit(content='**3**')
    await asyncio.sleep(2)
    await msg.edit(content='**2**')
    await asyncio.sleep(2)
    await msg.edit(content='**1**')
    await asyncio.sleep(2)
    await msg.edit(content='**Go go go!!**')



@commands.cooldown(1 ,3, BucketType.user)
@bot.command()
async def hype(ctx):
    await ctx.message.delete()
    msg = await ctx.send('**My name is: Jacobi33 - BOT**')
    await asyncio.sleep(2)
    await msg.edit(content='**My developer is <@396693859436068875> !**')
    await asyncio.sleep(2)
    await msg.edit(content='**I got 22 commands!**')
    await asyncio.sleep(2)
    await msg.edit(content='**You can invite me to your server!**')
    await asyncio.sleep(3)
    await msg.edit(content='**If you want a program bot like me type in the chat:** `?owner` **and send him a message!**')
    await asyncio.sleep(5)
    await msg.edit(content='**Just enjoy my commands :heart: **')
    await asyncio.sleep(2)
    await msg.edit(content='**Wish you enjoy, bye!**', delete_after=4)



@bot.command()
async def pricelist(ctx):
    embed = discord.Embed(title='**Price List**' , color=0x52d2db)
    embed.set_image(url='https://cdn.discordapp.com/attachments/519634805953134592/540150289622237187/aa26de244482c11e.gif')
    await ctx.author.send(embed=embed)

    embed = discord.Embed(description=":white_check_mark: Price List was sent in DM." , color=0x41d31f)
    await ctx.send(embed=embed)



@commands.cooldown(1 ,3, BucketType.user)
@bot.command()
async def timer(ctx, Time: int, *, args):
    embed = discord.Embed(description='**{}**, You set timer for **{}** mintues. reason **{}** '.format(ctx.author.mention, Time, args) , color=0x52d2db)
    await ctx.send(embed=embed)
    await asyncio.sleep(Time*60)
    embed = discord.Embed(description=f'{ctx.author.mention}, **The timer is end!** \n I hope you have succeeded `{args}` in time?' , color=0x52d2db)
    await ctx.send(embed=embed)


@commands.has_permissions(administrator=True)
@bot.command()
async def tempmute(ctx, member: discord.Member, Time: int, *, reason):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)
    embed = discord.Embed(title="Muted" , description="**Member:** {} \n **Executor:** {} \n **Time:** {} \n Reason **{}** ".format(user, ctx.author.mention, Time, args) , color=0x52d2db)
    await ctx.send(embed=embed)
    await asyncio.sleep(Time*60)
    await ctx.send('`✔️` {} Has been Unmuted after {}'.format(user, Time))
    await member.remove_roles(role)
    


@bot.command()
async def coinflip(ctx):
    choices = ["Heads" , "Tails"]
    rancoin = random.choice(choices)
    await ctx.send(rancoin)



@bot.command()
async def Gur(ctx):
    embed = discord.Embed(title='**_Help_**' , color=0x52d2db)
    embed.add_field(name="**_You Can See All The Categories Below!_**" , value="**• To See The General Commands Click On** :gear:\n\n **• To See The Staff Commands Click On** :pencil:\n\n **• To See The Administration Commands Click On** :clipboard:\n\n **• To See The Fun Commands Click On** :ribbon:\n\n **• To Get Back TO Here Click On** :arrows_counterclockwise:")
    msg = await ctx.send(embed=embed)
    await msg.add_reaction(emoji="✅️")
    await msg.add_reaction(emoji="❌")

    

@commands.has_permissions(administrator=True)
@bot.command()
async def game(ctx):
    await ctx.message.delete()
    await bot.change_presence(activity=discord.Activity(name=f"on {len(set(bot.get_all_members()))} | ?help", type=discord.ActivityType.watching), status=discord.Status.online)



@bot.command()
async def youtube(ctx, *args):
    query = 'https://www.youtube.com/results?search_query='
    for word in args:
        query+=word
        if word != args[-1]:
            query+='+'
    await ctx.send(query)



@commands.has_permissions(administrator=True)
@bot.command()
async def giveaway(ctx, *, args):
    await ctx.message.delete()
    embed = discord.Embed(title=args , description='React with :tada: to enter!\n Time remaining: 5 hours ' , color=0x52d2db)
    embed.set_footer(text='© Giveaway system | Question by {}'.format(ctx.author.name))
    msg = await ctx.send(embed=embed)
    await msg.add_reaction(emoji="✅️")



@bot.command()
@commands.has_permissions(administrator=True)
async def say(ctx, *, args):
    await ctx.message.delete()
    await ctx.send(f'{args}')

bot.run(str(os.environ.get('BOT_TOKEN')))
