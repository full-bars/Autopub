# AutoPublisher Bot

Automatically publishes Discord announcement messages so follower servers get updates instantly — no human delay.
---

## Setup

1. Clone the repo and create a virtual environment:
   ```bash
   python -m venv autopub-env   # Windows
   python3 -m venv autopub-env  # macOS/Linux
   ```

2. Activate the virtual environment:

   - **Windows (PowerShell):**
     ```powershell
     .\autopub-env\Scripts\Activate.ps1
     ```

   - **macOS/Linux (bash/zsh):**
     ```bash
     source autopub-env/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install discord.py python-dotenv
   ```

4. Create a `.env` file in the root folder:
   ```env
   DISCORD_TOKEN=your-bot-token
   TARGET_CHANNEL_IDS=123456789012345678,123456789012345679
   ```

5. Run the bot:
   ```bash
   python autopub.py
   ```

---

## Notes

- Only works with **announcement (news)** channels
- Ignores bot-authored messages unless sent via webhook
- `.env` is excluded via `.gitignore` for safety
- For Linux servers, you can run it as a `systemd` service (see below)

---

## Optional: Run on boot as a systemd Service (Linux)

Create `/etc/systemd/system/autopub.service`:

```ini
[Unit]
Description=Discord AutoPublisher Bot
After=network.target

[Service]
User=your-username
WorkingDirectory=/home/your-username/autopub
ExecStart=/home/your-username/autopub/autopub-env/bin/python /home/your-username/autopub/autopub.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Then enable and start:

```bash
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable autopub
sudo systemctl start autopub
```
