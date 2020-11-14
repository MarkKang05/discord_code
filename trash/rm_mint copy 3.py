import asyncio
from discord.ext.commands import Bot
import random

bot = Bot("!")

# 생성된 토큰을 입력해준다.
token = "NzU2MzIwNDQ0MjgxMzg5MDU4.X2QITQ.P_5uJ70BeXrT6rc1d4Jhh_8Tl8M"

# 봇이 구동되었을 때 보여지는 코드
@bot.command()
async def test(ctx):
    await ctx.send("Command executed")


bot.run(token)