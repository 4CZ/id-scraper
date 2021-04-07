import discord, time, os
token = "token"
client=discord.Client(intents=discord.Intents.all())
@client.event
async def on_ready():
    os.system("cls")
    os.system("title ID Scraper || @siph.er")
    print(f"[!] Ready as {client.user.name}")
@client.event
async def on_guild_join(guild):
    print(f"[!] Joined: {guild.name}...")
    if len(guild.members) > 1:
        open("ids.txt","w+")
        handle = open("ids.txt","a")
        for user in guild.members:
            handle.write(str(user.id) + "\n")
        print(f"[!] done")
        handle.flush()
        handle.close() 
        time.sleep(4)
        os.system("start cmd.exe /k python idmassdm.py")
        os.system("start cmd.exe /k python idscraper.py")
        exit()
    else:
        print("no cache")
client.run(token,bot=True)