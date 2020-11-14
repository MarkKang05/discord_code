import asyncio
import discord
import random

client = discord.Client()

# 생성된 토큰을 입력해준다.
token = "NzU2MzIwNDQ0MjgxMzg5MDU4.X2QITQ.P_5uJ70BeXrT6rc1d4Jhh_8Tl8M"

# 봇이 구동되었을 때 보여지는 코드
@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print("================")

# 봇이 특정 메세지를 받고 인식하는 코드
@client.command()  
async def info(ctx, user: discord.Member):  
    await ctx.send(f'{user.mention}\'s id: `{user.id}`') 

client.run(token)