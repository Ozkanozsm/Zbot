import os
import time
import datetime
import json
import urllib.request

prefix = "'"
onay = "oke"


def muzik(muzikadi):
    return "Spotify'dan " + muzikadi + " adlı şarkıyı dinliyorsun."


def oyun(oyunadi):
    return oyunadi + " oynuyorsun."


def nabiyom(aktivitesi):
    if not aktivitesi:
        ylnck = "Hiçbir şey oynamıyorsun"
    elif aktivitesi.type.name == "listening":
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


def denemefonk(ilce):
    if ilce == "maltepe":
        latilong = "40.953845,29.124498"
    else:
        latilong = "hatalı ilçe girdin mal mısın lan şerro"
    return latilong


def havadark(ilce):
    darkskyapi = "5dc9545bd1a1234aee3dce97e8953b66/"
    darkskyurl = "https://api.darksky.net/forecast/"
    if ilce == "maltepe":
        latilong = "40.953845,29.124498"
    elif (ilce == "acıbadem") or (ilce == "acibadem"):
        latilong = "41.005202, 29.043165"
    else:
        return "hatalı ilçe girdin mal mısın lan şerro"

    urlacan = urllib.request.urlopen(darkskyurl + darkskyapi + latilong + "?lang=tr&units=auto")
    veri = json.loads(urlacan.read().decode())
    suanki_ozet = veri["currently"]["summary"]
    saatlik_ozet = veri["hourly"]["summary"]
    derece = str(round(veri["hourly"]["data"][0]["temperature"]))
    return derece + "°C" + " " + saatlik_ozet

def havaopen(ilce):
    openapi = "a4972480eb62ae01c53bc8e831cb37f6"
    openurl = ""

def mesajadondur(a):
    listeoldu = list(a)
    del listeoldu[0]
    return "".join(listeoldu).lower().split()


def pingle():
    os.system("start cmd /c ping -n 20 google.com")


def nekadardirup(ilkzaman):
    suankizaman = datetime.datetime.now()
    upzamani = suankizaman - ilkzaman
    if upzamani.seconds // 60 < 1:
        return "{} saniye".format(upzamani.seconds)
    else:
        updakkasi = upzamani.seconds // 60
        upsaniyesi = upzamani.seconds % 60
        return "{} dakika {} saniye".format(updakkasi, upsaniyesi)


mesajlarakarsilik = {
    "sa": "as",
    "ananzaa": "sensin o",
    "çal": "#play",
    "naber": "iyi senden",
    "anan": "102 92",
    "yrk": "anandır"
}

oynamalar = ["oyun", "nabıyom", "nabıyorum", "neyapıyorum"]
hazirlik = ["hazır", "hazir", "ready", "hazırız", "bura"]
ilce_longlati = {"maltepe"}
