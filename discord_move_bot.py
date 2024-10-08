import os
import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load environment variables from a .env file (e.g., for the bot token)
load_dotenv()

# Set up the bot with necessary permissions (intents)
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent to read messages
bot = commands.Bot(command_prefix='!', intents=intents)  # Initialize the bot with a command prefix

# Sync the command tree (slash commands) when the bot is ready
@bot.event
async def on_ready():
    await bot.tree.sync()  # Sync application commands with Discord
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')  # Print bot login info
    print('------')

# Define a slash command to move messages between channels
@bot.tree.command(name="move", description="Move messages from one channel to another.")
@app_commands.describe(
    channel_from="The source channel to move messages from.",
    channel_to="The target channel to move messages to.",
    action="Action to perform: -all, -last, -from_user.",
    time_period="Time period for '-last' action (e.g., '7 days', '1 hour').",
    user="The user to filter messages for the '-from_user' action."
)
async def move_messages(
    interaction: discord.Interaction,
    channel_from: discord.TextChannel,
    channel_to: discord.TextChannel,
    action: str = '-all',
    time_period: str = None,
    user: discord.User = None
):
    """
    Moves messages from one channel to another based on user command.

    Arguments:
    - channel_from: The source channel to move messages from.
    - channel_to: The target channel to move messages to.
    - action: The action to perform. Options are "-all", "-last <xy-time>", "-from_user".
    - time_period: The time period for "-last" action (e.g., "7 days", "1 hour").
    - user: The user to filter messages for the "-from_user" action.
    """
    await interaction.response.defer()  # Defer the response to avoid interaction timeout

    # Validate the action parameter
    if action not in ['-all', '-last', '-from_user']:
        await interaction.followup.send("Invalid action. Use '-all', '-last <xy-time>', or '-from_user'.")
        return

    messages = []
    # Fetch the message history from the source channel
    async for message in channel_from.history(limit=None):
        if action == '-all':
            messages.append(message)  # Collect all messages
        elif action == '-last':
            # Validate and parse the time period for the '-last' action
            if not time_period:
                await interaction.followup.send("Please specify a time period for '-last'.")
                return
            try:
                number, unit = time_period.split()
                number = int(number)
                # Handle singular/plural cases
                if unit.endswith('s'):
                    unit = unit[:-1]
                # Create a time delta for filtering based on the parsed unit
                delta = timedelta(**{f'{unit}s': number})
            except (ValueError, KeyError):
                await interaction.followup.send("Invalid time period format. Use '<number> days' or '<number> hours'.")
                return

            # Filter messages within the given time period
            if datetime.now() - message.created_at <= delta:
                messages.append(message)
        elif action == '-from_user' and user and message.author == user:
            messages.append(message)  # Collect messages from the specified user

    # Move messages to the target channel in reverse order to maintain original order
    for message in reversed(messages):
        attachments = [await attachment.to_file() for attachment in message.attachments if attachment and attachment.url]
        author_info = f"{message.author.display_name} ({message.author}):"
        await channel_to.send(content=f"{author_info}\n{message.content}", files=attachments)
        await message.delete()  # Delete the original message from the source channel

    # Notify the user how many messages were moved
    await interaction.followup.send(f"Moved {len(messages)} messages from {channel_from.name} to {channel_to.name}.")

# Define a slash command to delete messages in a channel based on a timescale
@bot.tree.command(name="delete", description="Delete messages in a channel based on a time period.")
@app_commands.describe(
    channel="The channel to delete messages from.",
    time_period="Time period to delete messages from (e.g., '7 days', '1 hour')."
)
async def delete_messages(
    interaction: discord.Interaction,
    channel: discord.TextChannel,
    time_period: str
):
    """
    Deletes messages in a channel based on a specified time period.

    Arguments:
    - channel: The channel to delete messages from.
    - time_period: The time period to filter messages (e.g., '7 days', '1 hour').
    """
    await interaction.response.defer()  # Defer the response to avoid interaction timeout

    try:
        number, unit = time_period.split()
        number = int(number)
        # Handle singular/plural cases
        if unit.endswith('s'):
            unit = unit[:-1]
        # Create a time delta for filtering based on the parsed unit
        delta = timedelta(**{f'{unit}s': number})
    except (ValueError, KeyError):
        await interaction.followup.send("Invalid time period format. Use '<number> days' or '<number> hours'.")
        return

    # Calculate the cutoff time
    cutoff_time = datetime.now() - delta

    # Fetch and delete messages older than the cutoff time
    deleted_count = 0
    async for message in channel.history(limit=None, before=cutoff_time):
        await message.delete()
        deleted_count += 1

    # Notify the user how many messages were deleted
    await interaction.followup.send(f"Deleted {deleted_count} messages from {channel.name} older than {time_period}.")

# Get the bot token from environment variables and start the bot
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
