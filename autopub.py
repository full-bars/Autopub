import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Load target channel IDs from .env (comma-separated)
CHANNEL_IDS = os.getenv("TARGET_CHANNEL_IDS", "")
ANNOUNCEMENT_CHANNEL_IDS = [int(cid.strip()) for cid in CHANNEL_IDS.split(",") if cid.strip().isdigit()]

# Set up Discord intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.messages = True

# Initialize bot
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"[AutoPublisher] Logged in as {bot.user}")

@bot.event
async def on_message(message):
    # Only act on messages in target channels
    if message.channel.id not in ANNOUNCEMENT_CHANNEL_IDS:
        return

    # Skip bot-authored messages unless they came from a webhook
    if message.webhook_id is None and message.author.bot:
        return

    # Only publish if it's a news channel
    if not message.channel.is_news():
        return

    try:
        await message.publish()
        print(f"[AutoPublisher] Published message in channel ID {message.channel.id}")
    except discord.Forbidden:
        print(f"[AutoPublisher] Missing MANAGE_MESSAGES permission for channel {message.channel.id}")
    except discord.HTTPException as e:
        print(f"[AutoPublisher] Failed to publish in channel {message.channel.id}: {e}")

bot.run(TOKEN)