from discord.ext import commands
import discord
import ffmpeg

 
client = commands.Bot(command_prefix='~')
 
#@bot.command(pass_context=True)
#async def play(ctx):
    #await 
    #voice = await bot.join_voice_channel(ctx.message.author.voice.voice_channel)
    #753600926190927872
    #channel = ctx.message.author.VoiceChannel
    #await bot.VoiceChannel.connect(channel)
    #player = voice.create_ffmpeg_player('music.mp3')
    #player.start()

@client.event
async def on_message(message):
    if message.content.lower() == '~play':
        if message.content.lower() == '~play':
            channel = client.get_channel(753600926190927872)
            await channel.connect()

            voice_client = discord.VoiceClient = discord.utils.get(client.voice_clients)
            audio_source = discord.FFmpegPCMAudio("./pic/toong.mp3")
            if not voice_client.is_playing():
                voice_client.play(audio_source, after=None)

            #vc.play(discord.FFmpegPCMAudio(source="./pic/toong.mp3"))

            #player = vc.create_ffmpeg_player('./pic/music.mp3')
            #player.start()
            #vc.is_playing()
            #vc.pause()
            #vc.resume()
            #vc.stop()
            print("dd")

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

#client.run(TOKEN)

client.run("NzU3NDAzNTg4NzkxMjM4NzU3.X2f5Dw.c7xasfmWQXbaimpfrhJBytzs_iU")