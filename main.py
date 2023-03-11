import interactions
from colorama import Fore
from subcommands import *

# -- Constantes and Variables -- #

TOKEN = ""
ready = False
bot = interactions.Client(token=TOKEN)
BOT_OWNER = bot.me.owner.id
help_cmd = HelpCommand()

# -- Fonctions -- #

def logger(message, type="INFO"):
    if(type == "INFO"):
        print(Fore.GREEN + "[INFO] " + message + Fore.RESET)
    elif(type == "WARNING"):
        print(Fore.YELLOW + "[WARNING] " + message + Fore.RESET)
    elif(type == "ERROR"):
        print(Fore.RED + "[ERROR] " + message + Fore.RESET)
    else:
        print(Fore.CYAN + "[DEBUG] " + message + Fore.RESET)

## -- Events -- ##

@bot.event
async def on_start():
    global ready
    if(not ready):
        logger(f"Bot `{bot.me.name}` connecté avec succès !")
        ready = True
        await bot.change_presence(
            interactions.ClientPresence(
                status=interactions.StatusType.DND,
                activities=[
                    interactions.PresenceActivity(
                        name="à la recherche de bugs !",
                        type=interactions.PresenceActivityType.GAME
                    )
                ]
            )
        )

@bot.event
async def on_command_error(ctx: interactions.CommandContext, error):
    owner_user = await interactions.get(bot, interactions.User, object_id=BOT_OWNER)
    embed = interactions.Embed(title="Une erreur est survenue !", color=0xFF0000)
    embed.add_field(name="Une erreur est survenue !", value=f"```{error}```")
    logger(f"Une erreur est survenue !\n{error}", type="ERROR")
    await owner_user.send(embed=embed)

## -- Commands -- ##

@bot.command(
    name="help",
    description="Affiche l'aide du bot"
)
async def help(ctx: interactions.CommandContext):
    embed = interactions.Embed(title="Aide du bot", color=0x00FF00)
    embed.add_field(name="Aide du bot", value=help_cmd.get_help_informations())
    await ctx.send(embeds=embed)


@bot.command(
    name="add_help",
    description="Ajoute une commande à l'aide du bot",
    default_member_permissions=interactions.MemberPermissions.ADMINISTRATOR
)
async def add_help(ctx: interactions.CommandContext, name: str, description: str):
    if(ctx.user.id == BOT_OWNER):
        help_cmd.add_command(name, description)
        await ctx.send("Commande ajoutée avec succès !")
    else:
        logger("Tentative d'ajout d'une commande à l'aide du bot par un utilisateur non autorisé !", type="WARNING")
        await ctx.send("Vous n'êtes pas autorisé à ajouter une commande à l'aide du bot !")


@bot.command(
    name="remove_help",
    description="Supprime une commande de l'aide du bot",
    default_member_permissions=interactions.MemberPermissions.ADMINISTRATOR
)
async def remove_help(ctx: interactions.CommandContext, name: str):
    if(ctx.user.id == BOT_OWNER):
        help_cmd.remove_command(name)
        await ctx.send("Commande supprimée avec succès !")
    else:
        logger("Tentative de suppression d'une commande de l'aide du bot par un utilisateur non autorisé !", type="WARNING")
        await ctx.send("Vous n'êtes pas autorisé à supprimer une commande de l'aide du bot !")


@bot.command(
    name="ping",
    description="Affiche le ping du bot"
)
async def ping(ctx: interactions.CommandContext):
    await ctx.send(f"Pong ! `{bot.latency * 1000:.0f}ms`")


# -- Lancement du bot -- #
if __name__ == "__main__":
    bot.run()
else:
    logger("Ce fichier ne doit pas être importé !", type="ERROR")
    exit()