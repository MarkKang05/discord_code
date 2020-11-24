##ㅁㅌ처리봇 메인코드

import asyncio
import discord
import random
from discord.ext import commands
import time
import random
import os
from bs4 import BeautifulSoup
from pprint import pprint
import requests
import re
from discord.utils import get

import wmodule
import classcode

#client = discord.Client()
bad = ['민트','민초','민트초코','mint','mincho','mint cho'] 
warning_msg = ['적당히 해라...휴먼...','봇도 힘들답니다..','10초 후 자폭합니다','미쳤습니까? 휴먼?','I will kill YOU','제 개발자한테 이를거에요','암유발자 최고']
toggle = 0
global count
global start
weather_count = 0
count = 0
start = 0

token = "NzU2ODIwNzMzNDUxMTczOTc5.X2XaOw.WuMjiboEwZkM1WkGPx0uItPSRLo" #채금봇
#token = "NzU2MzIwNDQ0MjgxMzg5MDU4.X2QITQ.P_5uJ70BeXrT6rc1d4Jhh_8Tl8M" #민트처리봇


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
    if message.author.bot: #만약 메시지를 보낸사람이 봇일 경우에는
        return None #동작하지 않고 무시합니다.
    message_contant=str(message.content).lower()

    global count
    global start
    global weather_count
    

    if weather_count == 1:
        w_list = []
        w_list = wmodule.weather(message_contant)
        try:
            await message.channel.send(weather_send(w_list))
        except:
            w_list = wmodule.weather('서울시 강남구')
            await message.channel.send(weather_send(w_list))
            await message.channel.send('주소를 잘못 입력하셔서 서울시 강남구 기준으로 말씀드렸어요 :)')
        del w_list
        weather_count = 0


    if '!민트야' in message_contant[:4]:
        if(str(message.author)=="암유발자#0112"):
            um_list = ['@아잉봇 우리 개발자님이 나쁜 사람이랑 말하지 말랬지...?','누구....?','무시할게^^','']
            um_random_value = random.randrange(0,len(um_list)-1)
            await message.channel.send('{}'.format(um_list[um_random_value]))
            await message.channel.send('{} 그래도 명령은 들어줄게'.format(str(message.author.mention())))
        #print(author)
        
        
        
        if '밥먹자' in message_contant:
            await message.channel.send('구구구구 마시쪙')
        
        elif '안녕' in message_contant:
            author = str(message.author.nick)
            if author == "None":
                author = str(message.author)
                author = author[:-5]
            await message.channel.send('안녕하세요. {}님'.format(author))


        elif '과목' in message_contant:
            await message.channel.send(classcode.all_class_code())


        elif classcode.code_if(message_contant[5:]):
            await message.channel.send(classcode.class_code(message_contant[5:]))


        elif '날씨' in message_contant:
            weather_count = 1
            await message.channel.send('>>> 지역을 입력해주세요(@@시 @@구):')


        elif '코로나' in message_contant:
            html = requests.get('http://ncov.mohw.go.kr/')
            soup = BeautifulSoup(html.text, 'html.parser')
            cor = soup.find('span',{'class': 'before'}).text
            del soup
            cor = re.findall("\d+",cor)
            await message.channel.send('전일대비 {}명 늘었습니다'.format(cor[0]))
            #print(cor[0])


        elif '온도' in message_contant:
            cpu_temp = int(os.popen('cat /sys/class/thermal/thermal_zone0/temp').read())
            gpu_temp = str(os.popen('/opt/vc/bin/vcgencmd measure_temp').read())
            await message.channel.send('CPU:{}°C\nGPU:{}°C'.format(cpu_temp/1000,gpu_temp[5:9]))


        elif '엄준식' in message_contant:
            await message.channel.send("준식이 놀리지 마셈.ㅅㄱ")
            


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
            

def weather_send(w_list):

    return ('>>> '
            +"=============================="+'\n'
            +w_list[0]+" 날씨 정보입니다."+'\n'
            +"=============================="+'\n'
            +"현재온도: "+w_list[1]+'\n'
            +"체감온도: "+w_list[2]+'\n'
            +"오전/오후 온도: "+w_list[3]+'/'+w_list[4]
            +"현재 상태: "+w_list[5]+'\n'
            +"현재 자외선 지수: "+w_list[6]+'\n'
            +"현재 미세먼지 농도: "+w_list[7]+'\n'
            +"현재 초미세먼지 농도: "+w_list[8]+'\n'
            +"현재 오존 지수: "+w_list[9]+'\n'
            +"=============================="+'\n'
            +w_list[0]+" 내일 날씨 정보입니다."+'\n'
            +"=============================="+'\n'
            +"내일 오전 온도: "+w_list[10]+'\n'
            +"내일 오전 상태: "+w_list[11]+'\n'
            +"내일 오후 온도: "+w_list[12]+'\n'
            +"내일 오후 상태: "+w_list[13]+'\n'
            
            ) 



client.run(token,bot = True)
            

             


