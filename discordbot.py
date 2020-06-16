import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("삐릿 토리봇이다")
    game = discord.Game("totori Client")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("토리야 안녕"):
        await message.channel.send("ㅇ")
    if message.content.startswith("토리야 밥사줘"):
        await message.channel.send("니가 사먹어")
    if message.content.startswith("토리야 밥먹어"):
        await message.channel.send("그럼 밥을 사줘")
    if message.content.startswith("토리야 짖어"):
        await message.channel.send("멍")
    if message.content.startswith("토리야 뭐할까"):
        await message.channel.send("치킨 시켜")
    if message.content.startswith("토리야 너 트롤이야"):
        await message.channel.send("ㅇㅉㄹㄱ")
    if message.content.startswith("토리야 마크하자"):
        await message.channel.send("ㅇㅋ ㄱㄱ")
    if message.content.startswith("토리야 너 멍청해"):
        await message.channel.send("응 니가 더^v^")
    if message.content.startswith("토리야 너 빙구야"):
        await message.channel.send("반사")
    if message.content.startswith("토리야 하픽하자"):
        await message.channel.send("레벨링 도와줘 빨리")
    if message.content.startswith("토리야 배워하자"):
        await message.channel.send("아.. 또 배워 완전 잘하는 우리 토리 형님이 캐뤼를 해줘야 겠구만~")
    if message.content.startswith("토리야 스블하자"):
        await message.channel.send("스블 노잼 노오오재애애앰")
    if message.content.startswith("토리야 앉아"):
        await message.channel.send("(털썩)")
    if message.content.startswith("토리야 일어서"):
        await message.channel.send("자다가도 벌떡 일어나는 토리토리!!!!!")
    if message.content.startswith("토리야 빵!"):
        await message.channel.send("(꽥)")
    if message.content.startswith("도배 밴"):
        await message.channel.send("/ban AndrewDS")
    if message.content.startswith("!toribot help"):
        await message.channel.send("채팅으로 '토리야 안녕/밥사줘/밥먹어/짖어/뭐할까/너 트롤이야/마크하자/너 멍청해/너 빙구야/하픽하자/배워하자/스블하자/앉아/일어서/빵!' 를 쳐라 휴먼")
    if message.content.startswith("/DM"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await author.send("ㅎㅇ")



client.run("NzIyMzAzMDMwNTgxNjU3NjYw.XuhHiA.ObJE6D44TdbbHmdsmNfbqVT1y9U")