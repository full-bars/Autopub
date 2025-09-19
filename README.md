# AutoPublisher Bot

This bot automatically publishes messages from Discord announcement channels.

## Setup

1. Clone the repo and create a virtual environment:
   ```
   python -m venv autopub-env
   ```

2. Activate the virtual environment:

   - **Windows (PowerShell):**
     ```
     .\autopub-env\Scripts\Activate.ps1
     ```

   - **macOS/Linux (bash/zsh):**
     ```
     source autopub-env/bin/activate
     ```

3. Install dependencies:
   ```
   pip install discord.py python-dotenv
   ```

4. Create a `.env` file in the root folder:
   ```
   DISCORD_TOKEN=your-bot-token
   TARGET_CHANNEL_IDS=comma,separated,channel,IDs
   ```

5. Run the bot:
   ```
   python autopub.py
   ```

## Notes

- Only works with announcement (news) channels
- Ignores bot-authored messages unless sent via webhook
- `.env` is excluded via `.gitignore`
