# Discord Channel Merge Bot

This bot helps you move messages from one Discord channel to another. It provides admin commands to move all messages, specific messages within a timeframe, or messages from specific users.

You can also join our NIM community on Discord, Reddit, and Facebook, or visit our homepage:

[![Join our Discord](https://img.shields.io/badge/Discord-Join-blue)](https://discord.com/invite/SVYMhKpCAb)
[![Visit our Homepage](https://img.shields.io/badge/Homepage-Visit-orange)](https://nimiates.org)
[![Visit our Reddit](https://img.shields.io/badge/Reddit-Visit-red)](https://www.reddit.com/r/nimiates/)
[![Visit our Facebook](https://img.shields.io/badge/Facebook-Visit-blue)](https://www.facebook.com/groups/nimiates/)

## Features

- Move all messages from one channel to another.
- Move the last 'X' days of messages.
- Move messages from specific users.
- User-friendly command system.

## Commands

The bot offers the following commands:

- `!move -all -Channel-x -Channel-y`: Move all messages from Channel-x to Channel-y.
- `!move -last <number_of_days> -Channel-x -Channel-y`: Move messages from the last specified number of days from Channel-x to Channel-y.
- `!move -from_user <username> -Channel-x -Channel-y`: Move messages from a specific user in Channel-x to Channel-y.

## Requirements

- Python 3.8 or higher
- Discord API Token
- Discord.py library

## Installation

### Prerequisites

1. **Install Python**: Make sure Python is installed on your system. You can download it from [Python.org](https://www.python.org/downloads/).

2. **Install pip**: Pip is the package installer for Python. It is usually included in Python installations.

### Installation Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/discord-channel-merge-bot.git
   
2. **Change to the project directory**:

`cd discord-channel-merge-bot`

3. **Create a virtual environment**:

`python -m venv venv`

5. **Activate the virtual environment**:

*Windows*:

`venv\Scripts\activate`

*MacOS/Linux*:

`source venv/bin/activate`

5. **Install the dependencies**:

`pip install -r requirements.txt`

### Configuration

1. **Create a `.env` file** in the project directory to store your environment variables:

`DISCORD_TOKEN=your_discord_bot_token_here`

`BOT_OWNER_ID=your_discord_user_id_here`

`DISCORD_PREFIX=!`

2. **Replace the placeholder values with your actual values**.

## Running the Bot

1. **Start the bot**:

`python discord_move_bot.py`

2. **Stop the bot**: To stop the bot, press Ctrl+C in the terminal where it is running.

### More Information
To learn more about running and managing Discord bots, read the official [Discord.py documentation](https://discordpy.readthedocs.io/en/stable/#getting-started).

Join our NIM community on Discord, Reddit, and Facebook, or visit our homepage:

[![Join our Discord](https://img.shields.io/badge/Discord-Join-blue)](https://discord.com/invite/SVYMhKpCAb)
[![Visit our Homepage](https://img.shields.io/badge/Homepage-Visit-orange)](https://nimiates.org)
[![Visit our Reddit](https://img.shields.io/badge/Reddit-Visit-red)](https://www.reddit.com/r/nimiates/)
[![Visit our Facebook](https://img.shields.io/badge/Facebook-Visit-blue)](https://www.facebook.com/groups/nimiates/)

## License
This project is licensed under the MIT License.
