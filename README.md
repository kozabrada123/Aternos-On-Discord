![Aternos On Discord (Updated)](https://repository-images.githubusercontent.com/457308479/f3408eec-a02b-4846-9484-180cfb0be4d3)
![GitHub](https://img.shields.io/github/license/kozabrada123/Aternos-On-Discord)
![GitHub top language](https://img.shields.io/github/languages/top/kozabrada123/Aternos-On-Discord)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/kozabrada123/Aternos-On-Discord)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/kozabrada123/Aternos-On-Discord)
![GitHub issues](https://img.shields.io/github/issues/kozabrada123/Aternos-On-Discord)
![GitHub last commit](https://img.shields.io/github/last-commit/kozabrada123/Aternos-On-Discord)


A Discord bot made in Python which manages an Aternos Minecraft server.


Logins to Aternos and can start the server and take commands from Discord.


An update of Mekolaos's repo.


- [Aternos On Discord](#aternos-on-discord)
  - [Prerequisites](#prerequisites)
  - [Getting Started](#getting-started)
    - [Windows/Mac/Linux (x64)](#windowsmaclinux-x64)
    - [Raspberry Pi (ARM)](#raspberry-pi-arm)
  - [Usage](#usage)
  - [Cloud Hosting Note](#cloud-hosting-note)



## Prerequisites

* Python 3.7 or higher
* A Discord server for which you have the rights to add a bot
* An Aternos account



## Getting Started

### Windows/Mac/Linux (x64)

1. Git clone this repository
2. Install it using either:
   * Copy, paste and execute this command inside the project folder: ```pip install -r requirements.txt```
3. Setup a [Bot Account](https://discordpy.readthedocs.io/en/latest/discord.html)
   - You'll need the Bot Token for setting up the Bot

4. Open Settings.py in a text editor or ide:
- Set `Token = ****` to your bot token, so `Token = "1w3prk3adjjbfp8d91r3onls8t1roy7f7pf4zx5zmdywh5qemhuulumybl2"`
- Set `Username = ****` to your aternos username, so `Username = "AnAternosUsername"`
- Set `Password = ****` to your aternos password, so `Password = "AnAternosPassword"`
 
5. Run this command to start the bot : ```python3 Bot.py```


### Raspberry Pi (ARM)

Before following the instructions, make sure you have the following installed: 
- `sudo apt-get install libxml2-dev libxslt-dev python-dev`
- `sudo apt-get install python3-lxml python-lxml`
- `sudo apt-get install python3-wheel`


1. Git clone this repository
2. Install it using `pip3 install -r requirements.txt` inside the folder
   - **NOTE**: This may take a while even on higher end Pi's
3. Setup a [Bot Account](https://discordpy.readthedocs.io/en/latest/discord.html)
   - You'll need the Bot Token for setting up the Bot
4. Setup Settings.py:
- Set `Token = ****` to your bot token
- Set `Username = ****` to your aternos username
- Set `Password = ****` to your aternos password

5. Setup Chromium 
   1. `sudo apt-get install chromium-browser`
   2. `sudo apt-get install chromium-chromedriver`
   ~~3. In `connect_and_launch.py`, change driver executable path to `'/usr/lib/chromium-browser/chromedriver'`~~ This is deprecated in selenium, should not be needed
6. Run the bot with `python3 Bot.py`


*Note: some commands were removed from the original Aternos on Discord for simplicity, status and info have been merged.*

## Usage:

### Discord Commands:
* --launch - starts the server
* --status - displays info about the server
* --help - displays commands


## Cloud Hosting Note

*Cloud hosting this bot would require some workarounds as Aternos recognizes you are connecting from a data center and prompts for a captcha test.* - Original note from Mekolaos, now still aplies but wouldn't work anyway as I'm not sure if you can run non headless in servers


## Acknowledgments

* - [Mekolaos, creator of the original Aternos-On-Discord](https://github.com/Mekolaos)


