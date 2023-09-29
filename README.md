# Discord User Token Auto Message Script

This Python script allows you to send automated messages on Discord using your user token.

## Prerequisites

Before using this script, ensure you have the following:

- Python 3.x installed on your computer.
- Your Discord user token. [Here's how to obtain your user token](#how-to-get-your-discord-user-token).
- The channel ID where you want to send messages. [Here's how to get a channel ID](#how-to-get-a-discord-channel-id).
- The message you want to send.

## How to Get Your Discord User Token

1. Open Discord in your web browser or desktop app.
2. Press `Ctrl + Shift + I` (or `Cmd + Option + I` on Mac) to open the Developer Tools.
3. Navigate to the "Application" tab.
4. In the left sidebar, click on "Local Storage," then select `https://discord.com`.
5. Look for the "token" key in the right-hand pane. This is your user token.

**Warning:** Keep your token private and never share it with anyone.

## How to Get a Discord Channel ID

1. Open Discord and go to the server and channel where you want to send messages.
2. Right-click on the channel name in the left sidebar.
3. Click "Copy ID." The channel ID is now in your clipboard.

## Usage

2. Open the script in a text editor.
3. Replace the following variables in the script with your own values:
- `channel_id`: The channel ID where you want to send messages.
- `message`: The message you want to send.
- `delay`: The delay in seconds between messages (5 seconds is recommended).
- `YOUR_TOKEN`: Your Discord user token.

  **make sure that the token is between the "" and when you paste the token paste it without their ""!

4. Save the changes.
5. Open your terminal/command prompt and navigate to the script's directory.
6. Run the script: python sender.py


**Note:** Make sure to use this script responsibly and only for educational purposes.

## Disclaimer

This script is provided for educational purposes only. The author does not take any responsibility for its usage.

## Requirements

You can install the required Python packages using the following command:
pip install requests





---

Made by aro22 on Discord.

contact me if you needed help.












