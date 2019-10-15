import discord
import varlarvs
import tokenim
import time
import datetime

client = discord.Client()
botacmazamani = None
kul_aktiviteleri = {}
oyunbildirimi = 463052720933306379


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
            if len(mesajlarınhepsi) == 1:
                ylnck = msjyollayan.avatar_url
            elif len(mesajlarınhepsi) == 2:
                fonksiyona = varlarvs.avatar(mesajlarınhepsi[1])
                ylnck = client.get_guild(463052720509812736).get_member(fonksiyona).avatar_url
        elif mesaj == "ikon":
            ylnck = message.guild.icon_url
        elif mesaj in varlarvs.oynamalar:
            ylnck = varlarvs.nabiyom(msjyollayan.activity)
        elif mesaj == "ping":
            ylnck = str(round(client.latency, 2)) + " saniye"
        elif mesaj == "pingle":
            # varlarvs.pingle()
            ylnck = "__**pinglemek benim ne haddime!!**__\n \t\t\t_(şaka şaka daha beceremiyorum pinglemeyi)_"
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
            ylnck = "şuan boşum"
        elif mesaj == "latilong":
            ylnck = varlarvs.latilongsorgula(mesajlarınhepsi[1])
        elif mesaj == "para":
            if len(mesajlarınhepsi) == 1:
                ylnck = "eksik veri girdin"
            elif len(mesajlarınhepsi) == 4:
                ylnck = varlarvs.paracevir(mesajlarınhepsi[1], mesajlarınhepsi[2], mesajlarınhepsi[3])
            elif len(mesajlarınhepsi) == 3:
                ylnck = varlarvs.paracevir(mesajlarınhepsi[1], mesajlarınhepsi[2], "1")
            else:
                ylnck = "hatalı"
        elif mesaj == "çık":
            if message.author.id == 134323487085953025:
                ylnck = "bb ben kaçar"
                await message.channel.send(ylnck)
                print("---BOT KAPATILDI---")
                await client.logout()
                return
            else:
                ylnck = "#play sen kimsin ya"
                await message.channel.send(ylnck)
                return

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
                    await member.guild.get_channel(oyunbildirimi).send(yollancak)
                kul_aktiviteleri[member] = member.activity.name
            else:
                kul_aktiviteleri[member] = ""


@client.event
async def on_member_join(member):
    kanalidsi = 531912642772860938
    await member.guild.get_channel(kanalidsi).send("<@{}>, kanala hoşgeldin!".format(member.id))


@client.event
async def on_ready():
    global kul_aktiviteleri, botacmazamani
    for i in client.get_guild(463052720509812736).members:
        if i.bot:
            continue
        kul_aktiviteleri.update({i.id: i})
    botacmazamani = datetime.datetime.now()
    print('Logged in as')
    print("--" + client.user.name + "--")
    print("#" + client.user.discriminator)
    print('------')


client.run(tokenim.token)
