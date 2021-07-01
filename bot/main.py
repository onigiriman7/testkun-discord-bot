import discord
import os
#import pynacl
#import dnspython
import server
from discord.ext import commands
from chatbot import Chat, register_call
import random
#fucntion that generates random testkun quote
def quotegen():
    lines = []
    with open('testkunmessagedata.txt',encoding='utf-8',errors='ignore') as f:
        lines = f.readlines()
    leng = len(lines)

    return lines[random.randint(0, leng-1)]

prefix = "?"
bot = commands.Bot(command_prefix = prefix)
@register_call("whoIs")
def who_is(query, session_id="general"):
    try:
        return "僕はテストボットだ、これがなにかわからない：" + query
    except Exception:
        pass
    return "ぽきた・・・"+query
template_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"cb","cb.template")
chat=Chat(template_file_path)
@bot.event
async def on_ready():
    print("ぽきた・・・!")
@bot.command(pass_context = True)
async def testkun(ctx,*,message=".."):
    #result = chat.respond(message)
    result = "ぽきた・・・" + quotegen()
    if(len(result)<=2048):
        embed=discord.Embed(title="テストボットくんーAI", description = result, color = (0xF48D1))
        await ctx.send(embed=embed)
    else:
        embedList = []
        n=2048
        embedList = [result[i:i+n] for i in range(0, len(result), n)]
        for num, item in enumerate(embedList, start = 1):
            if(num == 1):
                embed = discord.Embed(title="ChatBot AI", description = item, color = (0xF48D1))
                embed.set_footer(text="Page {}".format(num))
                await ctx.send(embed = embed)
            else:
                embed = discord.Embed(description = item, color = (0xF48D1))
                embed.set_footer(text = "Page {}".format(num))
                await ctx.send(embed = embed)

server.server()
bot.run('ODYwMDIzODc1Nzg1OTgxOTcz.YN1Npg.cq9RIA-RR5kcTheiREav1FzCBbs')
