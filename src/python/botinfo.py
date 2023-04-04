TOKEN = "MTA4NDA2NDU1MjI4MDQxMjE3MA.GMhAPk.FKOOjmUMxx2OKNdJ2eZF15gQLuQsObpyaB4ICA"
ID_CHANNEL_MEMBER_JOIN: int = 0
ID_CHANNEL_MEMBER_LEAVE: int = 0
ID_OWNER: int = 0

from interactions import Embed

EMBED_JOIN: Embed = Embed(title="Bienvenue !", color=0x00FF00)
EMBED_JOIN.set_footer(text="Merci de lire les règles du serveur !")
EMBED_JOIN.set_thumbnail(url="https://cdn.discordapp.com/attachments/708000000000000000/708000000000000000/unknown.png")

EMBED_LEAVE: Embed = Embed(title="Au revoir !", color=0xFF0000)
EMBED_LEAVE.set_footer(text="Merci d'avoir été parmi nous !")
EMBED_LEAVE.set_thumbnail(url="https://cdn.discordapp.com/attachments/708000000000000000/708000000000000000/unknown.png")