import os
import time
import datetime
import json
import urllib.request
import tokenim

prefix = "'"
onay = "oke"


def muzik(muzikadi):
    return "Spotify'dan " + muzikadi + " adlı şarkıyı dinliyorsun."


def oyun(oyunadi):
    return oyunadi + " oynuyorsun."


def nabiyom(aktivitesi):
    if not aktivitesi:
        ylnck = "Hiçbir şey oynamıyorsun"

    if aktivitesi.type.name == "listening":
        ylnck = muzik(aktivitesi.title)
    elif aktivitesi.type.name == "playing":
        ylnck = oyun(aktivitesi.name)
    else:
        ylnck = "Kodlanmadığım bir şey yapıyorsun"
    return ylnck


def oyuntepkisi(before, member):
    if member.activity.name in before.values():
        partilistesi = list()
        yollanacak = None
        for i in before.keys():
            if before[i] == member.activity.name:
                partilistesi.append(i)
        if len(partilistesi) == 1:
            yollanacak = "{}, {} ile {} partisine katıldı!".format(member.display_name, partilistesi[0].display_name,
                                                                   member.activity.name)
        elif len(partilistesi) == 2:
            yollanacak = "{} partiye katıldı. Parti 3 kişi oldu.".format(member.display_name)
        elif len(partilistesi) == 3:
            yollanacak = "{} partiye katıldı. Squad tamamlandı!".format(member.display_name)
        elif len(partilistesi) == 4:
            yollanacak = "{}, {} squad'ına dahil oldu. Secret hitler mi giriyolar yoksa".format(member.display_name,
                                                                                                member.activity.name)
        return yollanacak
    else:
        return "{} {} oynamaya başladı".format(member.display_name, member.activity.name)


def paracevir(cevirme1, cevirme2, para):
    currencyurl = "https://free.currencyconverterapi.com/api/v6/convert?compact=ultra&apiKey="
    cevirme1 = cevirme1.upper()
    cevirme2 = cevirme2.upper()
    para = float(para)
    ceviriyazimi = cevirme1 + "_" + cevirme2
    urlac = urllib.request.urlopen(currencyurl + tokenim.currencyapi + ceviriyazimi)
    veri = json.loads(urlac.read().decode())
    cevrik = round(veri[ceviriyazimi], 2)
    carpim = round((para * cevrik), 2)
    return "{} {} = {} {}".format(para, cevirme1, cevirme2, carpim)


def havadark(ilce):
    darkskyurl = "https://api.darksky.net/forecast/"
    if ilce in dark_ilce_longlati:
        latilong = dark_ilce_longlati[ilce]
    else:
        return "hatalı ilçe girdin"

    urlacan = urllib.request.urlopen(darkskyurl + tokenim.darkskyapi + latilong + "?lang=tr&units=auto")
    veri = json.loads(urlacan.read().decode())
    suanki_ozet = veri["currently"]["summary"]
    saatlik_ozet = veri["hourly"]["summary"]
    derece = str(round(veri["hourly"]["data"][0]["temperature"]))
    return derece + "°C" + " " + saatlik_ozet


def mesajadondur(a):
    listeoldu = list(a)
    del listeoldu[0]
    return "".join(listeoldu).lower().split()


def pingle():
    os.system("start cmd /c ping -n 20 google.com")


def nekadardirup(ilkzaman):
    suankizaman = datetime.datetime.now()
    upzamani = suankizaman - ilkzaman
    uptsaniye = round(upzamani.total_seconds())
    uptdakika = uptsaniye // 60
    uptsaat = uptdakika // 60
    uptgun = uptsaat // 24
    if uptsaniye // 60 < 1:
        return "{} saniye".format(uptsaniye)
    elif uptdakika // 60 < 1:
        upksaniye = uptsaniye % 60
        return "{} dakika, {} saniye".format(uptdakika, upksaniye)
    elif uptsaat // 24 < 1:
        upksaniye = uptsaniye % 60
        upkdakika = uptdakika % 60
        return "{} saat, {} dakika, {} saniye".format(uptsaat, upkdakika, upksaniye)
    else:
        upksaniye = uptsaniye % 60
        upkdakika = uptdakika % 60
        upksaat = uptsaat % 24
        return "{} gün, {} saat, {} dakika, {} saniye".format(uptgun, upksaat, upkdakika, upksaniye)


def acilis(botacilisi):
    return str(botacilisi)


mesajlarakarsilik = {
    "sa": "as",
    "ananzaa": "sensin o",
    "çal": "#play",
    "naber": "iyi senden",
    "anan": "102 92"
}

oynamalar = ["oyun", "nabıyom", "nabıyorum", "neyapıyorum"]
hazirlik = ["hazır", "hazir", "ready", "hazırız", "bura"]
dark_ilce_longlati = {
    "maltepe": "40.953845,29.124498",
    "acıbadem": "41.005202, 29.043165"
}
