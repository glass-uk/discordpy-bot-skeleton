# Python Discord Bot Skeleton
This project is a skeleton project designed to help you get up and running quickly when creating a discord bot.
## Features
* Cogs.
* Live reloading of cogs useful for updating the bot remotely without downtime.
* .env support to store multiple keys.

## Quick Guide 
```
1. Clone project 
2. Install requirements.txt
3. Add your discord bot key into .env.
4. Update bot.py line 20 to match the variable name:
    * bot.run(os.getenv('LIVE_BOT'))
Based on what you have entered in .env.
5. Run bot.py and message your bot ;HelloWorld.
6. Continue Adding commands and cogs to your liking.
```

## Reloading Cogs
I have hosted my personal discord bot on AWS EC2 so I implemented the reload cog command to reduce restarts.
### How I reload cogs remotely
```
1. FTP into AWS server.
2. Upload your updated cog into the server cogs folder.
3. Reload your cog by messaging your bot with ;reload cogname.
4. Cog should now be updated.
```
### Limitations
This will not work if the cog you are reloading was not initially added when running the bot. To add new cogs to the running bot you will need to restart the bot.

## Recommended
Add these to the .gitignore file:
```
.env
.gitignore
```