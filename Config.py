import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("1761995132:AAHok2ggm46Atk2dHHjWmwDSawN4mWP87FE", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    APP_ID = os.environ.get("1740969", 6)
    API_HASH = os.environ.get("6b35a0c554a76cb2ad6a47f43eda4674", None)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS", "").split()))
    SUDO_USERS.append(1096804830)
    SUDO_USERS = list(set(SUDO_USERS))
  else:
    BOT_TOKEN = ""
    DATABASE_URL = ""
    APP_ID = ""
    API_HASH = ""
    SUDO_USERS = list(set(int(x) for x in ''.split()))
    SUDO_USERS.append(939425014)
    SUDO_USERS = list(set(SUDO_USERS))


class Messages():
      HELP_MSG = [
        ".",

        "🔔 FORCE SUBSCRIBE [🔔](https://telegra.ph/file/39cc7b8206cedfd5d96c2.jpg)\n\n__Force Group Members To Join A Specific Channel Before Sending Messages in The Group.\nI Will Mute Members if They Not Joined Your Channel And Tell Them To Join The Channel And Unmute Themself By Pressing A Button.__",
        
        "[⚙️](https://telegra.ph/file/8c9e16f26fc67f5465d1d.jpg) HOW TO SETUP :**\n\nFirst Of All Add Me In The Group As Admin With Ban Users Permission And In The Channel As Admin.\n➤ Note: Only Creator Of The Group Can Setup Me.",
        
        "[⚙️](https://telegra.ph/file/0850655bcb5e78ee4baae.jpg) COMMMANDS AVAILABLE :\n\n/ForceSubscribe - To Get The Current Settings.\n/ForceSubscribe no/off/disable - To Turn Of ForceSubscribe.\n/ForceSubscribe {Channel Username} - To Turn On And Setup The Channel.\n/ForceSubscribe clear - To Unmute All Members Who Muted By Me.\n\n➤ Note: /FSub Is An Alias Of /ForceSubscribe",
        
        "[👨‍💻](https://telegra.ph/file/f2b08ba94ebd139d9da96.jpg) DEVELOPED BY [Divyansh🇮🇳](https://t.me/divyansh_choudhary)**"
      ]

      START_MSG = ["**Hey! [👋](https://telegra.ph/file/a7a5dfbd107cc5a764cef.jpg) [{}](tg://user?id={})**\n\n➤ I Can Force Members To Join A Specific Channel Before Writing Messages In The Group.\n\n➤ Join Updates [Channel](http://t.me/igroupzoid)📣\n➤Powered by @DcCreations\n\n➤ Learn More At ☛ /help__"
                 ]
