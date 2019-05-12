import discord
import varlarvs
import tokenim
import time
import datetime

client = discord.Client()
botacmazamani = None
kul_aktiviteleri = {}
mesajatilankanal = 531912642772860938


@client.event
async def on_message(message):
    global mesajatilankanal
    msjyollayan = message.author
    print(msjyollayan.name, ": ", message.content, sep="")
    if msjyollayan == client.user:
        return

    if message.content in varlarvs.hazirlik:
        mesajatilankanal = message.channel
        await message.channel.send(varlarvs.onay)
    elif message.content == "sa":
        ylnck = "as"
        await message.channel.send(ylnck)
    elif message.content.startswith(varlarvs.prefix):
        ylnck = "wrong"
        mesajlarınhepsi = varlarvs.mesajadondur(message.content)
        mesaj = mesajlarınhepsi[0]
        if varlarvs.mesajlarakarsilik.get(mesaj):
            ylnck = varlarvs.mesajlarakarsilik.get(mesaj)
        elif mesaj == "name":
            ylnck = msjyollayan.name
        elif mesaj == "avatar":
            ylnck = msjyollayan.avatar_url
        elif mesaj == "ikon":
            ylnck = message.guild.icon_url
        elif mesaj in varlarvs.oynamalar:
            ylnck = varlarvs.nabiyom(msjyollayan.activity)
        elif mesaj == "ping":
            ylnck = str(round(client.latency, 2)) + " saniye"
        elif mesaj == "pingle":
            varlarvs.pingle()
            ylnck = "pingleniyor..."
        elif mesaj == "botacilisi":
            ylnck = botacmazamani
        elif mesaj == "up":
            ylnck = varlarvs.nekadardirup(botacmazamani)
        elif mesaj == "açılış":
            ylnck = varlarvs.acilis(botacmazamani)
        elif mesaj == "hava":
            if len(mesajlarınhepsi) == 1:
                ylnck = "eksik veri girdin"
            else:
                ylnck = varlarvs.havadark(mesajlarınhepsi[1])
        elif mesaj == "gecici":
            ylnck = mesajlarınhepsi
        elif mesaj == "dene":
            ylnck = type(msjyollayan.activity.start)
        elif mesaj == "site":
            ylnck = "http://zbotwiki.gq"
        elif mesaj == "para":
            if len(mesajlarınhepsi) == 1:
                ylnck = "eksik veri girdin"
            elif len(mesajlarınhepsi) == 4:
                ylnck = varlarvs.paracevir(mesajlarınhepsi[1], mesajlarınhepsi[2], mesajlarınhepsi[3])
            else:
                ylnck = "hatalı"
        elif mesaj == "çık":
            ylnck = "bb ben kaçar"
            await message.channel.send(ylnck)
            print("---BOT KAPATILDI---")
            await client.logout()

        statu = msjyollayan.status.name
        if statu != "online":
            ylnck = ylnck + ", ama <@{}> {} gözüküyorsun haberin olsun".format(msjyollayan.id, statu)

        await message.channel.send(ylnck)


@client.event
async def on_member_update(before, after):
    member = after
    if member.bot:
        return
    if member.guild.name == "Freedom":
        if before.activity != after.activity:
            if after.activity:
                if (not before.activity) or (before.activity.name != after.activity.name):
                    if member.activity.name == "Spotify":
                        return
                    yollancak = varlarvs.oyuntepkisi(kul_aktiviteleri, member)
                    await member.guild.get_channel(mesajatilankanal.id).send(yollancak)
                kul_aktiviteleri[member] = member.activity.name
            else:
                kul_aktiviteleri[member] = ""


@client.event
async def on_member_join(member):
    kanalidsi = 531912642772860938
    await member.guild.get_channel(kanalidsi).send("<@{}>, kanala hoşgeldin!".format(member.id))


@client.event
async def on_ready():
    global kul_aktiviteleri, botacmazamani, mesajatilankanal
    mesajatilankanal = client.get_channel("220661231130771467")
    for i in client.get_guild(135796707580444674).members:
        if i.bot:
            continue
        if not i.activity:
            kul_aktiviteleri.update({i: ""})
        else:
            kul_aktiviteleri.update({i: i.activity.name})
    botacmazamani = datetime.datetime.now()
    print('Logged in as')
    print("--" + client.user.name + "--")
    print("#" + client.user.discriminator)
    print('------')


client.run(tokenim.token)
