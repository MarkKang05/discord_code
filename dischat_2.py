##ㅁㅌ처리봇 메인코드

import asyncio
import discord
import random
from discord.ext import commands
import time
import random
import os


#client = discord.Client()
bad = ['민트','민초','민트초코','mint','mincho','mint cho'] 
warning_msg = ['적당히 해라...휴먼...','봇도 힘들답니다..','10초 후 자폭합니다','미쳤습니까? 휴먼?','I will kill YOU','제 개발자한테 이를거에요','암유발자 최고']
toggle = 0
global count
global start
count = 0
start = 0

#token = "NzU2ODIwNzMzNDUxMTczOTc5.X2XaOw.WuMjiboEwZkM1WkGPx0uItPSRLo" #채금봇
token = "NzU2MzIwNDQ0MjgxMzg5MDU4.X2QITQ.P_5uJ70BeXrT6rc1d4Jhh_8Tl8M" #민트처리봇


##
client = commands.Bot(command_prefix= '~')


@client.event
async def bt(games):
    await client.wait_until_ready()
    #await client.change_presence(activity=discord.Game(name='민트 처리'))
    while not client.is_closed():
        for g in games:
            await client.change_presence(status = discord.Status.online, activity = discord.Game(g))
            await asyncio.sleep(5)

#@client.event
@client.event
async def on_ready():
    await bt(['민트 처리','암유발자 최고','민트 혐오'])

@client.event
async def on_message(message): 
    message_contant=str(message.content).lower()

    global count
    global start

    if '!민트야' in message_contant[:4]:
        
        
        if '밥먹자' in message_contant:
            await message.channel.send('구구구구 마시쪙')
        
        elif '안녕' in message_contant:
            author = str(message.author.nick)

            if author == "None":
                author = str(message.author)
                author = author[:-5]
            await message.channel.send('안녕하세요. {}님'.format(author))
        elif '엄준식' in message_contant:
            await message.channel.send("엄마가 준비한 식사")
            
        elif 'wol-desktop' in message_contant:
            os.system("wakeonlan BC:5F:F4:5C:85:B9")

        else:
            else_msg = ['저는 AI 봇이 아니니까 시리한테나 말거세요.','에?','?']
            random_value = random.randrange(0,len(else_msg))
            await message.channel.send('{}'.format(else_msg[random_value]))
        
    
    else:
        for i in bad: 
            if i in message_contant: 

                author = str(message.author.nick)

                if author == "None":
                    author = str(message.author)
                    author = author[:-5]

                await message.delete()
                await message.channel.send('```bash\n"ㅁㅌ"는 금지어입니다. 삭제합니다.\n"{}"님, 경고입니다.\n깨끗한 서버를 위해 더 노력하겠습니다!```'.format(author))
    
                if count == 0:
                    start = time.time()
                count += 1
                end = time.time()
                if (end-start) >= 8.00:
                    count = 0

                while (end-start) < 8.00:
                    #print("dd")
                    if count >= 4:
                        random_value = random.randrange(0,len(warning_msg))
                        if random_value == 3:
                            await message.channel.send(file=discord.File('./pic/robot.jpg'))
                        await message.channel.send("```diff\n-{}\n```".format(warning_msg[random_value]))
                        count = 0
                    else:
                        break

            else:
                msg = message_contant
                i=0
                j=0
                for i in range(0,len(msg)):
                    if msg[i] == '민':
                        ads = msg.find('민')
                        for j in range(ads, len(msg)):
                            if (msg[j] == '트'):
                                #if (msg[j] == '초'):


                                author = str(message.author.nick)

                                if author == "None":
                                    author = str(message.author)
                                    author = author[:-5]
                                
                                await message.delete()
                                await message.channel.send('```bash\n"ㅁㅌ"는 금지어입니다. 삭제합니다.\n"{}"님, 경고입니다.\n깨끗한 서버를 위해 더 노력하겠습니다!```'.format(author))   
        
    
        
            
            #await message.channel.send(count)
            




client.run(token,bot = True)
            

             


