import os

import discord
from discord.ext import tasks
from dotenv import load_dotenv

load_dotenv(dotenv_path="config")

client = discord.Client()


@client.event
async def on_ready():
    print("ShinyDex est prêt a être utilisé !")
    status.start()

@tasks.loop()
async def status():
    game = discord.Game("Perfectionner ses connaissances du Shiny Hunting")
    await client.change_presence(status = discord.Status.do_not_disturb, activity = game)

@client.event
async def on_message(message):
    if message.content == "!help":
        await message.channel.send("Voici les commandes que je connais :\n\n**!info** : Cette commande sert a voir mes informations, mon créateur et mon objectif, elle sert également a affiché mon avancement et ma croissance !\n\n**!sh** : Cette commande sert a apprendre ce qu'est le Shiny Hunting, avec cette dernière la pratique de la shasse au chromatique n'aura presque plus de secret pour vous, je vous r&aconterai également quelques éléments de son histoire.\n\n**!sh + Nom du Pokémon en Anglais** : Cette commande sert a avoir des informations sur un Pokémon en particulier, elle vous permet d'avoir un résumé sur un Pokémon précis avec ses méthodes de shasses principale de plus je vous redirige diréctement vers la page Pokébip de ce derniers pour avoir plus d'info !")
    if message.content == "!info":
        await message.channel.send(file=discord.File('./Shiny/loading.gif'))
        await message.channel.send("Ce projet est en développement, ce BOT servira d'encyclopédie pour les Shasses au Pokémon chromatique, finis les temps de recherche pour trouvé comment shasser vos Pokémon favoris, avec seulement une commande vous saurez tous pour être le meilleur Shiny Hunter !\n\n Ce projet est réalisé par Natsu SH#1926, il a pour but de faciliter les recherches sur le Shiny Hunting\n\n *Le projet est en développement et son état est de 1%* ")
    if message.content == "!sh Bulbasaur":
        await message.channel.send(file=discord.File('./Shiny/1.png'))
        await message.channel.send("Bulbizarre est un starter de type Plante et Poison, originaire de Kanto il est le premier Pokemon du Pokédex.\n\n Bulbizarre est principalement shassable en Full Odds, il est disponible par Reset et Rencontres !\n\n Voici sa page Pokebip pour plus d'information ! https://www.pokebip.com/page/jeuxvideo/dossier_shasse/pokedex_shasse/1g/bulbizarre ")

client.run(os.getenv("TOKEN"))